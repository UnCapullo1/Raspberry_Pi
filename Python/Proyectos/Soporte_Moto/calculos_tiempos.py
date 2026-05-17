import math

def solicitar_dato(mensaje, valor_por_defecto):
    """Muestra un mensaje al usuario pidiendo un dato y ofrece un valor por defecto."""
    entrada = input(f"{mensaje} [Por defecto: {valor_por_defecto}]: ")
    if entrada.strip() == "":
        return float(valor_por_defecto)
    try:
        return float(entrada.replace(',', '.'))
    except ValueError:
        print(f"  -> Valor no válido. Se usará el valor por defecto: {valor_por_defecto}")
        return float(valor_por_defecto)

def menu():
    while True:
        print("\n" + "="*60)
        print(" CÁLCULO DE TIEMPOS DE FABRICACIÓN EN TALLER (SOPORTE)")
        print("="*60)
        print("1: Tiempo de Soldadura")
        print("2: Tiempo de Fresado")
        print("3: Tiempo de Torneado")
        print("4: Tiempo de Corte (Sierra con dientes, Láser, Cizalla)")
        print("0: Salir")
        
        op = input("\nSelecciona una opción (0-4): ")
        
        if op == "1":
            print("\n--- 1. TIEMPO DE SOLDADURA ---")
            L = solicitar_dato("Longitud total de los cordones a soldar (mm)", 400.0)
            v_avance = solicitar_dato("Velocidad de avance de soldadura (mm/min, ej: MIG ~350)", 350.0)
            eficiencia = solicitar_dato("Factor de eficiencia del soldador (0.1 a 1.0)", 0.6)
            
            t_arco = L / v_avance
            t_total = t_arco / eficiencia
            print("-" * 40)
            print(f"Tiempo de arco encendido (neto): {t_arco:.2f} min")
            print(f"Tiempo total estimado en taller (preparación + soldadura): {t_total:.2f} min")
            
        elif op == "2":
            print("\n--- 2. TIEMPO DE FRESADO ---")
            L = solicitar_dato("Longitud a fresar (mm)", 150.0)
            D = solicitar_dato("Diámetro de la fresa (mm)", 50.0)
            Z = solicitar_dato("Número de dientes de la fresa", 4.0)
            Vc = solicitar_dato("Velocidad de corte Vc (m/min)", 100.0)
            fz = solicitar_dato("Avance por diente fz (mm/diente)", 0.1)
            pasadas = solicitar_dato("Número de pasadas", 1.0)
            
            N = (Vc * 1000) / (math.pi * D)
            Vf = fz * Z * N
            L_total = L + D
            t_corte = (L_total / Vf) * pasadas
            
            print("-" * 40)
            print(f"Velocidad de giro (N): {N:.0f} RPM")
            print(f"Avance de mesa (Vf): {Vf:.2f} mm/min")
            print(f"Tiempo total de fresado: {t_corte:.2f} min")
            
        elif op == "3":
            print("\n--- 3. TIEMPO DE TORNEADO ---")
            L = solicitar_dato("Longitud a tornear en el eje Z (mm)", 100.0)
            D = solicitar_dato("Diámetro de la pieza a mecanizar (mm)", 40.0)
            Vc = solicitar_dato("Velocidad de corte Vc (m/min)", 150.0)
            f = solicitar_dato("Avance por revolución f (mm/rev)", 0.2)
            pasadas = solicitar_dato("Número de pasadas", 2.0)
            
            N = (Vc * 1000) / (math.pi * D)
            t_corte = (L / (f * N)) * pasadas
            
            print("-" * 40)
            print(f"Velocidad de giro (N): {N:.0f} RPM")
            print(f"Tiempo total de torneado: {t_corte:.2f} min")
            
        elif op == "4":
            print("\n--- 4. TIEMPO DE CORTE ---")
            tipo_corte = input("¿Tipo de corte? (1: Sierra de disco/cinta, 2: Láser/Plasma/Cizalla) [1]: ")
            if tipo_corte.strip() != "2":
                print("\n--- CORTE POR SIERRA (Parámetros de herramienta dentada) ---")
                L = solicitar_dato("Longitud a cortar o penetración de la sierra (mm)", 40.0)
                D = solicitar_dato("Diámetro del disco o rodillo (mm)", 250.0)
                Z = solicitar_dato("Número de dientes del disco/sierra", 60.0)
                Vc = solicitar_dato("Velocidad de corte Vc (m/min)", 30.0)
                fz = solicitar_dato("Avance por diente fz (mm/diente)", 0.05)
                
                N = (Vc * 1000) / (math.pi * D)
                Vf = fz * Z * N
                t_corte = L / Vf if Vf > 0 else 0
                
                print("-" * 40)
                print(f"Velocidad de giro (N): {N:.0f} RPM")
                print(f"Velocidad de avance (Vf): {Vf:.2f} mm/min")
            else:
                print("\n--- CORTE LÁSER / PLASMA / CIZALLA ---")
                L = solicitar_dato("Longitud total de corte (mm, ej: Perímetro = 5900)", 5900.0)
                v_corte = solicitar_dato("Velocidad de avance de corte (mm/min)", 1200.0)
                t_corte = L / v_corte
                
            eficiencia = solicitar_dato("Factor de eficiencia/preparación en taller (0.1 a 1.0)", 0.8)
            t_total = t_corte / eficiencia
            
            print("-" * 40)
            print(f"Tiempo de corte neto (máquina en marcha): {t_corte:.2f} min")
            print(f"Tiempo total en taller (incluyendo cambio/preparación): {t_total:.2f} min")
            
        elif op == "0":
            print("Saliendo del programa de cálculos...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nPrograma cancelado por el usuario.")
