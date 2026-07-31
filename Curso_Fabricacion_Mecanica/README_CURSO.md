# Curso: Diseño por Fabricación Mecánica (DEFAME)

Este directorio contiene todo el material académico, scripts de cálculo, ejercicios de programación y herramientas de IA desarrolladas durante el curso de **Diseño por Fabricación Mecánica**.

---

## 📂 Estructura del Contenido

### 1. 📟 [TI-84](file:///c:/Users/sousi/OneDrive/Documents/GitHub/Dise-o-por-fabricacion-mecanica-/Curso_Fabricacion_Mecanica/TI-84/) - Calculadoras para TI-84 Plus CE Python
Programas de cálculo simplificados, optimizados para ejecutarse en el intérprete de Python de la calculadora gráfica de Texas Instruments. Tienen dependencias mínimas y entrada/salida por consola clásica.
*   **`CALC_MEC.py`**: Cálculos de diseño mecánico para el soporte de moto (fuerza de cilindro, tijeras, torque de husillo, pandeo, cortadura).
*   **`HYDRA.py`**: Parámetros básicos para sistemas hidráulicos.
*   **`T_FABRIC.py`**: Tolerancias y ajustes dimensionales recomendados según tolerancias estándar.
*   **`INY_FOR.py`**, **`INY_MAQ.py`**, **`INY_MOL.py`**: Cálculos relacionados con el moldeo por inyección de polímeros (fuerza de cierre de prensa, parámetros de máquina e inyección, y diseño del molde).
*   **`TROQ1.py`** a **`TROQ5.py`**: Cálculos para diseño de troquelería progresiva, fuerzas de corte y desgarro de chapa.

### 2. ⚙️ [Navantia](file:///c:/Users/sousi/OneDrive/Documents/GitHub/Dise-o-por-fabricacion-mecanica-/Curso_Fabricacion_Mecanica/Navantia/) - Ejercicios de Fabricación
Fórmulas y scripts prácticos relacionados con la fabricación mecánica inspirados en ejercicios prácticos:
*   **`01TOLERA.py`**: Diámetro medio, unidad de tolerancia IT y juegos/aprietos.
*   **`02TIEMPO.py`**: Tiempos de torneado, fresado y operaciones mecánicas.
*   **`03CONOSG.py`**: Ángulos y dimensiones para el torneado de conos.
*   **`04ENGRAN.py`**: Dimensionamiento de engranajes rectos e helicoidales (módulos, diámetros primitivos, adendo, dedendo).
*   **`05CHAPAF.py`**: Deformación y conformado de chapa metálica.
*   **`06CADCIN.py`**: Relaciones de transmisión y cinemática de cadenas.

### 3. 🐍 [Python](file:///c:/Users/sousi/OneDrive/Documents/GitHub/Dise-o-por-fabricacion-mecanica-/Curso_Fabricacion_Mecanica/Python/) - Scripts de Procesos y Proyectos
Algoritmos y programas más complejos estructurados en varias subcarpetas:
*   **`Proyectos/Soporte_Moto/`**: Cálculos analíticos (`calculos_soporte.py`) y de tiempos y costes de mecanizado (`calculos_tiempos.py`) para el diseño del **Soporte Expositor de Motos con Mordaza Hidráulica**. *Los modelos 3D y planos CAD en SolidWorks están ubicados en tu otro repositorio: `DEFAME/Proyecto D`*.
*   **`Procesos_Fabricacion/`**: Calculadoras avanzadas interactivas de mecanizado (`calculadora_mecanizado.py`) para torneado, taladrado y fresado (cálculo de potencias, RPM, velocidades de corte, avance y par), y scripts independientes para conformado de chapa (`calculo_doblado.py`, `calculo_embuticion.py`, `calculo_fuerzas_corte.py`, `calculo_longitud_desarrollada.py`), además de cálculo de bobinas de chapa (`calculo_bobina.py`).
*   **`SmartOrganizer/`**: Herramienta gráfica basada en `customtkinter` (`pdf_organizer.py`) que usa una IA local (Ollama con modelo `llama3`) para clasificar, ordenar y mover archivos PDF automáticamente de una carpeta origen a una de destino, leyendo y analizando su contenido.
*   **`Ejercicios/`**: Ejercicios introductorios sobre lógica en Python y costes de producción.
*   **`Utilidades/`**: Script independiente para calcular días de vacaciones (`calcular_vacaciones.py`).

### 4. 🧠 [ADPV](file:///c:/Users/sousi/OneDrive/Documents/GitHub/Dise-o-por-fabricacion-mecanica-/Curso_Fabricacion_Mecanica/ADPV/) - Asistente de PDFs RAG
Sistema RAG (Retrieval-Augmented Generation) local para indexar y consultar documentos PDF de estudio:
*   **`ingest.py`**: Carga archivos PDF desde una carpeta `data/`, los fragmenta y genera una base de datos vectorial local en ChromaDB utilizando embeddings de HuggingFace (`paraphrase-multilingual-MiniLM-L12-v2`).
*   **`chat.py`**: Permite hacer preguntas en lenguaje natural sobre los apuntes del curso y obtener respuestas precisas basadas en los PDFs indexados.

### 5. 🚥 [PLC](file:///c:/Users/sousi/OneDrive/Documents/GitHub/Dise-o-por-fabricacion-mecanica-/Curso_Fabricacion_Mecanica/PLC/) - Automatización
*   **`Ejercicio_Puerta_Garage.md`**: Enunciado, diseño y lógica de programación en Ladder para controlar una puerta de garaje automatizada equipada con sensores de seguridad, fotocélulas, finales de carrera y señalización luminosa.

---

## 🛠️ Requisitos de Ejecución
La mayoría de los scripts en `Python/` y `ADPV/` requieren ciertas librerías de Python. Puedes instalar las dependencias básicas ejecutando:
```bash
pip install -r Python/SmartOrganizer/requirements.txt
# O bien para el asistente RAG:
pip install -r ADPV/requirements.txt
```
Además:
*   Para **SmartOrganizer**: Requiere que [Ollama](https://ollama.com/) esté instalado y ejecutándose en segundo plano con el modelo `llama3`.
*   Para **ADPV**: Requiere la suite de `langchain`, `chromadb` y `sentence-transformers` instalada localmente.
