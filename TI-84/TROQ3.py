print("TROQ3")
# --- Datos ---
# e=2, Kd=50
e=2.0
Kd=50.0
# "b" usado en formula (40)
# (Dist. apoyos 40, Ancho 60)
b=40.0
print("e="+str(e))
print("Kd="+str(Kd))
print("b="+str(b))

# --- Doblado en L ---
# Fd = (b * e * Kd) / 6
FdL=(b*e*Kd)/6
print("L) Fd:"+str(round(FdL,2)))

# --- Doblado en U ---
# Fd = (b * e * Kd) / 3
FdU=(b*e*Kd)/3
print("U) Fd:"+str(round(FdU,2)))
