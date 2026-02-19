import os
import shutil
import threading
import requests
import fitz  # PyMuPDF
import customtkinter as ctk
from tkinter import filedialog, messagebox

# --- Configuration ---
OLLAMA_API_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "llama3"  # Change to "mistral" or "gemma" if preferred
CATEGORIES = ["Personal", "Trabajo", "Finanzas", "Educación", "Manuales", "Facturas", "Otros"]

class OllamaClient:
    def __init__(self, model=DEFAULT_MODEL):
        self.model = model

    def classify_text(self, text):
        prompt = f"""
        Actúa como un asistente de organización de archivos.
        Analiza el siguiente texto extraído de un documento PDF y clasifícalo en UNA sola de estas categorías:
        {', '.join(CATEGORIES)}.
        
        Si no estás seguro, usa "Otros".
        Responde SOLAMENTE con el nombre de la categoría, sin explicaciones ni puntos.
        
        Texto del documento (primeros fragmentos):
        {text[:2000]}
        """
        
        try:
            response = requests.post(OLLAMA_API_URL, json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            })
            if response.status_code == 200:
                result = response.json().get("response", "").strip()
                # Clean up response to match categories
                for cat in CATEGORIES:
                    if cat.lower() in result.lower():
                        return cat
                return "Otros"
            else:
                return "Error_API"
        except Exception as e:
            print(f"Error conectando con Ollama: {e}")
            return "Error_Conexión"

class PDFProcessor:
    def extract_text(self, filepath):
        try:
            doc = fitz.open(filepath)
            text = ""
            for page in doc:
                text += page.get_text()
                if len(text) > 2000:  # Optimization: only need start of doc
                    break
            return text
        except Exception as e:
            print(f"Error leyendo PDF {filepath}: {e}")
            return None

    def organize_file(self, filepath, source_dir, target_dir, category):
        try:
            # Create category folder
            cat_path = os.path.join(target_dir, category)
            os.makedirs(cat_path, exist_ok=True)
            
            filename = os.path.basename(filepath)
            dest_path = os.path.join(cat_path, filename)
            
            # Handle duplicates by renaming
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(dest_path):
                dest_path = os.path.join(cat_path, f"{base}_{counter}{ext}")
                counter += 1
            
            # COPY operation (Safety first)
            shutil.copy2(filepath, dest_path)
            return True, dest_path
        except Exception as e:
            return False, str(e)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Organizador Inteligente de PDFs con Ollama")
        self.geometry("700x500")
        
        self.ollama_client = OllamaClient()
        self.pdf_processor = PDFProcessor()
        self.processing = False
        
        self._setup_ui()

    def _setup_ui(self):
        # Title
        self.label_title = ctk.CTkLabel(self, text="Organizador de PDFs (Ollama Local)", font=("Arial", 20, "bold"))
        self.label_title.pack(pady=10)

        # Source Selection
        self.frame_source = ctk.CTkFrame(self)
        self.frame_source.pack(pady=5, padx=20, fill="x")
        self.btn_source = ctk.CTkButton(self.frame_source, text="Origen (Descargas)", command=self.select_source)
        self.btn_source.pack(side="left", padx=10)
        self.lbl_source = ctk.CTkLabel(self.frame_source, text="No seleccionado", text_color="gray")
        self.lbl_source.pack(side="left", padx=10)

        # Target Selection
        self.frame_target = ctk.CTkFrame(self)
        self.frame_target.pack(pady=5, padx=20, fill="x")
        self.btn_target = ctk.CTkButton(self.frame_target, text="Destino (Pen Drive)", command=self.select_target)
        self.btn_target.pack(side="left", padx=10)
        self.lbl_target = ctk.CTkLabel(self.frame_target, text="No seleccionado", text_color="gray")
        self.lbl_target.pack(side="left", padx=10)

        # Options
        self.frame_opts = ctk.CTkFrame(self)
        self.frame_opts.pack(pady=10, padx=20, fill="x")
        self.entry_model = ctk.CTkEntry(self.frame_opts, placeholder_text="Modelo Ollama (ej: llama3)")
        self.entry_model.insert(0, DEFAULT_MODEL)
        self.entry_model.pack(side="left", padx=10, expand=True, fill="x")

        # Action Button
        self.btn_start = ctk.CTkButton(self, text="Iniciar Organización", command=self.start_processing_thread, fg_color="green")
        self.btn_start.pack(pady=10)

        # Log Area
        self.textbox_log = ctk.CTkTextbox(self, height=200)
        self.textbox_log.pack(pady=10, padx=20, fill="both", expand=True)

        # Progress
        self.progressbar = ctk.CTkProgressBar(self)
        self.progressbar.set(0)
        self.progressbar.pack(pady=5, padx=20, fill="x")

    def log(self, message):
        self.textbox_log.insert("end", message + "\n")
        self.textbox_log.see("end")

    def select_source(self):
        path = filedialog.askdirectory()
        if path:
            self.lbl_source.configure(text=path, text_color="white")
            self.source_path = path

    def select_target(self):
        path = filedialog.askdirectory()
        if path:
            self.lbl_target.configure(text=path, text_color="white")
            self.target_path = path

    def start_processing_thread(self):
        if not hasattr(self, 'source_path') or not hasattr(self, 'target_path'):
            messagebox.showwarning("Faltan Datos", "Por favor selecciona origen y destino.")
            return
            
        model = self.entry_model.get()
        self.ollama_client.model = model
        
        self.processing = True
        self.btn_start.configure(state="disabled")
        self.progressbar.set(0)
        
        threading.Thread(target=self.process_files, daemon=True).start()

    def process_files(self):
        self.log(f"--- Iniciando escaneo en: {self.source_path} ---")
        
        pdf_files = [f for f in os.listdir(self.source_path) if f.lower().endswith('.pdf')]
        total = len(pdf_files)
        
        if total == 0:
            self.log("No se encontraron archivos PDF.")
            self.after(0, lambda: self.btn_start.configure(state="normal"))
            return

        success_count = 0
        
        for i, filename in enumerate(pdf_files):
            if not self.processing: break
            
            filepath = os.path.join(self.source_path, filename)
            self.log(f"Procesando: {filename}...")
            
            # Extract Text
            text = self.pdf_processor.extract_text(filepath)
            if not text:
                self.log(f"  [X] No se pudo leer texto de {filename}. Revisa si está encriptado o es imagen.")
                continue

            # Classify
            category = self.ollama_client.classify_text(text)
            self.log(f"  -> Clasificado como: {category}")
            
            if category in ["Error_API", "Error_Conexión"]:
                self.log("  [!] Error de Ollama. Asegúrate que 'ollama serve' esté corriendo.")
                continue

            # Copy
            success, msg = self.pdf_processor.organize_file(filepath, self.source_path, self.target_path, category)
            if success:
                self.log(f"  [OK] Copiado a /{category}/{os.path.basename(msg)}")
                success_count += 1
            else:
                self.log(f"  [X] Error copiando: {msg}")

            # Update progress
            progress = (i + 1) / total
            self.after(0, lambda p=progress: self.progressbar.set(p))

        self.log(f"--- Finalizado. {success_count}/{total} archivos procesados correctamente. ---")
        self.after(0, lambda: self.btn_start.configure(state="normal"))
        self.processing = False

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    
    app = App()
    app.mainloop()
