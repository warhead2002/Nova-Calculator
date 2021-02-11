import math as m

global G
G = 6.67*10**(-11)

global h
h = 1.05*10**(-34) 

global c
c = 3*10**8

global kB
kB = 1.38*10**(-23)

global sigma
sigma = 5.67*10**(-8)

global a
a = 7.56*10**(-16)

def redshift(lo,le):
  z = (lo-le)/le
  return z

def kepler_law_3(r,m):
  T = 2*m.pi*m.sqrt((r**3)/(G*m))
  return T

def hubble_law_distance(v):
  D = v/70
  return D

def escape_velocity(M,R):
  v = m.sqrt((2*G*M)/R)
  return v

def Black_hole_temp(M):
  T = (h*(c**3))/8*m.pi*G*M*kB
  return T

def luminosity(A,T):
  L = sigma*A*T**4
  return L

def orbital_period(rho):
  T = m.sqrt((3*m.pi)/G*rho)
  return T

def Schwarzschild_radius(g,M):
  r = m.sqrt((G*M)/g)
  return r

def apparent_brightness(L,d):
  b = L/(4*m.pi*d**2)
  return b

def stellar_radiation_pressure(T):
  P = 0.3*a*T**4
  return 