# Diseño de Molde (DMPP)
import math

while True:
  print("\n-- MOLDE (INY_MOL) --")
  print("1: Cavidades")
  print("2: Canales/Boquilla")
  print("3: Refrigeracion")
  print("0: Salir")
  op = input("Opcion:")
  
  if op=="1":
    print("\n- Nº CAVIDADES -")
    print("Intro datos:")
    n_p = float(input("Cant. piezas:"))
    c_m = float(input("Coste maq(e/h):"))
    c_o = float(input("Coste oper(e/h):"))
    c_ml = float(input("Coste molde(1):"))
    t_c = float(input("T. ciclo(s):"))
    print("Usa nomograma con estos datos.")
    
  elif op=="2":
    print("\n- CANALES Y BOQUILLA -")
    sub = input("1:Canal, 2:Boq, 3:Beb?")
    if sub=="1":
      w = float(input("Peso pieza(g):"))
      e = float(input("Espesor(mm):"))
      d = 3.8 * (w**0.25) * (e**0.25)
      print("Diam. sugerido:",round(d,1),"mm")
    elif sub=="2":
      m = float(input("Masa(g):"))
      den = float(input("Dens. fund(g/cm3):"))
      ti = float(input("T. llenado(s):"))
      vd = m / den
      q = vd / ti
      sr = float(input("Shear Rate max:"))
      r3 = (4 * q) / (math.pi * sr)
      r = r3**(1/3)
      print("Radio d:",round(r*10,2),"mm")
      print("Diam d:",round(r*20,2),"mm")
    elif sub=="3":
      l = float(input("Long. placa(mm):"))
      d1 = float(input("Diam. boquilla(mm):"))
      df = d1 + 1 + (l * 0.035)
      print("Df mec:",round(df,1),"mm")
      
  elif op=="3":
    print("\n- REFRIGERACION -")
    d = float(input("Diam. canal(mm):"))
    e = float(input("Espesor pieza(mm):"))
    print("B (Prof):",round(2.5*d,1),"mm (avg)")
    print("A (Dist):",round(4.5*d,1),"mm (avg)")
    
  elif op=="0":
    break
