import math

def calcular_diametro_cilindro():
    """Calcula el diámetro del pistón de un cilindro hidráulico."""
    print("--- Cálculo de Diámetro de Pistón (Ejercicio 2.18) ---")
    
    while True:
        try:
            # 1. Solicitar masa (Carga)
            masa_input = input("\nIntroduce la carga (masa) en kg (o 'q' para salir): ")
            if masa_input.lower() == 'q':
                break
            masa = float(masa_input)
            
            # 2. Solicitar presión
            presion_bar = float(input("Introduce la presión en bar: "))
            
            # Paso 1: Hallar la fuerza (F = m * g)
            g = 9.8  # Aceleración de la gravedad (m/s^2)
            fuerza = masa * g
            print(f"\n1. Fuerza (F): {fuerza:.2f} N")
            
            # Paso 2: Convertir la presión a Pascales (Pa)
            # 1 bar = 100,000 Pa = 10^5 Pa
            presion_pa = presion_bar * 100000
            print(f"2. Presión (p): {presion_pa:.0f} Pa")
            
            # Paso 3: Calcular el área (A = F / p)
            area = fuerza / presion_pa
            print(f"3. Área requerida (A): {area:.6f} m²")
            
            # Paso 4: Despejar el diámetro (d = sqrt(4 * A / pi))
            diametro_m = math.sqrt((4 * area) / math.pi)
            diametro_mm = diametro_m * 1000
            
            print(f"4. Diámetro calculado (d): {diametro_m:.5f} m")
            print(f"   => Diámetro en milímetros: {diametro_mm:.2f} mm")
            
        except ValueError:
            print("Error: Por favor, introduce valores numéricos válidos.")
        except ZeroDivisionError:
            print("Error: La presión no puede ser 0.")

if __name__ == "__main__":
    calcular_diametro_cilindro()
