#import your libraries such as math,numpy etc on top
import math as m

#set constants global so u can use in all functions
global G
G = 6.67*(10**-11)

#define formulas in functions
def gravitational_acceleration(m,r):
    g = (G*m)/(r**2)
    #return values instead of print for easy function calls
    return g

def momentum(m,v):
    p = m*v
    return p

def force(m,a):
    f = m*a
    return f

def frictional_force(u,n):
    f = u*n
    return f

def centripetal_force(m,v,r):
    f = m*(v**2)/r
    return f

def work(f,s,thetha):
    w = f*s*m.cos(thetha)
    return w

def kinetic_energy(m,v):
    k = 0.5*m*(v**2)
    return k

def potential_energy(m,g,h):
    p = m*g*h
    return p

def power(w,t):
    p = w/t
    return p

def moment_of_inertia(m,r):
    i = m*(r**2)
    return i

def impulse(f,t):
    i = f*t
    return i

def radius_of_gyration(i,m):
    k  = (i/m)**(1/2)
    return k

def angular_momentum(i,w):
    l = i*w
    return l

def torque(r,f,thetha):
    t = r*f*m.sin(thetha)
    return t

def gravitational_force(M,m,r):
    f = G*M*m/(r**2)
    return f
    
def orbital_velocity(m,r):
    v = (G*m/r)**(1/2)
    return v

def escape_velocity(m,r):
    v = (2*G*m/r)**(1/2)
    return v

def time_period_planet(m,a):
    t = 4*3.1415*(a**3)/(G*m)
    return t

def compressibility(bulk_mod):
    c = 1/bulk_mod
    return c

def modulus_of_rigidity(f,l,a,del_a):
    y = (f*l)/(a*del_a)
    return y
def surface_tension(f,l):
    s = 0.5*f/l
    return s

def hydrostatic_pressure(q,g,h):
    p = q*g*h
    return p
def bouyant_force(q,v,g):
    f = q*v*G
    return f
def stokes_force(n,r,v):
    f = 6*3.14159*n*r*v
    return f
def timeperiod_pendulum(l,g):
    t = 2*3.14159*(l/g)**(1/2)
    return t
def energy_pendulum(m,w,a):
    e = 0.5*m*(w**2)*(a**2)
    return e