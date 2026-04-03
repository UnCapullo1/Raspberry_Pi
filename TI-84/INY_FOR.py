# Fuerzas y Tiempos (DMPP)
import math

while True:
  print("\n-- FUERZA (INY_FOR) --")
  print("1: Fuerza Cierre")
  print("2: Correderas")
  print("3: T. Enfriamiento")
  print("0: Salir")
  op = input("Opcion:")
  
  if op=="1":
    print("\n- FUERZA CIERRE -")
    p = float(input("Pres. Cav(kg/cm2):"))
    sp = float(input("Sup. Pieza(cm2):"))
    n = float(input("Nº Piezas:"))
    sc = float(input("Sup. Canales(cm2):"))
    fc = (p * (sp * n + sc) * 1.2) / 1000
    print("F. Cierre:",round(fc,2),"Ton")
    
  elif op=="2":
    print("\n- CORREDERAS -")
    d = float(input("Contrasalida(mm):"))
    ang = float(input("Angulo(deg):"))
    rad = math.radians(ang)
    lt = d / math.tan(rad)
    ls = d / math.sin(rad)
    print("L(tan):",round(lt,1),"mm")
    print("L(sin):",round(ls,1),"mm")
    v = math.sqrt(lt**2 + d**2)
    print("Recorrido V:",round(v,1),"mm")
    
  elif op=="3":
    print("\n- T. ENFRIAMIENTO -")
    s = float(input("Espesor(mm):"))
    alfa = float(input("Difusiv(x10-3):"))
    ti = float(input("T. iny(C):"))
    tm = float(input("T. molde(C):"))
    te = float(input("T. desmo(C):"))
    t1 = (s**2) / (math.pi**2 * alfa * 0.001)
    t2 = math.log((8/(math.pi**2)) * ((ti-tm)/(te-tm)))
    t = t1 * t2
    print("T. enfria:",round(t,2),"s")
    
  elif op=="0":
    break
