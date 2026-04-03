"""
ECUACIONES UTILIZADAS (Tiempos de máquina):
- RPM: N = (1000 * Vc) / (PI * D)
- T. Cilindrado: Tc = (L + c) / (a * N)
- T. Refrentado: Tr = Radio / (a * N)
- T. Fresado: Tc = (L + c) / (az * z * N)
- T. Taladrado: Tc = (B + D_broca/3) / (a * N)
- T. Rectificado Cilíndrico: Tc = (L * i) / (nw * a)
"""
import math

def pedir(msg):
    while True:
        try:
            return float(input(msg))
        except:
            print("Error: numero invalido")

print("1:RPM    2:Cilin  3:Refr")
print("4:Fres   5:Talad  6:Rectif")
opc = input("Opcion (1-6): ")

if opc == '1':
    Vc = pedir("Vc (m/min): ")
    D = pedir("Diam (mm): ")
    if D > 0:
        print("N:", round((1000 * Vc) / (math.pi * D), 2), "RPM")
elif opc == '2':
    L = pedir("L (mm): ")
    c = pedir("c (mm): ")
    a = pedir("a (mm/rev): ")
    N = pedir("N (RPM): ")
    if a * N > 0:
        print("Tc:", round((L+c)/(a*N), 4), "min")
elif opc == '3':
    R = pedir("Radio (mm): ")
    a = pedir("a (mm/rev): ")
    N = pedir("N (RPM): ")
    if a * N > 0:
        print("Tr:", round(R/(a*N), 4), "min")
elif opc == '4':
    L = pedir("L (mm): ")
    c = pedir("c (mm): ")
    az = pedir("az (mm/diente): ")
    z = pedir("z (dientes): ")
    N = pedir("N (RPM): ")
    denom = az * z * N
    if denom > 0:
        print("Tc:", round((L+c)/denom, 4), "min")
elif opc == '5':
    B = pedir("Espesor B(mm): ")
    D_br = pedir("Diam broca(mm): ")
    a = pedir("a (mm/rev): ")
    N = pedir("N (RPM): ")
    if a * N > 0:
        print("Tc:", round((B+(D_br/3))/(a*N), 4), "min")
elif opc == '6':
    print("--- RECTIFICADO CILINDRICO ---")
    L = pedir("Longitud mesa L (mm): ")
    i = pedir("Pasadas i: ")
    nw = pedir("RPM pieza nw: ")
    a = pedir("Avance long a (mm/rev): ")
    
    if nw * a > 0:
        print("Tc:", round((L * i) / (nw * a), 4), "min")
    else:
        print("RPM o avance no deben ser 0")
else:
    print("Opcion invalida")
