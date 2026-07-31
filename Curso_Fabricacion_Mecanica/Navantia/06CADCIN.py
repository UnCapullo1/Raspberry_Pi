"""
ECUACIONES UTILIZADAS (Cadenas Cinematicas):
- Relacion Transmision: i = i1 * i2 * ... | i = N_salida / N_entrada = Z_conductora / Z_conducida
- RPM Salida: N_out = N_in * i_total
- Paso de rosca (Lira): Paso_rosca = Paso_tornillo_patron * i_lira
"""
import math

def pedir(msg):
    while True:
        try:
            return float(input(msg))
        except:
            print("Error: numero invalido")

print("--- CADENAS CINEMATICAS ---")
print("1: RPM Salida (N_out)")
print("2: Relacion Tren Engran.")
print("3: Paso Roscado (Lira)")
opc = input("Opcion (1-3): ")

if opc == '1':
    Nin = pedir("RPM Motor N_in: ")
    n = int(pedir("Num. de pares transmision: "))
    i_tot = 1
    for k in range(n):
        print("--- Par", k+1, "---")
        # i_k = Z_cond / Z_conducida (o similar)
        Z1 = pedir("Z o D Conductora: ")
        Z2 = pedir("Z o D Conducida: ")
        if Z2 != 0:
            i_tot *= (Z1 / Z2)
        else:
            print("Z2 no puede ser 0")
            i_tot = 0
            break
            
    if i_tot != 0:
        Nout = Nin * i_tot
        print("i total:", round(i_tot, 4))
        print("N salida:", round(Nout, 2), "RPM")

elif opc == '2':
    Z1 = pedir("Z Conductora 1: ")
    Z2 = pedir("Z Conducida 1: ")
    opc_mas = input("Tiene 2do par? (s/n): ").strip().lower()
    
    if Z2 != 0:
        i = Z1 / Z2
        if opc_mas == 's':
            Z3 = pedir("Z Conductora 2: ")
            Z4 = pedir("Z Conducida 2: ")
            if Z4 != 0:
                i *= (Z3 / Z4)
            else:
                print("Z4 no puede ser 0")
                i = 0
                
        if i != 0:
            print("Relacion Total (i):", round(i, 4))
    else:
        print("Z2 no puede ser 0")

elif opc == '3':
    P_tp = pedir("Paso tornillo patron(mm): ")
    i_lira = pedir("Relacion Lira (i): ")
    
    P_rosca = P_tp * i_lira
    print("Paso a roscar:", round(P_rosca, 4), "mm")

else:
    print("Opcion invalida")
