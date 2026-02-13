import math

def main():
    print("--- CÁLCULO DE LONGITUD DESARROLLADA (TROQ4) ---")

    try:
        # --- Datos ---
        print("\nIngrese los datos generales:")
        e = float(input("Espesor de la chapa (e) [ej. 2]: "))
        r = float(input("Radio interior (r) [ej. 3]: "))

        print(f"\nDatos ingresados:")
        print(f"e = {e}")
        print(f"r = {r}")

        # --- Fibra Neutra ---
        R = r + (e/2)
        print(f"Radio Neutro (R) = {R}")

        # --- Longitud Arco ---
        # Asumiendo 90 grados (1/4 de circulo) por defecto como en el original
        AB = (2 * math.pi * R) / 4
        print(f"Longitud Arco 90° (AB) = {round(AB, 2)}")

        input("\nPresione Enter para ingresar los segmentos rectos...")

        # --- Segmentos Rectos ---
        print("\nIngrese las longitudes de los segmentos rectos:")
        
        # En el original eran calculos fijos: sa=50-5, etc.
        # Aquí pediremos el valor final del segmento o la operación si el usuario prefiere calcularlo antes.
        # Asumiremos que el usuario mete el valor neto del segmento recto.
        sa = float(input("Segmento a [ej. 45]: "))
        sb = float(input("Segmento b [ej. 90]: "))
        sc = float(input("Segmento c [ej. 115]: "))
        sd = float(input("Segmento d [ej. 90]: "))
        se = float(input("Segmento e [ej. 40]: "))
        sf = float(input("Segmento f [ej. 45]: "))

        print(f"\nSegmentos ingresados:")
        print(f"a = {sa}")
        print(f"b = {sb}")
        print(f"c = {sc}")
        print(f"d = {sd}")
        print(f"e = {se}")
        print(f"f = {sf}")

        input("\nPresione Enter para calcular longitud total...")

        # --- Longitud Total ---
        # El original tenía 5 curvas (5 * AB) mas los 6 segmentos
        L = sa + sb + sc + sd + se + sf + (5 * AB)
        
        print("\n--- Resumen ---")
        print(f"Longitud Total (L) = {round(L, 2)} mm")

    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
