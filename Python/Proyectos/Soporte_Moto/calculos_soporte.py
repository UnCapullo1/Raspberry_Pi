import math
import sys

def solicitar_dato(mensaje, valor_por_defecto):
    """Muestra un mensaje al usuario pidiendo un dato y ofrece un valor por defecto."""
    entrada = input(f"{mensaje} [Por defecto: {valor_por_defecto}]: ")
    if entrada.strip() == "":
        return valor_por_defecto
    try:
        # Permitir comas en vez de puntos para decimales
        return float(entrada.replace(',', '.'))
    except ValueError:
        print(f"  -> Valor no válido. Se usará el valor por defecto: {valor_por_defecto}")
        return valor_por_defecto

def calcular_soporte_moto():
    print("="*80)
    print(" CÁLCULOS DE INGENIERÍA INTERACTIVOS: SOPORTE EXPOSITOR PARA MOTOS")
    print("="*80)
    print("Por favor, introduce los valores solicitados para adaptar los cálculos a tu diseño.")
    print("Si quieres mantener el valor sugerido, simplemente pulsa ENTER.\n")
    
    # --- ENTRADA DE DATOS ---
    print("--- DATOS GENERALES ---")
    masa_moto = solicitar_dato("Masa máxima de la moto (kg)", 300.0)
    g = 9.81
    peso_moto = masa_moto * g
    
    print("\n--- 1. PARÁMETROS DEL ELEVADOR DE TIJERA ---")
    L_brazo = solicitar_dato("Longitud del brazo de la tijera (mm)", 1000.0)
    H_min = solicitar_dato("Altura mínima del elevador plegado (mm)", 150.0)
    H_max = solicitar_dato("Altura máxima del elevador desplegado (mm)", 400.0)
    
    print("\n--- 2. PARÁMETROS DE LA ESTRUCTURA TUBULAR ---")
    b = solicitar_dato("Ancho del tubo cuadrado/rectangular (mm)", 40.0)
    h_tubo = solicitar_dato("Alto del tubo (mm)", 40.0)
    t_tubo = solicitar_dato("Espesor del tubo (mm)", 2.0)
    L_perfil = solicitar_dato("Longitud del larguero principal (distancia entre apoyos en mm)", 2200.0)
    limite_elastico = solicitar_dato("Límite elástico del acero estructural (MPa, ej: S235 -> 235)", 235.0)
    
    print("\n--- 3. PARÁMETROS DE LA CHAPA BASE Y ESTAMPACIÓN ---")
    largo_chapa = solicitar_dato("Largo de la chapa a cortar/estampar (mm)", 2200.0)
    ancho_chapa = solicitar_dato("Ancho de la chapa (mm)", 750.0)
    espesor_chapa = solicitar_dato("Espesor de la chapa lagrimada (mm)", 2.0)
    resistencia_corte = solicitar_dato("Resistencia a cizalladura del acero (MPa)", 320.0)
    
    # --- EJECUCIÓN DE CÁLCULOS ---
    print("\n" + "="*80)
    print(" RESULTADOS DE LOS CÁLCULOS")
    print("="*80)
    
    resultados = []
    
    # 1. Elevador de tijera
    # Protección matemática si la altura mínima es mayor que la longitud del brazo
    if H_min >= L_brazo:
        print("Error: La altura mínima no puede ser igual o mayor que la longitud del brazo de tijera.")
        theta_min = math.asin(1)
    else:
        theta_min = math.asin(H_min / L_brazo)
        
    fuerza_cilindro_tijera = peso_moto / math.tan(theta_min)
    
    print(f"\n[ELEVADOR DE TIJERA]")
    print(f" - Ángulo mínimo de ataque: {math.degrees(theta_min):.2f} grados")
    print(f" - Fuerza de empuje requerida en el cilindro (posición más baja): {fuerza_cilindro_tijera:,.2f} N (aprox. {(fuerza_cilindro_tijera/1000/g):.2f} t)")
    resultados.append({"Elemento": "Cilindro Tijera", "Carga/Fuerza": f"{fuerza_cilindro_tijera:.0f} N", "Tensión/Presión": "N/A", "Estado": "Calculado"})
    
    # 2. Tubería
    E_acero = 210000 # Módulo de Young estándar para acero
    # Cálculo del momento de inercia
    I_x = (b * h_tubo**3 - (b - 2*t_tubo) * (h_tubo - 2*t_tubo)**3) / 12
    W_x = I_x / (h_tubo / 2)
    # Momento flector asumiendo que la carga se reparte entre 2 largueros
    momento_max = ((peso_moto / 2) * L_perfil) / 4
    tension_max = momento_max / W_x
    
    print(f"\n[ESTRUCTURA TUBULAR]")
    print(f" - Momento de inercia (Ix): {I_x:,.2f} mm^4")
    print(f" - Módulo resistente (Wx): {W_x:,.2f} mm^3")
    print(f" - Tensión máxima de flexión teórica: {tension_max:.2f} MPa")
    
    estado_tubo = "Seguro" if tension_max <= limite_elastico else "CRÍTICAMENTE SOBRECARGADO"
    if tension_max > limite_elastico:
        print("   -> ¡CUIDADO! La tensión supera el límite elástico del acero especificado.")
    else:
        print("   -> La tensión está dentro de los límites de seguridad elástica.")
    
    resultados.append({"Elemento": f"Tubo {b}x{h_tubo}x{t_tubo}", "Carga/Fuerza": f"{peso_moto/2:.0f} N", "Tensión/Presión": f"{tension_max:.2f} MPa", "Estado": estado_tubo})
    
    # 3. Estampación y Cizalladura
    perimetro_corte = 2 * (ancho_chapa + largo_chapa)
    fuerza_estampacion_N = perimetro_corte * espesor_chapa * resistencia_corte
    fuerza_estampacion_ton = fuerza_estampacion_N / (g * 1000)
    
    print(f"\n[ESTAMPACIÓN Y CIZALLADURA]")
    print(f" - Perímetro total de corte de la chapa: {perimetro_corte} mm")
    print(f" - Tonelaje requerido en prensa estampadora: {fuerza_estampacion_ton:,.1f} Toneladas métricas")
    
    viabilidad_prensa = "Prensa Industrial" if fuerza_estampacion_ton < 500 else "Prensa Especial (>500t)"
    if fuerza_estampacion_ton <= 500:
        print("   -> Viable para producción en serie con una prensa industrial estándar.")
    else:
        print("   -> Tonelaje muy elevado. Puede requerir maquinaria muy pesada y de alto coste.")
        
    resultados.append({"Elemento": "Prensa Troqueladora", "Carga/Fuerza": f"{fuerza_estampacion_ton:.1f} Ton", "Tensión/Presión": f"{resistencia_corte} MPa", "Estado": viabilidad_prensa})

    # --- TABLA RESUMEN ---
    print("\n" + "="*80)
    print(f"{'TABLA RESUMEN DE ELEMENTOS Y ESFUERZOS':^80}")
    print("="*80)
    print(f"{'Elemento':<25} | {'Carga/Fuerza Soportada':<22} | {'Tensión/Presión':<15} | {'Estado / Viabilidad'}")
    print("-" * 80)
    for res in resultados:
        print(f"{res['Elemento']:<25} | {res['Carga/Fuerza']:<22} | {res['Tensión/Presión']:<15} | {res['Estado']}")
    print("="*80)

if __name__ == "__main__":
    try:
        calcular_soporte_moto()
        print("\nFinalizado con éxito.")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")
