import math

print("HYDRA V1.0")

while True:
  # --- 1. Datos ---
  m_str = input("Masa(kg):")
  if m_str == "q": break
  m = float(m_str)
  
  p_str = input("Pres(bar):")
  p_bar = float(p_str)
  
  # --- 2. Calculos ---
  # F = m * g
  g = 9.8
  f = m * g
  
  # p = bar * 10^5
  p_pa = p_bar * 100000.0
  
  # A = F / p
  area = f / p_pa
  
  # d = sqrt(4*A/pi)
  d_m = math.sqrt((4 * area) / math.pi)
  d_mm = d_m * 1000.0
  
  # --- 3. Resultados ---
  print("F(N):"+str(round(f,2)))
  print("P(Pa):"+str(int(p_pa)))
  print("A(m2):"+str(round(area,6)))
  print("d(mm):"+str(round(d_mm,2)))
  
  input("Btn..")
