import math
print("TROQ4")

# --- Datos ---
e=2.0
r=3.0
print("e="+str(e))
print("r="+str(r))

# --- Fibra Neutra ---
R = r + (e/2)
print("R_neutra="+str(R))

# --- Longitud Arco ---
AB = (2*math.pi*R)/4
print("Arco_AB="+str(round(AB,2)))

input("Btn..")

# --- Segmentos Rectos ---
sa = 50 - 5
sb = 100 - 10
sc = 125 - 10
sd = 100 - 10
se = 50 - 10
sf = 50 - 5

print("a="+str(sa))
print("b="+str(sb))
print("c="+str(sc))
print("d="+str(sd))
print("e="+str(se))
print("f="+str(sf))

input("Btn..")

# --- Longitud Total ---
L = sa + sb + sc + sd + se + sf + (5 * AB)
print("L_total:"+str(round(L,2)))

# --- Resumen ---
print("---")
print("L="+str(round(L,2))+" mm")
