def main():
    print("--- CÁLCULO DE FUERZAS DE DOBLADO (TROQ3) ---")

    try:
        # --- Datos ---
        print("\nIngrese los datos:")
        e = float(input("Espesor de la chapa (e) [ej. 2]: "))
        Kd = float(input("Coeficiente de doblado (Kd) [ej. 50]: "))
        b = float(input("Ancho o distancia entre apoyos (b) [ej. 40]: "))

        print(f"\nDatos ingresados:")
        print(f"e = {e}")
        print(f"Kd = {Kd}")
        print(f"b = {b}")

        # --- Doblado en L ---
        # Fd = (b * e * Kd) / 6
        FdL = (b * e * Kd) / 6
        print("\n--- Resultados ---")
        print(f"Doblado en L (Fd): {round(FdL, 2)} kg")

        # --- Doblado en U ---
        # Fd = (b * e * Kd) / 3
        FdU = (b * e * Kd) / 3
        print(f"Doblado en U (Fd): {round(FdU, 2)} kg")

    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
