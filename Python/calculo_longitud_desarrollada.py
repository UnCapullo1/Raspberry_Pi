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
        num_segmentos = int(input("\n¿Cuántos tramos rectos tiene la pieza? [ej. 6]: "))
        
        segmentos = []
        suma_segmentos = 0
        
        print(f"Ingrese la longitud de los {num_segmentos} tramos:")
        for i in range(1, num_segmentos + 1):
            seg = float(input(f"  Tramo {i}: "))
            segmentos.append(seg)
            suma_segmentos += seg

        print(f"\nLongitud total de tramos rectos: {suma_segmentos}")

        input("\nPresione Enter para calcular longitud total...")

        # --- Longitud Total ---
        # Asumiremos que el número de curvas es (número de tramos - 1) si es una linea continua abierta
        # O el usuario podría querer especificarlo.
        # En el ejemplo original: 6 tramos, 5 curvas. Coincide con n-1.
        num_curvas = num_segmentos - 1
        # Si fuese 1 solo tramo, 0 curvas.
        if num_curvas < 0: num_curvas = 0
        
        print(f"Calculando con {num_curvas} curvas de 90°...")

        L = suma_segmentos + (num_curvas * AB)
        
        print("\n--- Resumen ---")
        print(f"Longitud Total (L) = {round(L, 2)} mm")

    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
