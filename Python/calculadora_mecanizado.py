import math
import sys

def pedir_numero(mensaje):
    """
    Solicita un número al usuario iterando hasta que introduzca un valor numérico válido.
    Evita que el programa falle si se introduce texto.
    """
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: Por favor, introduzca un valor numérico válido.")

def tolerancias_y_ajustes():
    """
    Menú y cálculos para Tolerancias y Ajustes (Sistema ISO)
    """
    print("\n--- 1. CÁLCULO DE TOLERANCIAS Y AJUSTES ---")
    print("a) Diámetro medio y Unidad de tolerancia")
    print("b) Juego y Aprieto (Máximos y Mínimos)")
    opcion = input("Elige una opción (a/b): ").strip().lower()

    if opcion == 'a':
        d_min = pedir_numero("Introduce el diámetro mínimo del grupo (mm): ")
        d_max = pedir_numero("Introduce el diámetro máximo del grupo (mm): ")
        
        if d_min < 0 or d_max < 0:
            print("Los diámetros deben ser positivos.")
            return

        # Diámetro medio: D = raiz_cuadrada(D_min * D_max)
        D = math.sqrt(d_min * d_max)

        # Unidad de tolerancia: i = 0.45 * raiz_cubica(D) + 0.001 * D
        i = 0.45 * (D ** (1/3)) + 0.001 * D
        
        print("\nResultados:")
        print(f"Diámetro medio (D): {D:.4f} mm")
        print(f"Unidad de tolerancia (i): {i:.4f} μm (micras)")
        
    elif opcion == 'b':
        D_max_agujero = pedir_numero("Introduce el diámetro máximo del agujero (mm): ")
        D_min_agujero = pedir_numero("Introduce el diámetro mínimo del agujero (mm): ")
        d_max_eje = pedir_numero("Introduce el diámetro máximo del eje (mm): ")
        d_min_eje = pedir_numero("Introduce el diámetro mínimo del eje (mm): ")
        
        # Fórmulas de Juegos y Aprietos
        J_max = D_max_agujero - d_min_eje
        J_min = D_min_agujero - d_max_eje
        A_max = d_max_eje - D_min_agujero
        A_min = d_min_eje - D_max_agujero
        
        print("\nResultados:")
        print(f"Juego Máximo (J_max): {J_max:.4f} mm")
        print(f"Juego Mínimo (J_min): {J_min:.4f} mm")
        print(f"Aprieto Máximo (A_max): {A_max:.4f} mm")
        print(f"Aprieto Mínimo (A_min): {A_min:.4f} mm")
    else:
        print("Opción no válida.")


def tiempos_y_velocidades():
    """
    Menú y cálculos para Tiempos de máquina y Velocidades (Torneado, Fresado, Taladrado)
    """
    print("\n--- 2. CÁLCULO DE TIEMPOS DE MÁQUINA Y VELOCIDADES ---")
    print("a) Revoluciones por minuto (N)")
    print("b) Tiempo de Torneado (Cilindrado)")
    print("c) Tiempo de Torneado (Refrentado)")
    print("d) Tiempo de Fresado")
    print("e) Tiempo de Taladrado")
    
    opcion = input("Elige una opción (a/b/c/d/e): ").strip().lower()
    
    if opcion == 'a':
        Vc = pedir_numero("Introduce la velocidad de corte (V_c) (m/min): ")
        Diametro = pedir_numero("Introduce el diámetro (mm): ")
        if Diametro == 0:
            print("El diámetro no puede ser 0.")
            return
            
        # N = (1000 * V_c) / (PI * Diametro)
        N = (1000 * Vc) / (math.pi * Diametro)
        print(f"\nResultados:\nRevoluciones por minuto (N): {N:.2f} RPM")
        
    elif opcion == 'b':
        L = pedir_numero("Introduce la longitud a mecanizar (L) (mm): ")
        c = pedir_numero("Introduce la longitud de entrada/salida (c) (mm): ")
        a = pedir_numero("Introduce el avance por vuelta (a) (mm/rev): ")
        N = pedir_numero("Introduce las revoluciones por minuto (N) (RPM): ")
        if a * N == 0:
            print("Existen valores que provocarían división por 0. Comprueba avance y RPM.")
            return
            
        # Tc = (L + c) / (a * N)
        Tc = (L + c) / (a * N)
        print(f"\nResultados:\nTiempo de Torneado de Cilindrado (Tc): {Tc:.4f} minutos")
        
    elif opcion == 'c':
        R = pedir_numero("Introduce el radio de la pieza (mm): ")
        a = pedir_numero("Introduce el avance por vuelta (a) (mm/rev): ")
        N = pedir_numero("Introduce las revoluciones por minuto (N) (RPM): ")
        if a * N == 0:
            print("Existen valores que provocarían división por 0. Comprueba avance y RPM.")
            return
            
        # Tr = Radio_pieza / (a * N)
        Tr = R / (a * N)
        print(f"\nResultados:\nTiempo de Torneado de Refrentado (Tr): {Tr:.4f} minutos")
        
    elif opcion == 'd':
        L = pedir_numero("Introduce la longitud a fresar (L) (mm): ")
        c = pedir_numero("Introduce la longitud de entrada/salida (c) (mm): ")
        az = pedir_numero("Introduce el avance por diente (a_z) (mm/diente): ")
        z = pedir_numero("Introduce el número de dientes de la fresa (z): ")
        N = pedir_numero("Introduce las revoluciones por minuto (N) (RPM): ")
        if az * z * N == 0:
            print("Existen valores que provocarían división por 0.")
            return
            
        # Tc = (L + c) / (a_z * z * N)
        Tc = (L + c) / (az * z * N)
        print(f"\nResultados:\nTiempo de Fresado (Tc): {Tc:.4f} minutos")
        
    elif opcion == 'e':
        B = pedir_numero("Introduce el espesor de la pieza (B) (mm): ")
        Diam_broca = pedir_numero("Introduce el diámetro de la broca (mm): ")
        a = pedir_numero("Introduce el avance por vuelta (a) (mm/rev): ")
        N = pedir_numero("Introduce las revoluciones por minuto (N) (RPM): ")
        if a * N == 0:
            print("Existen valores que provocarían división por 0.")
            return
            
        # Tc = (B + (Diametro_broca / 3)) / (a * N)
        Tc = (B + (Diam_broca / 3)) / (a * N)
        print(f"\nResultados:\nTiempo de Taladrado (Tc): {Tc:.4f} minutos")
        
    else:
        print("Opción no válida.")

def calculos_conos():
    """
    Cálculos geométricos de conicidad, inclinación y ángulo
    """
    print("\n--- 3. CÁLCULOS GEOMÉTRICOS DE CONOS ---")
    D_mayor = pedir_numero("Introduce el diámetro mayor (D) (mm): ")
    d_menor = pedir_numero("Introduce el diámetro menor (d) (mm): ")
    Longitud = pedir_numero("Introduce la longitud del cono (mm): ")
    
    if Longitud == 0:
        print("La longitud no puede ser 0.")
        return
        
    # C = (D_mayor - d_menor) / Longitud
    C = (D_mayor - d_menor) / Longitud
    
    # i = (D_mayor - d_menor) / (2 * Longitud)
    i = (D_mayor - d_menor) / (2 * Longitud)
    
    # alpha = arco_tangente( (D_mayor - d_menor) / (2 * Longitud) )
    alpha_rad = math.atan(i)
    alpha_deg = math.degrees(alpha_rad)
    
    print("\nResultados:")
    print(f"Conicidad (C): {C:.4f} (adimensional)")
    print(f"Inclinación (i): {i:.4f} (adimensional)")
    print(f"Ángulo del cono (α): {alpha_deg:.4f} grados ({alpha_rad:.4f} radianes)")

def engranajes_rectos():
    """
    Cálculo de engranajes rectos
    """
    print("\n--- 4. ENGRANAJES RECTOS ---")
    print("a) Dimensiones de un engranaje (d, de, di)")
    print("b) Distancia entre centros (L)")
    opcion = input("Elige una opción (a/b): ").strip().lower()

    if opcion == 'a':
        Modulo = pedir_numero("Introduce el Módulo (mm): ")
        Z = pedir_numero("Introduce el número de dientes (Z): ")
        
        # Fórmulas
        d = Modulo * Z
        d_e = d + (2 * Modulo)
        d_i = d - (2.5 * Modulo)
        
        print("\nResultados:")
        print(f"Diámetro primitivo (d): {d:.4f} mm")
        print(f"Diámetro exterior (d_e): {d_e:.4f} mm")
        print(f"Diámetro interior (d_i): {d_i:.4f} mm")
        
    elif opcion == 'b':
        D_rueda = pedir_numero("Introduce el diámetro primitivo de la rueda (mm): ")
        d_pinon = pedir_numero("Introduce el diámetro primitivo del piñón (mm): ")
        
        # L = (D_rueda + d_piñon) / 2
        L = (D_rueda + d_pinon) / 2
        print(f"\nResultados:\nDistancia entre centros (L): {L:.4f} mm")
    else:
        print("Opción no válida.")

def conformado_chapa():
    """
    Cálculo de diámetro de disco para embutición de vaso cilíndrico
    """
    print("\n--- 5. CONFORMADO DE CHAPA (EMBUTICIÓN) ---")
    d = pedir_numero("Introduce el diámetro de la pieza final (d) (mm): ")
    h = pedir_numero("Introduce la altura de la pieza (h) (mm): ")
    
    if d < 0 or h < 0:
        print("El diámetro y la altura deben ser positivos.")
        return
        
    # D = raiz_cuadrada( d^2 + 4 * d * h )
    D = math.sqrt(d**2 + 4 * d * h)
    
    print("\nResultados:")
    print(f"Diámetro del disco o formato inicial (D): {D:.4f} mm")

def main():
    """
    Controla el menú principal de la aplicación.
    """
    while True:
        print("\n" + "="*55)
        print(" CALCULADORA DE INGENIERÍA DE FABRICACIÓN Y MECANIZADO ")
        print("="*55)
        print("1. Cálculo de tolerancias y ajustes (Sistema ISO)")
        print("2. Cálculo de tiempos de máquina y velocidades")
        print("3. Cálculos geométricos de conos")
        print("4. Engranajes rectos")
        print("5. Conformado de chapa (Embutición)")
        print("0. Salir")
        print("="*55)
        
        opcion = input("Elige el número de la operación que deseas realizar: ").strip()
        
        if opcion == '1':
            tolerancias_y_ajustes()
        elif opcion == '2':
            tiempos_y_velocidades()
        elif opcion == '3':
            calculos_conos()
        elif opcion == '4':
            engranajes_rectos()
        elif opcion == '5':
            conformado_chapa()
        elif opcion == '0':
            print("Saliendo de la calculadora. ¡Hasta pronto!")
            sys.exit(0)
        else:
            print("Opción no válida, por favor elige un número del menú principal.")

if __name__ == "__main__":
    main()
