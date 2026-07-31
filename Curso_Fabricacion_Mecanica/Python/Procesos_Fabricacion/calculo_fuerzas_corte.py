def main():
    print("--- CÁLCULO DE FUERZAS DE CORTE (TROQ1) ---")
    
    try:
        # --- Datos ---
        print("\nIngrese los datos:")
        Kc = float(input("Resistencia al corte (Kc) [ej. 105]: "))
        e = float(input("Espesor de la chapa (e) [ej. 2]: "))
        Pe = float(input("Perímetro exterior (Pe) [ej. 142.83]: "))
        Pi = float(input("Perímetro interior (Pi) [ej. 60]: "))

        print(f"\nDatos ingresados:")
        print(f"Kc = {Kc}")
        print(f"e = {e}")
        print(f"P_ext = {Pe}")
        print(f"P_int = {Pi}")

        # --- 1. F. Corte ---
        Fce = Pe * e * Kc
        Fci = Pi * e * Kc
        Fct = Fce + Fci

        print("\n--- 1. Fuerzas de Corte ---")
        print(f"Fc_ext: {round(Fce, 2)} kg")
        print(f"Fc_int: {round(Fci, 2)} kg")
        print(f"Fc_TOT: {round(Fct, 2)} kg")

        input("\nPresione Enter para continuar...")

        # --- 2. F. Expulsion ---
        # Nota: En el original era Fexp = Fct * 1.5 (quizás error de tipeo en original? suele ser un % de Fct, o Fct + margen?)
        # Asumiendo literal del original: Fexp = Fct * 1.5
        # En muchos manuales F_expulsion es un 10-20% de F_corte, aqui multiplica por 1.5. Respetamos el script original.
        Fexp = Fct * 1.5
        print("\n--- 2. Fuerza de Expulsión ---")
        print(f"Fexp: {round(Fexp, 2)} kg")

        # --- 3. F. Extraccion ---
        Fext_e = Fce * 0.04
        Fext_i = Fci * 0.07
        Fext_t = Fext_e + Fext_i
        print("\n--- 3. Fuerza de Extracción ---")
        print(f"Fext_e: {round(Fext_e, 2)} kg")
        print(f"Fext_i: {round(Fext_i, 2)} kg")
        print(f"Fext_TOT: {round(Fext_t, 2)} kg")

        # --- 4. F. Rozamiento ---
        Froz = Fct * 1.2
        print("\n--- 4. Fuerza de Rozamiento ---")
        print(f"Froz: {round(Froz, 2)} kg")

        input("\nPresione Enter para ver Resumen en Toneladas...")

        # --- Resumen Tons ---
        print("\n--- Resumen en Toneladas ---")
        print(f"Fc: {round(Fct/1000, 2)} T")
        print(f"Fexp: {round(Fexp/1000, 2)} T")
        print(f"Fext: {round(Fext_t/1000, 2)} T")
        print(f"Froz: {round(Froz/1000, 2)} T")

    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
