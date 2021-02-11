import math as m

global G
G= 6.67*(10**-11)
global h
h = 6.6260*(10**34)
global c
c= 3*(10**8)
global pi
pi=3.1415
global K
K= 1.3806*(10**-23)

def de_broglie_wavelength(m,v):
    global lamb
    lamb = h/(m*v)
    return lamb

def energy_contained_in_a_photon(lamb):
    E = h*c/lamb
    return E

def energy_in_nth_orbit(Z,n):
    E1 = -13.6 
    En = -13.6*(Z*2/n*2)
    return En

#def Wavelength_corresponding_to_spectral_lines(R,n1,n2):
    #lamb = 1/(R*(((1/n1)*2)–((1/n2)*2)))
    #return 1/lamb

def Moseley_Law(a,b,z):
    m.sqrt(v) = a*(z–b)
    #a and b are positive constants
    #return sqrt(v)

def Average_radius_of_nucleus(A):
    Rknot = 1.1 x 10-15 M
    R = ((1.1*10-15*)A)*(1/3)
    #A = mass number
    return R

def Half_life(lambda):
    T(half) = 0.693/lambda
    return T(half)
  
def Average_life(): 
    Tavg = T(half)/0.693
    return Tavg

#particle_at_temperature_T
def energy(T): 
    E = (3/2)*K*T
    return E

def wavelegnth(m,T):
    lambda = h/(√3*m*K*T)
    return lambda

def Compton_wave_length(mknot):
    lambda_c = h/(mknot*c)
#h is Planck’s constant, mknot is rest mass of electron c is speed light
    return lambda_c

#angular momentum of an electron is an integral multiple of h/2π
def angular_momentum(n):
    mvr = nh/2π
    return mvr

def Orbital_velocity_of_electron():
    vn= (2*pi*k*Z*(e**2))/nh
    return vn

def Kinetic_energy_of_electron():
    KE = (1/2)*k*(Z*(e**2)/r)
    return KE

def Potential_energy_of_electron():
    PE = -k*(Z*(e**2)/r )
    return PE

#Mass of proton, mp = 1.6726×10-27 kg
#Charge of proton = 1.602×10-19 C
#Mass of neutron, mn = 1.6749×10-27 kg
#(1 amu) = 1.66×10-27 kg= 1 u = 931.5 MeV
#Rydberg’s constant: R=k2 =2π2z2 me4/ch3

def Volume_of_the_nucleus():
    V = 4/3*pi*(Rknot*A(1/3))**3
    return V

def mass_energy(m):
    E = m*(c**2)
    return E

def photoelectric_effect(f,fknot):
    Kmax = h*(f − fknot)
    return Kmax

def Time_Dilation(t,v):
    td = t/(m.sqrt((1 − (v**2))/(c**2)))
    return td