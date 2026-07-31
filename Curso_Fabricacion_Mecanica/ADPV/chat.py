import os
import sys
import tempfile
from colorama import init, Fore, Style

# Ocultar advertencias de TensorFlow / Torch u otras librerías
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3" 

import pyttsx3
import speech_recognition as sr
from faster_whisper import WhisperModel
from langchain_community.llms import Ollama
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate

init(autoreset=True)

# Configuraciones Base
CHROMA_PATH = "chroma_db"
EMBEDDING_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"
LLM_MODEL = "llama3.1" # Cámbialo a 'qwen2.5:14b' si lo prefieres para español/gallego

class ADPV:
    def __init__(self):
        print(Fore.CYAN + "Iniciando ADPV (Asistente de Diseño Por Voz)...")
        print(Fore.CYAN + "Cargando motor de voz (Text-to-Speech)...")
        self.tts_engine = pyttsx3.init()
        self.setup_voice()
        
        print(Fore.CYAN + "Cargando motor de reconocimiento (Faster-Whisper para RTX 4090)...")
        self.whisper = WhisperModel("tiny", device="cuda", compute_type="float16")
        self.recognizer = sr.Recognizer()

        print(Fore.CYAN + "Conectando a base de datos de PDFs local...")
        if not os.path.exists(CHROMA_PATH):
            print(Fore.RED + f"Error: No se encuentra la base de datos '{CHROMA_PATH}'.")
            print(Fore.YELLOW + "Primero guarda PDFs en la carpeta 'data' y ejecuta 'python ingest.py'.")
            sys.exit(1)
            
        self.embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
        self.db = Chroma(persist_directory=CHROMA_PATH, embedding_function=self.embeddings)
        
        print(Fore.CYAN + f"Cargando modelo LLM ({LLM_MODEL} vía Ollama)...")
        self.llm = Ollama(model=LLM_MODEL)
        
        self.prompt = PromptTemplate.from_template(
            "Eres el Asistente de Diseño por Fabricación Mecánica (ADPV).\n"
            "Responde a la pregunta de manera clara y directa basándote ÚNICAMENTE en el siguiente contexto extraído de los PDFs.\n"
            "Si el contexto no tiene la respuesta, di que no has encontrado esa información.\n"
            "MANTÉN el idioma en el que te han preguntado (Español o Gallego).\n\n"
            "Contexto de los PDFs:\n{context}\n\n"
            "Pregunta del usuario: {question}\n\n"
            "Respuesta:"
        )

        
    def setup_voice(self):
        # Intentar buscar una voz en español
        voices = self.tts_engine.getProperty('voices')
        for voice in voices:
            if 'es' in voice.languages or 'spanish' in voice.name.lower() or 'es-es' in voice.id.lower() or 'es-mx' in voice.id.lower():
                self.tts_engine.setProperty('voice', voice.id)
                break
        self.tts_engine.setProperty('rate', 160) # Velocidad al hablar
        
    def speak(self, text):
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print(Fore.YELLOW + "\n🎙️  Ajustando ruido ambiente... por favor espera un instante silencioso.")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print(Fore.GREEN + Style.BRIGHT + "🗣️  ¡Habla ahora! (Te estoy escuchando)...")
            try:
                # timeout = tiempo max para empezar a hablar; phrase_time_limit = duracion maxima
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=30)
                print(Fore.CYAN + "Procesando audio de voz...")
                
                # Guardar un momento como archivo para pasarlo a whisper
                with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                    f.write(audio.get_wav_data())
                    tmp_name = f.name
                    
                try:
                    segments, info = self.whisper.transcribe(tmp_name, language="es") # Force es for best accuracy in ES/GL handling
                    text = "".join([segment.text for segment in segments])
                    return text.strip()
                finally:
                    if os.path.exists(tmp_name):
                        os.remove(tmp_name)
            except sr.WaitTimeoutError:
                print(Fore.RED + "No se ha detectado voz dentro del tiempo límite.")
                return ""
            except Exception as e:
                print(Fore.RED + f"Error al usar el micrófono: {e}")
                return ""

    def query_rag(self, question):
        print(Fore.CYAN + "Buscando en la base de datos de PDFs...")
        docs = self.db.similarity_search(question, k=4)
        if not docs:
            return "Lo siento, no he encontrado ningún documento relevante."
            
        context = "\n---\n".join([doc.page_content for doc in docs])
        formatted_prompt = self.prompt.format(context=context, question=question)
        
        print(Fore.CYAN + "Procesando respuesta con la IA Local...")
        response = self.llm.invoke(formatted_prompt)
        return response

def main():
    print(Style.BRIGHT + Fore.WHITE + "========================================")
    print(Style.BRIGHT + Fore.WHITE + "     BIENVENIDO A ADPV (RAG Local)      ")
    print(Style.BRIGHT + Fore.WHITE + "========================================")
    
    app = ADPV()
    
    # Menú de configuración inicial
    print(Fore.GREEN + "\n¿Cómo prefieres INTRODUCIR preguntas?")
    print("1: Teclado")
    print("2: Micrófono (Voz)")
    entrada = input("Elige (1 ó 2): ").strip()
    usa_voz_entrada = (entrada == "2")
    
    print(Fore.GREEN + "\n¿Cómo prefieres RECIBIR las respuestas?")
    print("1: Sólo texto")
    print("2: Texto y Voz (Lectura por altavoz)")
    salida = input("Elige (1 ó 2): ").strip()
    usa_voz_salida = (salida == "2")
    
    app.speak("Sistema configurado y listo para ayudarte.")
    print(Fore.GREEN + Style.BRIGHT + "\n=== CHAT INICIADO (Escribe 'salir' para terminar) ===\n")
    
    while True:
        if usa_voz_entrada:
            pregunta = app.listen()
            if pregunta:
                print(Fore.WHITE + Style.BRIGHT + f"\nHas dicho (Interpretado): {pregunta}")
            else:
                input("Presiona ENTER para volver a intentar hablar o escribe 'salir': ")
                continue
        else:
            pregunta = input(Fore.YELLOW + "\nPregunta para ADPV: " + Fore.WHITE)
            
        if not pregunta:
            continue
            
        if pregunta.lower().strip() in ["salir", "exit", "quit"]:
            print(Fore.CYAN + "¡Hasta luego!")
            break
            
        # Obtener respuesta
        respuesta = app.query_rag(pregunta)
        
        print(Fore.GREEN + Style.BRIGHT + "\n🤖 ADPV:")
        print(Fore.WHITE + respuesta)
        
        if usa_voz_salida:
            app.speak(respuesta)

if __name__ == "__main__":
    main()
