print("TROQ1")
# --- Datos ---
Kc=105.0
e=2.0
Pe=142.83
Pi=60.0
print("Kc="+str(Kc))
print("e="+str(e))
print("P_ext="+str(Pe))
print("P_int="+str(Pi))

# --- 1. F. Corte ---
Fce=Pe*e*Kc
Fci=Pi*e*Kc
Fct=Fce+Fci
print("1)Fc_ext:"+str(round(Fce,2)))
print("  Fc_int:"+str(round(Fci,2)))
print("  Fc_TOT:"+str(round(Fct,2)))

input("Btn..")

# --- 2. F. Expulsion ---
Fexp=Fct*1.5
print("2)Fexp:"+str(round(Fexp,2)))

# --- 3. F. Extraccion ---
Fext_e=Fce*0.04
Fext_i=Fci*0.07
Fext_t=Fext_e+Fext_i
print("3)Fext_e:"+str(round(Fext_e,2)))
print("  Fext_i:"+str(round(Fext_i,2)))
print("  Fext_TOT:"+str(round(Fext_t,2)))

# --- 4. F. Rozamiento ---
Froz=Fct*1.2
print("4)Froz:"+str(round(Froz,2)))

input("Btn..")

# --- Resumen Tons ---
print("--- Tons ---")
print("Fc:"+str(round(Fct/1000,2))+"T")
print("Fexp:"+str(round(Fexp/1000,2))+"T")
print("Fext:"+str(round(Fext_t/1000,2))+"T")
print("Froz:"+str(round(Froz/1000,2))+"T")
