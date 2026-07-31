import math

while True:
  print("\n-- DISENO MECANICO --")
  print("1: Fuerza Cilindro")
  print("2: Fuerza Tijera")
  print("3: Torque Husillo")
  print("4: Peso Material")
  print("5: Cortadura Bulon")
  print("6: Pandeo Vastago")
  print("7: C.Gravedad Moto")
  print("0: Salir")
  op = input("Opcion:")
  
  if op=="1":
    print("\n- CILINDRO HIDRAULICO -")
    d = float(input("D interior(mm):"))
    p = float(input("Presion(bar):"))
    a = math.pi * (d/2)**2 / 100 
    f = (p * 10) * a  
    f_kg = f / 9.81
    print("Area:",round(a,2),"cm2")
    print("Fuerza:",round(f_kg,1),"kg")
    
  elif op=="2":
    print("\n- FUERZA TIJERA -")
    p = float(input("Carga base(kg):"))
    fs = float(input("Fact.Seguridad(1.5):"))
    l = float(input("L brazo(mm):"))
    h = float(input("Altura act(mm):"))
    p = p * fs
    if h >= l:
      print("Error: h >= L")
    else:
      ang = math.asin(h/l)
      f = p / math.tan(ang)
      print("Angulo:",round(math.degrees(ang),1),"deg")
      print("F.Cil(FS inc):",round(f,1),"kg")
      
  elif op=="3":
    print("\n- TORQUE HUSILLO -")
    p = float(input("Carga base(kg):"))
    fs = float(input("Fact.Seguridad(1.5):"))
    d = float(input("D medio(mm):"))
    pas = float(input("Paso(mm):"))
    mu = float(input("Coef.Fric(0.1):"))
    w = p * fs * 9.81
    ah = math.atan(pas / (math.pi * d))
    af = math.atan(mu)
    t = w * (d/2000) * math.tan(ah + af)
    print("Torque(FS inc):",round(t,2),"Nm")
    
  elif op=="4":
    print("\n- PESO MATERIAL -")
    print("1:Chapa 2:Tubo Cuad")
    tm = input("Tipo:")
    if tm=="1":
      x = float(input("Largo(mm):"))
      y = float(input("Ancho(mm):"))
      e = float(input("Espesor(mm):"))
      v = x*y*e / 1e9
    else:
      x = float(input("Largo(mm):"))
      a = float(input("Ancho ext(mm):"))
      e = float(input("Espesor(mm):"))
      ae = a*a
      ai = (a-2*e)*(a-2*e)
      v = x * (ae - ai) / 1e9
    kg = v * 7850
    print("Peso:",round(kg,2),"kg")

  elif op=="5":
    print("\n- CORTADURA BULON -")
    f = float(input("Fuerza tot(kg):"))
    d = float(input("D bulon(mm):"))
    c = float(input("Zonas corte(1/2):"))
    fs = float(input("Fact.Seg(1.5):"))
    a = math.pi * (d/2)**2
    tau = (f * 9.81 * fs) / (c * a)
    print("FS incl. Tension:")
    print(round(tau,1),"MPa")
    if tau>150:
      print("ALERTA: Muy alto")

  elif op=="6":
    print("\n- PANDEO VASTAGO -")
    d = float(input("D vastago(mm):"))
    l = float(input("L extendido(mm):"))
    fs = float(input("Fact.Seguridad(2):"))
    i = (math.pi * d**4) / 64
    fc = (math.pi**2 * 210000 * i) / (l**2)
    fmax = (fc / 9.81) / fs
    print("F.Max Segura:")
    print(round(fmax,1),"kg")

  elif op=="7":
    print("\n- C.GRAVEDAD MOTO -")
    p = float(input("Peso Moto(kg):"))
    l = float(input("Dist.Ejes(mm):"))
    pf = float(input("% Peso Delan(40):"))
    pd = 100 - pf
    x = l * (pd / 100)
    print("Dist CG a Delant:")
    print(round(x,1),"mm")
    print("Apoyo Del:",round(p*(pf/100),1),"kg")
    print("Apoyo Tra:",round(p*(pd/100),1),"kg")

  elif op=="0":
    break
