import math

def main():
    print("--- CÁLCULO DE EMBUTICIÓN (TROQ5) ---")

    try:
        # --- Datos ---
        print("\nIngrese los datos:")
        k1 = float(input("Coeficiente k1 [ej. 0.75]: "))
        k2 = float(input("Coeficiente k2 [ej. 0.90]: "))
        df = float(input("Diámetro final (df) [ej. 30]: "))
        hf = float(input("Altura final (hf) [ej. 42]: "))
        
        print(f"\nDatos ingresados:")
        print(f"k1 = {k1}")
        print(f"k2 = {k2}")
        print(f"df = {df}")
        print(f"hf = {hf}")

        # --- D Primitivo ---
        D = math.sqrt(df**2 + 4 * df * hf)
        print(f"\nDiámetro Primitivo (D) = {round(D, 2)}")

        # --- Etapa 1 ---
        num_h = D**2 - df**2
        
        d1 = k1 * D
        print(f"\n--- Etapa 1 ---")
        print(f"d1 = {round(d1, 2)}")
        
        h1 = num_h / (4 * d1)
        print(f"h1 = {round(h1, 2)}")

        input("\nPresione Enter para ver siguientes etapas...")

        # --- Etapas siguientes ---
        # El original itera de 2 a 8.
        # d_prev inicia con d1
        d_prev = d1
        
        print("\n--- Etapas Siguientes ---")
        for i in range(2, 8):
            dn = k2 * d_prev
            hn = num_h / (4 * dn)
            
            print(f"Etapa {i}:")
            print(f"  d{i} = {round(dn, 2)}")
            print(f"  h{i} = {round(hn, 2)}")
            
            d_prev = dn
            
            # Pausa cada 2 etapas (original: if i % 2 != 0 input...)
            # i=2 -> no pausa
            # i=3 -> pausa
            # i=4 -> no pausa
            if i % 2 != 0:
                input("Presione Enter para continuar...")

    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
