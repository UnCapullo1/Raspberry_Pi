import os
import glob
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from colorama import init, Fore, Style

init(autoreset=True)

# Configuraciones
DATA_PATH = "data"
CHROMA_PATH = "chroma_db"
EMBEDDING_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"

def main():
    print(Fore.CYAN + "=== ADPV: Ingesta de Documentos ===")
    
    # Crear carpeta de datos si no existe
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)
        print(Fore.YELLOW + f"He creado la carpeta '{DATA_PATH}'. Por favor, pon tus PDFs ahí y vuelve a ejecutar este script.")
        return

    # Buscar PDFs
    pdf_files = glob.glob(os.path.join(DATA_PATH, "*.pdf"))
    if not pdf_files:
        print(Fore.RED + f"No se encontraron archivos PDF en la carpeta '{DATA_PATH}'.")
        return

    print(Fore.GREEN + f"Se encontraron {len(pdf_files)} documentos PDF. Procesando...")

    # Cargar documentos
    documents = []
    for pdf in pdf_files:
        print(Fore.WHITE + f" -> Leyendo: {os.path.basename(pdf)}")
        loader = PyPDFLoader(pdf)
        documents.extend(loader.load())

    # Dividir el texto en fragmentos (chunks)
    print(Fore.CYAN + "Dividiendo documentos en fragmentos...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    print(Fore.GREEN + f"Se han generado {len(chunks)} fragmentos de texto.")

    # Generar Embeddings y Base de Datos Vectorial
    print(Fore.CYAN + f"Cargando modelo de incrustaciones (embeddings): {EMBEDDING_MODEL}")
    print(Style.DIM + "(Esto puede tardar un poco la primera vez que se descarga)")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    print(Fore.CYAN + "Creando base de datos vectorial local (ChromaDB)...")
    db = Chroma.from_documents(chunks, embeddings, persist_directory=CHROMA_PATH)
    
    print(Fore.GREEN + Style.BRIGHT + "\n¡Base de datos RAG creada con éxito!")
    print(Fore.WHITE + f"La información guardada en '{CHROMA_PATH}' está lista para que el asistente la consulte.")

if __name__ == "__main__":
    main()
