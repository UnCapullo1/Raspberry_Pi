# --- Variables (Datos) ---
largo = 100
ancho = 50
alto = 25
densidad = 8900  # kg/m^3 (Cobre/Bronce aprox)

# --- Función ---
def Dimensiones():
    # 1. Calcular Área y Volumen
    area = largo * ancho
    volumen = largo * ancho * alto  # Esto da mm^3
    
    # 2. Calcular Peso
    # Como la densidad está en kg/m^3 y el volumen en mm^3, hay que convertir.
    # 1 metro = 1000 mm
    # 1 metro cúbico = 1000 * 1000 * 1000 = 1,000,000,000 mm^3
    volumen_metros_cubicos = volumen / 1000000000
    
    peso = volumen_metros_cubicos * densidad
    
    # IMPORTANTE: El 'return' debe estar INDENTADO (dentro de la función)
    return area, volumen, peso

# --- Programa Principal ---
# Llamamos a la función y guardamos lo que devuelve en 3 variables
res_area, res_volumen, res_peso = Dimensiones()

print(f"Area: {res_area} mm^2")
print(f"Volumen: {res_volumen} mm^3")
print(f"Peso estimado: {res_peso} kg")
