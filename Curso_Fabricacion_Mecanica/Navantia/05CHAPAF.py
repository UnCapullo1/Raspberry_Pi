"""
ECUACIONES UTILIZADAS (Conformado de chapa):
- Diámetro formato inicial (vaso cilíndrico): D = raiz(d^2 + 4 * d * h)
"""
import math

def pedir(msg):
    while True:
        try:
            return float(input(msg))
        except:
            print("Error: numero invalido")

print("--- EMBUTICION (CHAPA) ---")
d = pedir("D final vaso (mm): ")
h = pedir("Altura h (mm): ")

if d >= 0 and h >= 0:
    D = math.sqrt(d**2 + 4 * d * h)
    print("D disco inic:", round(D, 4), "mm")
else:
    print("Valores deben ser positivos")
