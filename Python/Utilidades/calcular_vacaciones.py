def calcular_dias_vacaciones(dias_cotizados):
    """
    Calcula los días naturales de vacaciones correspondientes en España.
    Por lo general, corresponden 30 días naturales por cada año (365 días) trabajado.
    """
    # Constantes
    DIAS_ANO = 365
    VACACIONES_ANUALES = 30
    
    # Calculo
    proporcion_diaria = VACACIONES_ANUALES / DIAS_ANO
    dias_vacaciones = dias_cotizados * proporcion_diaria
    
    return round(dias_vacaciones, 2)

if __name__ == "__main__":
    print("--- Calculadora de Vacaciones en España ---")
    try:
        dias = int(input("Introduce el número de días cotizados: "))
        if dias < 0:
            print("El número de días no puede ser negativo.")
        else:
            vacaciones = calcular_dias_vacaciones(dias)
            print(f"\nPor {dias} días cotizados, te corresponden aproximadamente {vacaciones} días naturales de vacaciones.")
            print("Nota: El convenio colectivo puede mejorar estos días.")
    except ValueError:
        print("Error: Por favor, introduce un número entero válido.")
