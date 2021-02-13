# -*- coding: utf-8 -*-
"""physics calculator

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NR2MfmVQI7Qx7BAfoFdl0t5GDysU43HE
"""

def Carnot_efficiency_calculator(T1,T2):
  a = (T1+273) / (T2 + 273)
  b = (1 - a) * 100
  return b

def Efficiency_calculator(W,Q):
  Ef = (W/Q)
  return Ef

def joule_heating_calculator(C,R,T):
  H = (C**2)*R*T
  return H

def IdealGasLawforPressure(n,T,V):
  R = 0.0821
  P = (n*R*T)/V
  return P

def Idealgaslawforvolume(n,T,P):
  R = 0.0821
  V = (n*R*T)/P
  return V

def Idealgaslawfortemperature(P,V,n):
  R =0.0821
  T = P*V/(n*R)
  return T

def Idealgaslawforamount(P,V,T):
  R = 0.0821
  n = P*V/(R*T)
  return n

def Linear_Expansion(l,a,t):
  fl = l*(1+a*t)
  return fl

def Area_Expansion(A,a,t):
  fa = A*(1+a*t)
  return fa

def Volume_Expansion(V,a,t):
  fv = V*(1+a*t)
  return fv

def Thermal_Resistance(l,K,A): 
  R = l/(K*A)
  return R

  
def Heat_Transfer(T,t,R):
  Q = -t*T/R
  return Q

def absorbtive_power(Ea,Ei):
  Ap = Ea/Ei
  return Ap

def Emissivity(Es,Eb):
  Emis = Es/Eb
  return Emis

def first_law_of_thermodynamics(Q,W):
  U = Q - W
  return U

def Hhyd(Hsol,Hlattice):
  Hhyd = Hsol - Hlattice
  return Hhyd

def Gibbs_Energy(H,T,S):
  G = H - T*S
  return G

def Entropy(q,T):
  S = q/T
  return S

def Enthalpy_of_Reaction(Hreact,Hproduct):
  Hrxn = Hreact - Hproduct
  return Hrxn

def thermalstress(strain,Y):
  stress = strain*Y
  return stress

def Latent_Heat(Q,m):
  LH = Q/m
  return LH

def Specific_Heat(Q,m,T):
  C = Q/(m*T)
  return C

def Heat_Capacity_Ratio(Cp,Cv):
  gm = Cp/Cv
  return gm

def InternalEnergy(f,n,R,T):
  U = f*n*R*T/2
  return U

def Isobaricwork(P,V1,V2):
  W = P*(V2-V1)
  return W