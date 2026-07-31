"""
ECUACIONES UTILIZADAS (Tolerancias y Ajustes):
- Diámetro medio: D = raiz(D_min * D_max)
- Unidad de tolerancia: i = 0.45 * raiz_cubica(D) + 0.001 * D
- Juegos: J_max = D_M_agujero - d_m_eje | J_min = D_m_agujero - d_M_eje
- Aprietos: A_max = d_M_eje - D_m_agujero | A_min = d_m_eje - D_M_agujero
"""
import math

def pedir(msg):
    while True:
        try:
            return float(input(msg))
        except:
            print("Error: numero invalido")

print("1: Diametro medio y U.Tol.")
print("2: Juegos y Aprietos")
opc = input("Elige (1/2): ")

if opc == '1':
    d_min = pedir("D min (mm): ")
    d_max = pedir("D max (mm): ")
    if d_min >= 0 and d_max >= 0:
        D = math.sqrt(d_min * d_max)
        i = 0.45 * (D**(1/3)) + 0.001 * D
        IT = pedir("Calidad IT (ej. 7 para IT7): ")
        Tolerancia_total = i * IT
        
        print("D medio:", round(D, 4), "mm")
        print("i:", round(i, 4), "micras")
        print(f"Tol.(i*IT{int(IT)}):", round(Tolerancia_total, 4), "micras")
    else:
        print("Valores negativos no valen")
elif opc == '2':
    D_M_ag = pedir("D max agujero(mm): ")
    D_m_ag = pedir("D min agujero(mm): ")
    d_M_ej = pedir("d max eje(mm): ")
    d_m_ej = pedir("d min eje(mm): ")
    
    print("J max:", round(D_M_ag - d_m_ej, 4), "mm")
    print("J min:", round(D_m_ag - d_M_ej, 4), "mm")
    print("A max:", round(d_M_ej - D_m_ag, 4), "mm")
    print("A min:", round(d_m_ej - D_M_ag, 4), "mm")
else:
    print("Opcion invalida")
