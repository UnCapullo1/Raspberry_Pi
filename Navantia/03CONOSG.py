"""
ECUACIONES UTILIZADAS (Conos):
- Inclinación (i) = (D_may - d_men) / (2 * Lc)
- Ángulo (alpha/2) = arctan(i)  [en grados]
- Desplazamiento contrapunto (x) = i * L_total
- Conicidad (C) = (D_may - d_men) / Lc
"""
import math

def pedir(msg):
    while True:
        try:
            return float(input(msg))
        except:
            print("Error: numero")

print("--- METODOS TORNEADO CONO ---")
print("1: Carro orientable (Grados)")
print("2: Desplazamiento contrapunto")
print("3: Aparato copiador (Regla)")
opc = input("Metodo (1/2/3): ")

D_may = pedir("D mayor (mm): ")
d_men = pedir("d menor (mm): ")
Lc = pedir("Longitud del cono (mm): ")

if Lc > 0:
    i = (D_may - d_men) / (2 * Lc)
    alf_rad = math.atan(i)
    alf_deg = alf_rad * (180 / math.pi)

    if opc == '1':
        print("\n--- CARRO ORIENTABLE ---")
        print("Inclinacion a/2:", round(alf_deg, 4), "grados")
    elif opc == '2':
        print("\n--- DESPLAZ. CONTRAPUNTO ---")
        Lt = pedir("Long. total pieza (mm): ")
        x = (D_may - d_men) / (2 * Lc) * Lt
        print("Desplaz. x:", round(x, 4), "mm")
    elif opc == '3':
        print("\n--- APARATO COPIADOR ---")
        C = (D_may - d_men) / Lc
        print("Conicidad (C):", round(C, 4))
        print("Inclinacion a/2:", round(alf_deg, 4), "grados")
    else:
        print("Metodo invalido.")
else:
    print("Longitud no puede ser 0")
