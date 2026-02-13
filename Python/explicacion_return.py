# Diferencia entre PRINT y RETURN

# Caso 1: Función con PRINT (Solo muestra, no devuelve nada)
def sumar_con_print(a, b):
    resultado = a + b
    print(f"Dentro de la función (print): {resultado}")

# Caso 2: Función con RETURN (Devuelve el valor para usarlo después)
def sumar_con_return(a, b):
    resultado = a + b
    return resultado

# --- PRUEBA ---

print("--- Usando PRINT ---")
valor1 = sumar_con_print(5, 3)
# ¿Qué vale valor1?
print(f"Valor guardado: {valor1}") # Imprimirá 'None' (Nada) porque la función no devolvió nada.

print("\n--- Usando RETURN ---")
valor2 = sumar_con_return(5, 3)
# ¿Qué vale valor2?
print(f"Valor guardado: {valor2}") # Imprimirá '8'.

# ¿Por qué es útil return?
# Porque permite SEGUIR operando con el resultado.
# Ejemplo: Queremos el doble de la suma.
doble = valor2 * 2
print(f"\nEl doble de la suma (8 * 2) es: {doble}")

# Con valor1 esto daría error, porque no puedes multiplicar 'Nada' por 2.
