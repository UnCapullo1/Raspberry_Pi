# --- Ejercicio: Calculadora de Costes de Material ---
#
# OBJETIVO:
# 1. Aprender a pedir datos al usuario con 'input()'.
# 2. Usar 'if/elif/else' para tomar decisiones (elegir material).
# 3. Repasar funciones y cálculos matemáticos.

# --- 1. Precios y Densidades (Constantes) ---
# Densidad en kg/m^3
DENSIDAD_ACERO = 7850
DENSIDAD_ALUMINIO = 2700
DENSIDAD_COBRE = 8960

# Precio en €/kg
PRECIO_ACERO = 1.5
PRECIO_ALUMINIO = 4.0
PRECIO_COBRE = 9.5

# --- 2. Función de Cálculo ---
def calcular_peso(largo_mm, ancho_mm, alto_mm, densidad_material):
    """
    Calcula el peso en kg dadas las dimensiones en mm y la densidad en kg/m^3.
    """
    # Calculamos volumen en mm^3
    volumen_mm3 = largo_mm * ancho_mm * alto_mm
    
    # Pasamos a metros cúbicos (1 m^3 = 1,000,000,000 mm^3)
    volumen_m3 = volumen_mm3 / 1_000_000_000
    
    # Calculamos peso
    peso_kg = volumen_m3 * densidad_material
    
    return peso_kg

# --- 3. Programa Principal ---

print("=== CALCULADORA DE COSTES DE MATERIAL ===")
print("Elige un material:")
print("1. Acero")
print("2. Aluminio")
print("3. Cobre")

# Pedimos al usuario que elija (input siempre devuelve texto -> str)
opcion = input("Escribe el número del material (1, 2 o 3): ")

# Pedimos dimensiones (convertimos el texto a número decimal 'float')
print("\n--- Introduce las dimensiones en milímetros (mm) ---")
l = float(input("Largo: "))
a = float(input("Ancho: "))
h = float(input("Alto: "))

# Variables para guardar los datos seleccionados
densidad_elegida = 0
precio_elegido = 0
nombre_material = ""

# --- ESTRUCTURA IF / ELIF / ELSE ---
if opcion == "1":
    nombre_material = "Acero"
    densidad_elegida = DENSIDAD_ACERO
    precio_elegido = PRECIO_ACERO
elif opcion == "2":
    nombre_material = "Aluminio"
    densidad_elegida = DENSIDAD_ALUMINIO
    precio_elegido = PRECIO_ALUMINIO
elif opcion == "3":
    nombre_material = "Cobre"
    densidad_elegida = DENSIDAD_COBRE
    precio_elegido = PRECIO_COBRE
else:
    print("\n[ERROR] Opción no válida. Usaremos Acero por defecto.")
    nombre_material = "Acero (Default)"
    densidad_elegida = DENSIDAD_ACERO
    precio_elegido = PRECIO_ACERO

# --- Cálculos Finales ---
peso_final = calcular_peso(l, a, h, densidad_elegida)
coste_final = peso_final * precio_elegido

# --- Mostrar Resultados ---
print(f"\nResultados para {nombre_material}:")
print(f"Dimensiones: {l}x{a}x{h} mm")
print(f"Peso estimado: {peso_final:.2f} kg")  # :.2f redondea a 2 decimales
print(f"Coste estimado: {coste_final:.2f} €")
