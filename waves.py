import math as m

global u0
u0 = 4*(m.pi)*10**(-7)

def wavelength(v,f):
  l = v/f
  return l

def frequency(T):
  f = 1/T
  return f

def doppler_effect(fs,v,vo,vs):
  fo = fs(v+vo)/(v+vs)
  return fo

def harmonic_wave(A,l,x,v,t,phi):
  y = A*m.sin((2*m.pi)/l)*(x-v*t)+phi
  return y

def diffraction_grating(d,m,l,D):
  y = (m*l*D)/d
  return y

def sound_presure_level(P,Pref):
  SPL = 20*m.log(P/Pref)
  return SPL

def Alfven_velocity(B,rho):
  v = B/m.sqrt(u0*rho)
  return v