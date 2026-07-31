import math
print("Q2")
# --- Datos ---
N=70000
e=1.5
rho=8.9/1000000
# --- Dimensiones ---
# m = 10 + 1.8
m=11.8
# n = 14 + 1.5
n=15.5
print("m="+str(m))
print("n="+str(n))
# --- a) Angulo ---
# alpha = atan(m/n)
ar=math.atan(m/n)
ad=math.degrees(ar)
d=int(ad)
md=(ad-d)*60
mm=int(md)
sd=(md-mm)*60
print("a)Ang:"+str(d)+"d "+str(mm)+"' "+str(round(sd,2))+"''")
# --- b) Paso ---
# p = sqrt(m^2 + n^2)
p=math.sqrt(m**2+n**2)
print("b)Pas:"+str(round(p,2)))
# --- c) Ancho ---
rt=7
# x = 7 * sin(alpha)
x=rt*math.sin(ar)
xp=rt-x
br=(math.pi/2)-ar
rb=5
# y = 5 * sin(90-alpha)
y=rb*math.sin(br)
yp=rb-y
# a = 20 * cos(alpha) + x'
a=20*math.cos(ar)+xp
# b = 44 * sin(alpha) + y'
b_len=44*math.sin(ar)+yp
# B = 1.5 + a + b + 1.5
B=1.5+a+b_len+1.5
print("c)Anc:"+str(round(B,2)))
# --- d) Longitud ---
# L = N * p
L=N*p/1000
print("d)Lon:"+str(round(L,2))+"m")
# --- e) Peso ---
# W = Vol * rho
W=L*1000*B*e*rho
print("e)Pes:"+str(round(W,2))+"kg")
