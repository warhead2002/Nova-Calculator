import math as m
def wavelength(l,v,f):
  l = v/f
  return l

def frequency(f,T):
  f = 1/T
  return f

def doppler_effect(fo,fs,v,vo,vs):
  fo = fs(v+vo)/(v+vs)
  return fo

def harmonic_wave(y,A,l,x,v,t,phi):
  y = A*m.sin((2*m.pi)/l)*(x-vt)+phi
  return y

def diffraction_grating(d,m,l,D,y):
  y = (m*l*D)/d
  return y

def sound_presure_level(SPL,P,Pref):
  SPL = 20*m.log(P/Pref)
  return SPL

def Alfeven_velocity(v,B,rho):
  v = B/m.sqrt(4*m.pi*rho)
  return v

import math as m
def redshift(z,lo,le):
  z = (lo-le)/le
  return z

def kepler_law_3(T,r,m):
  T = 2*m.pi*m.sqrt((r**3)/(6.67*10**-11)*m)
  return T

def hubble_law_distance(v,D):
  v = 70*D
  return v

def escape_velocity(v,M,R):
  v = m.sqrt((2*(6.67*10**-11)*M)/R)
  return v

def Black_hole_temp(T,M):
  T = ((1.05*10**-34)*(3*10**8)**3)/8*m.pi*(6.67*10**-11)*M*1.38*10**-23
  return T

def luminosity(L,A,T):
  L = (5.67*10**-8)*A*T**4
  return L

def orbital_period(T,rho):
  T = m.sqrt((3*m.pi)/(6.67*10**-11)*rho)
  return T

def Schwarzschild_radius(g,M,r):
  g = (6.67*10**-11)*M/r**2
  return g

def apparent_brightness(b,L,d):
  b = L/(4*m.pi*d**2)
  return b

def stellar_radiation_pressure(P,T):
  P = 0.3*(7.56*10**-16)*T**4
  return P
