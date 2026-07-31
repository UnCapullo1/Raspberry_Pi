import math

def main():
    print("--- CÁLCULO DE BOBINA (Q2) ---")

    try:
        # --- Datos ---
        print("\nIngrese los datos:")
        N = int(input("Producción Total (N) [ej. 70000]: "))
        e = float(input("Espesor (e) [ej. 1.5]: "))
        rho_input = input("Densidad (rho) [ej. 8.9]: ")
        
        # Manejo de densidad: el original tenia 8.9/1000000
        # Preguntaremos al usuario el valor base (ej 8.9) y aplicaremos la division
        rho = float(rho_input) / 1000000

        print("\nDimensiones de la pieza (según diagrama):")
        # El original calculaba m = 10 + 1.8 = 11.8
        m = float(input("Dimensión m [ej. 11.8]: "))
        # El original calculaba n = 14 + 1.5 = 15.5
        n = float(input("Dimensión n [ej. 15.5]: "))
        
        print(f"\nDatos ingresados:")
        print(f"N = {N}")
        print(f"e = {e}")
        print(f"rho = {float(rho_input)} (usado internamente como {rho})")
        print(f"m = {m}")
        print(f"n = {n}")

        # --- a) Angulo ---
        # alpha = atan(m/n)
        ar = math.atan(m/n)
        ad = math.degrees(ar)
        
        # Conversión a grados, minutos, segundos
        d_deg = int(ad)
        md = (ad - d_deg) * 60
        mm = int(md)
        sd = (md - mm) * 60
        
        print(f"\na) Ángulo de inclinación:")
        print(f"   {d_deg}° {mm}' {round(sd, 2)}''")

        # --- b) Paso ---
        # p = sqrt(m^2 + n^2)
        p = math.sqrt(m**2 + n**2)
        print(f"\nb) Paso:")
        print(f"   {round(p, 2)} mm")

        # --- c) Ancho ---
        print("\nPara el ancho (B), ingrese los radios:")
        rt = float(input("Radio rt [ej. 7]: "))
        rb = float(input("Radio rb [ej. 5]: "))

        # x = rt * sin(alpha)
        x = rt * math.sin(ar)
        xp = rt - x
        
        # beta = 90 - alpha
        br = (math.pi/2) - ar
        
        # y = rb * sin(90-alpha)
        y = rb * math.sin(br)
        yp = rb - y
        
        # a_len = 20 * cos(alpha) + x'  (Original tenia 20 hardcoded)
        # Asumiremos que 20 y 44 eran cotas fijas del problema especifico.
        # Para hacerlo MAS util, podriamos pedir estas cotas, pero el usuario pidio 'funcionando igual'.
        # Mantendre 20 y 44 hardcoded pero lo indicare.
        print("Nota: Usando cotas fijas internas (20 y 44) del problema original.")
        
        a_len = 20 * math.cos(ar) + xp
        
        # b_len = 44 * sin(alpha) + y'
        b_len = 44 * math.sin(ar) + yp
        
        # B = 1.5 + a + b + 1.5 (Original tenia 1.5 hardcoded como margen)
        margen = 1.5
        B = margen + a_len + b_len + margen
        
        print(f"\nc) Ancho de banda (B):")
        print(f"   {round(B, 2)} mm")

        # --- d) Longitud ---
        # L = N * p
        L = N * p / 1000 # Convertir a metros
        print(f"\nd) Longitud Total:")
        print(f"   {round(L, 2)} m")

        # --- e) Peso ---
        # W = Vol * rho = (L_mm * B_mm * e_mm) * rho
        # Ojo: L en formula original usa L (en metros? no, en mm) * 1000?
        # Original: W = L*1000*B*e*rho. 
        # Si L era en metros, L*1000 es mm.
        # Vol = L_mm * B * e.
        # W = Vol * rho
        
        W = (L * 1000) * B * e * rho
        print(f"\ne) Peso Total:")
        print(f"   {round(W, 2)} kg")

    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
