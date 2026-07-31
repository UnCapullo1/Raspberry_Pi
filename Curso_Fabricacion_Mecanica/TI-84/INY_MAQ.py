# Maquina y Capacidades (DMPP)
import math

while True:
  print("\n-- MAQUINA (INY_MAQ) --")
  print("1: Pesos y Ocupacion")
  print("2: Presiones")
  print("3: Plastificacion")
  print("4: Seleccion y Luz")
  print("0: Salir")
  op = input("Opcion:")
  
  if op=="1":
    print("\n- PESO INYECCION -")
    m_ps = float(input("M_max PS(g):"))
    d_ps = 0.977 
    v_th = m_ps / d_ps
    print("V_th max:",round(v_th,2),"cm3")
    d_mat = float(input("Dens. Mat.(g/cm3):"))
    m_max = v_th * d_mat
    print("M_max Mat:",round(m_max,2),"g")
    m_iny = float(input("M_total iny(g):"))
    if m_max > m_iny: print("OK: Capacidad sufic.")
    else: print("ALERTA: Insuficiente")
    v_iny = m_iny / d_mat
    ocup = (v_iny / v_th) * 100
    print("Ocupacion:",round(ocup,1),"%")
    
  elif op=="2":
    print("\n- PRESION INY -")
    s_p = float(input("Secc. Piston(cm2):"))
    d_h = float(input("Diam. Husillo(mm):"))
    p_h = float(input("Pres. Hidr.(kg/cm2):"))
    f_p = s_p * p_h
    s_h = math.pi * ((d_h/20)**2)
    p_m = f_p / s_h
    p_bar = p_m * 0.981
    print("F Piston:",int(f_p),"kgf")
    print("P Masa:",round(p_m,1),"kg/cm2")
    print("P Masa:",round(p_bar,1),"bar")
    
  elif op=="3":
    print("\n- PLASTIFICACION -")
    m_iny = float(input("Masa iny(g):"))
    t_cic = float(input("T. ciclo(s):"))
    cp = (m_iny / t_cic) * 3.6
    print("Capac summ:",round(cp,2),"kg/h")
    
  elif op=="4":
    print("\n- SELEC. MAQUINA -")
    ce = float(input("Carrera expul(mm):"))
    li = float(input("Long. inyect(mm):"))
    mr = float(input("Mano robot(mm):"))
    mx = float(input("Mov. extrac(mm):"))
    da = ce + li + mr + mx
    print("Dist. Apertura:",round(da,1),"mm")
    gm = float(input("Grosor molde(mm):"))
    luz = (gm + da) * 1.1
    print("Luz Molde(1.1):",round(luz,1),"mm")
    
  elif op=="0":
    break
