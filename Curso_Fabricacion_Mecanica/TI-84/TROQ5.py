import math
print("TROQ5")

# --- Datos ---
k1=0.75
k2=0.90
# Final d=30, h=42
df=30.0
hf=42.0

# --- D Primitivo ---
D=math.sqrt(df**2 + 4*df*hf)
print("D="+str(round(D,2)))

# --- Etapa 1 ---
num_h = D**2 - df**2
d1 = k1 * D
print("d1="+str(round(d1,2)))
h1 = num_h / (4*d1)
print("h1="+str(round(h1,2)))

# Pausa para ver datos
input("Btn..")

# --- Etapas siguientes ---
d_prev = d1
for i in range(2, 8):
  dn = k2 * d_prev
  hn = num_h / (4*dn)
  print("d"+str(i)+"="+str(round(dn,2)))
  print("h"+str(i)+"="+str(round(hn,2)))
  d_prev = dn
  
  # Pausa cada 2 estapas
  if i % 2 != 0:
    input("Btn..")
