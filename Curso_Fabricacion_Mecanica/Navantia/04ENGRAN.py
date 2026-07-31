"""
ECUACIONES UTILIZADAS (Engranajes):
1. Rectos: d = m*Z | de = d + 2*m | di = d - 2.5*m | Dist. Centros L = (Dr + dp)/2
2. Helicoidales y Dobles: mt = mn/cos(beta) | d = mt*Z | de = d + 2*mn | di = d - 2.5*mn
3. Cónicos (90º): delta1 = arctan(Z1/Z2) | de = m*Z1 | L(generatriz) = de / (2*sin(delta1)) | dae = de + 2*m*cos(delta1)
"""
import math

def pedir(msg):
    while True:
        try:
            return float(input(msg))
        except:
            print("Error: numero invalido")

print("1:Recto      2:Helicoidal")
print("3:Conico     4:Doble Helic.")
tipo = input("Tipo engranaje (1-4): ")

if tipo == '1':
    print("--- RECTO ---")
    print("1: Dimensiones")
    print("2: Distancia centros")
    opc = input("Opcion (1/2): ")

    if opc == '1':
        M = pedir("Modulo (mm): ")
        Z = pedir("Dientes Z: ")
        
        d = M * Z
        de = d + (2 * M)
        di = d - (2.5 * M)
        
        print("d primitivo:", round(d, 4))
        print("d exterior:", round(de, 4))
        print("d interior:", round(di, 4))
    elif opc == '2':
        Dr = pedir("D rueda (mm): ")
        dp = pedir("d pinon (mm): ")
        L = (Dr + dp) / 2
        print("Dist. Centros:", round(L, 4), "mm")
    else:
        print("Opcion invalida")

elif tipo == '2' or tipo == '4':
    if tipo == '2':
        print("--- HELICOIDAL ---")
    else:
        print("--- DOBLE HELICOIDAL ---")
        
    Mn = pedir("Modulo normal (mm): ")
    Z = pedir("Dientes Z: ")
    beta_deg = pedir("Angulo helice (grados): ")
    
    beta_rad = math.radians(beta_deg)
    cos_b = math.cos(beta_rad)
    
    if cos_b != 0:
        Mt = Mn / cos_b
        d = Mt * Z
        de = d + (2 * Mn)
        di = d - (2.5 * Mn)
        print("M aparente:", round(Mt, 4), "mm")
        print("d primitivo:", round(d, 4), "mm")
        print("d exterior:", round(de, 4), "mm")
        print("d interior:", round(di, 4), "mm")
    else:
        print("Angulo invalido (cos=0)")

elif tipo == '3':
    print("--- CONICO (A 90 GRADOS) ---")
    M = pedir("Modulo talon (mm): ")
    Z1 = pedir("Z pinon: ")
    Z2 = pedir("Z rueda: ")
    
    if Z2 != 0:
        delta1_rad = math.atan(Z1 / Z2)
        delta1_deg = math.degrees(delta1_rad)
        de = M * Z1
        sen_d1 = math.sin(delta1_rad)
        
        if sen_d1 != 0:
            L = de / (2 * sen_d1)
            dae = de + 2 * M * math.cos(delta1_rad)
            print("Angulo cono pinon:", round(delta1_deg, 4), "grados")
            print("D prim. exterior:", round(de, 4), "mm")
            print("Generatriz cono:", round(L, 4), "mm")
            print("D ext max (dae):", round(dae, 4), "mm")
        else:
            print("Z1 no puede ser 0")
    else:
        print("Z2 no puede ser 0")
else:
    print("Opcion invalida")
