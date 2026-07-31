import math

while True:
  print("\n-- T. FABRICACION --")
  print("1: Soldadura")
  print("2: Fresado")
  print("3: Torneado")
  print("4: Corte (Sierra/Laser)")
  print("0: Salir")
  op = input("Opcion:")
  
  if op=="1":
    print("\n- SOLDADURA -")
    l = float(input("L total(mm):"))
    va = float(input("V.Avance(mm/min):"))
    ef = float(input("Eficiencia(0-1):"))
    ta = l / va
    tt = ta / ef
    print("T. Arco:",round(ta,2),"min")
    print("T. Total:",round(tt,2),"min")
    
  elif op=="2":
    print("\n- FRESADO -")
    l = float(input("L a fresar(mm):"))
    d = float(input("D fresa(mm):"))
    z = float(input("N dientes:"))
    vc = float(input("Vc(m/min):"))
    fz = float(input("fz(mm/diente):"))
    pas = float(input("Pasadas:"))
    n = (vc * 1000) / (math.pi * d)
    vf = fz * z * n
    lt = l + d
    tc = (lt / vf) * pas
    print("RPM:",round(n,0))
    print("Avance:",round(vf,1),"mm/min")
    print("T. Total:",round(tc,2),"min")
    
  elif op=="3":
    print("\n- TORNEADO -")
    l = float(input("L tornear(mm):"))
    d = float(input("D pieza(mm):"))
    vc = float(input("Vc(m/min):"))
    f = float(input("f(mm/rev):"))
    pas = float(input("Pasadas:"))
    n = (vc * 1000) / (math.pi * d)
    tc = (l / (f * n)) * pas
    print("RPM:",round(n,0))
    print("T. Total:",round(tc,2),"min")
    
  elif op=="4":
    print("\n- CORTE -")
    print("1:Sierra 2:Laser/Ciz")
    tcorte = input("Tipo:")
    if tcorte=="1":
      l = float(input("L cortar(mm):"))
      d = float(input("D disco(mm):"))
      z = float(input("N dientes:"))
      vc = float(input("Vc(m/min):"))
      fz = float(input("fz(mm/diente):"))
      n = (vc * 1000) / (math.pi * d)
      vf = fz * z * n
      tc = l / vf
      print("RPM:",round(n,0))
      print("Avance:",round(vf,1),"mm/min")
    else:
      l = float(input("L total(mm):"))
      vc = float(input("V corte(mm/min):"))
      tc = l / vc
    ef = float(input("Eficiencia(0-1):"))
    tt = tc / ef
    print("T. Neto:",round(tc,2),"min")
    print("T. Total:",round(tt,2),"min")
    
  elif op=="0":
    break
