from flask import Flask, render_template,request
import mechanics as mec
import astrophysics as astro
import waves as wa
import thermo
import quantum as q
import relativity as r

app = Flask(__name__)

#main website
@app.route('/')
def main():
    return render_template('index.html')

# add your section here
# mechanics section
@app.route('/mechanics')
def mechanics():
    return render_template('mechanics.html')

# add your module functions here
# start of mechanics subsection
@app.route('/mechanics/momentum',methods = ['GET','POST'])
def momentum():
    if request.method == 'POST':
        a = int(request.form.get('one'))
        b = int(request.form.get('two'))
        momentum = mec.momentum(a,b)
        # result
        return '<br><br><br><br><br><br><br><br><center><h1>Momentum is: '+str(momentum)+'kg metre sec^-1'+'</h1></center>'
        
    return render_template('mechanics-momentum.html')

@app.route('/mechanics/gravitational-acceleration',methods = ['GET','POST'])
def gravitational_acceleration():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        r = float(request.form.get('two'))
        acceleration = mec.gravitational_acceleration(m,r)
        return '<br><br><br><br><br><br><br><br><center><h1>Acceleration Due To Gravity is: '+str(acceleration)+' metre/sec'+'</h1></center>'
        
    return render_template('mechanics-acceleration.html')

@app.route('/mechanics/force',methods = ['GET','POST'])
def force():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        a = float(request.form.get('two'))
        force = mec.force(m,a)
        return '<br><br><br><br><br><br><br><br><center><h1>Force is: '+str(force)+' metre sec^2'+'</h1></center>'
        
    return render_template('mechanics-force.html')

@app.route('/mechanics/frictional-force',methods = ['GET','POST'])
def frictional_force():
    if request.method == 'POST':
        u = float(request.form.get('one'))
        n = float(request.form.get('two'))
        force = mec.frictional_force(u,n)
        return '<br><br><br><br><br><br><br><br><center><h1>Frictional force is: '+str(force)+' metre sec^2'+'</h1></center>'
        
    return render_template('mechanics-frictional-force.html')

@app.route('/mechanics/centripetal-force',methods = ['GET','POST'])
def centripetal_force():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        v = float(request.form.get('two'))
        r = float(request.form.get('three'))
        force = mec.centripetal_force(m,v,r)
        return '<br><br><br><br><br><br><br><br><center><h1>Centripetal force is: '+str(force)+' metre sec^2'+'</h1></center>'
        
    return render_template('mechanics-centripetal-force.html')

@app.route('/mechanics/work',methods = ['GET','POST'])
def work():
    if request.method == 'POST':
        f = float(request.form.get('one'))
        s = float(request.form.get('two'))
        thet = float(request.form.get('three'))
        force = mec.work(f,s,thet)
        return '<br><br><br><br><br><br><br><br><center><h1>Work is: '+str(force)+' Joule'+'</h1></center>'
        
    return render_template('mechanics-work.html')

@app.route('/mechanics/kinetic-energy',methods = ['GET','POST'])
def kinetic_energy():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        v = float(request.form.get('two'))
        energy = mec.kinetic_energy(m,v)
        return '<br><br><br><br><br><br><br><br><center><h1>Kinetic Energy is: '+str(energy)+' Joule'+'</h1></center>'
        
    return render_template('mechanics-kinetic-energy.html')

@app.route('/mechanics/potential-energy',methods = ['GET','POST'])
def potential_energy():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        g = float(request.form.get('two'))
        h = float(request.form.get('three'))
        energy = mec.potential_energy(m,g,h)
        return '<br><br><br><br><br><br><br><br><center><h1>Potential Energy is: '+str(energy)+' Joule'+'</h1></center>'
        
    return render_template('mechanics-potential-energy.html')

@app.route('/mechanics/power',methods = ['GET','POST'])
def power():
    if request.method == 'POST':
        w = float(request.form.get('one'))
        t = float(request.form.get('two'))
        power = mec.power(w,t)
        return '<br><br><br><br><br><br><br><br><center><h1>Power is: '+str(power)+' Watt'+'</h1></center>'
        
    return render_template('mechanics-power.html')

@app.route('/mechanics/moment-of-inertia',methods = ['GET','POST'])
def moment_of_inertia():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        r = float(request.form.get('two'))
        inertia = mec.moment_of_inertia(m,r)
        return '<br><br><br><br><br><br><br><br><center><h1>Moment of Inertia is: '+str(inertia)+' Kg metre^2'+'</h1></center>'
        
    return render_template('mechanics-inertia.html')

@app.route('/mechanics/impulse',methods = ['GET','POST'])
def impulse():
    if request.method == 'POST':
        f = float(request.form.get('one'))
        t = float(request.form.get('two'))
        impulse = mec.impulse(f,t)
        return '<br><br><br><br><br><br><br><br><center><h1>Impulse is: '+str(impulse)+' Kg metre^2'+'</h1></center>'
        
    return render_template('mechanics-impulse.html')

@app.route('/mechanics/radius-of-gyration',methods = ['GET','POST'])
def radius_of_gyration():
    if request.method == 'POST':
        i = float(request.form.get('one'))
        m = float(request.form.get('two'))
        rad = mec.radius_of_gyration(i,m)
        return '<br><br><br><br><br><br><br><br><center><h1>Radius of Gyration is: '+str(rad)+' Metre'+'</h1></center>'
        
    return render_template('radius-of-gyration.html')


# Atrophysics code
@app.route('/astrophysics')
def astrophysics():
    return render_template('astrophysics.html')

@app.route('/astrophysics')
def astropyhsics():
    return render_template('astrophysics.html')

# add your module functions here
# start of mechanics subsection
@app.route('/astro/redshift',methods = ['GET','POST'])
def redshift():
    if request.method == 'POST':
        le = int(request.form.get('one'))
        lo = int(request.form.get('two'))
        redshift = astro.redshift(lo,le)
        return '<br><br><br><br><br><br><br><br><center><h1>Redshift is: '+str(redshift)+'</h1></center>'
        
    return render_template('astro-redshift.html')

@app.route('/astro/kepler',methods = ['GET','POST'])
def kepler_law_3():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        r = float(request.form.get('two'))
        time = astro.kepler_law_3(m,r)
        return '<br><br><br><br><br><br><br><br><center><h1>Orbital Period is: '+str(time)+' sec'+'</h1></center>'
        
    return render_template('astro-kepler.html')

@app.route('/astro/hubble',methods = ['GET','POST'])
def hubble_law_distance():
    if request.method == 'POST':
        V = float(request.form.get('one'))
        distance = astro.hubble_law_distance(V)
        return '<br><br><br><br><br><br><br><br><center><h1>Distance is: '+str(distance)+' light years'+'</h1></center>'
        
    return render_template('astro-hubble.html')

@app.route('/astro/escape-velocity',methods = ['GET','POST'])
def escape_velocity():
    if request.method == 'POST':
        M = float(request.form.get('one'))
        r = float(request.form.get('two'))
        velocity = astro.escape_velocity(M,r)
        return '<br><br><br><br><br><br><br><br><center><h1>Escape Velocity is: '+str(velocity)+' metre sec'+'</h1></center>'
        
    return render_template('astro-escape-velocity.html')

@app.route('/astro/black-hole',methods = ['GET','POST'])
def black_hole_temp():
    if request.method == 'POST':
        M = float(request.form.get('one'))
        temp = astro.black_hole_temp(M)
        return '<br><br><br><br><br><br><br><br><center><h1>Black Hole Temperature is: '+str(temp)+' kelvin'+'</h1></center>'
        
    return render_template('astro-black-hole.html')

@app.route('/astro/luminosity',methods = ['GET','POST'])
def luminosity():
    if request.method == 'POST':
        A = float(request.form.get('one'))
        T = float(request.form.get('two'))
        luminosity = astro.luminosity(A,T)
        return '<br><br><br><br><br><br><br><br><center><h1>Work is: '+str(luminosity)+' Joules sec'+'</h1></center>'
        
    return render_template('astro-luminosity.html')

@app.route('/astro/orbital-period',methods = ['GET','POST'])
def orbital_period():
    if request.method == 'POST':
        rho = float(request.form.get('one'))
        period = astro.orbital_period(rho)
        return '<br><br><br><br><br><br><br><br><center><h1>Orbital Period is: '+str(period)+' second'+'</h1></center>'
        
    return render_template('astro-orbital-period.html')

@app.route('/astro/schwarzschild',methods = ['GET','POST'])
def schwarzschild_radius():
    if request.method == 'POST':
        M = float(request.form.get('one'))
        r = float(request.form.get('two'))
        radius = astro-schwarzschild_radius(M,r)
        return '<br><br><br><br><br><br><br><br><center><h1>Schwarzschild Radius is: '+str(radius)+' metre'+'</h1></center>'
        
    return render_template('astro-schwarzschild.html')

@app.route('/astro/apparent-brightness',methods = ['GET','POST'])
def apparnet_brightness():
    if request.method == 'POST':
        L = float(request.form.get('one'))
        d = float(request.form.get('two'))
        brightness = astro.apparent_brightness(L,d)
        return '<br><br><br><br><br><br><br><br><center><h1>Apparent brightness is: '+str(brightness)+' Watt metre^2'+'</h1></center>'
        
    return render_template('astro-apparent-brightness.html')

@app.route('/astro/stellar-radiation',methods = ['GET','POST'])
def stellar_radiation_pressure():
    if request.method == 'POST':
        T = float(request.form.get('one'))
        pressure = astro.stellar_radiation_pressure(T)
        return '<br><br><br><br><br><br><br><br><center><h1>Stellar Radiation Pressure is: '+str(pressure)+' Pascal</h1></center>'
        
    return render_template('astro-stellar-radiation.html')

# Waves code

@app.route('/waves')
def waves():
    return render_template('waves.html')

# add your module functions here
# start of mechanics subsection
@app.route('/waves/wavelength',methods = ['GET','POST'])
def wavelength():
    if request.method == 'POST':
        v = int(request.form.get('one'))
        f = int(request.form.get('two'))
        wavelength = wa.wavelength(v,f)
        return '<br><br><br><br><br><br><br><br><center><h1>Wavelength is: '+str(wavelength)+' Hertz</h1></center>'
        
    return render_template('waves-wavelength.html')

@app.route('/waves/frequency',methods = ['GET','POST'])
def frequency():
    if request.method == 'POST':
        T = float(request.form.get('one'))
        frequecy = wa.frequency(T)
        return '<br><br><br><br><br><br><br><br><center><h1>Frequency is: '+str(frequency)+' Hertz'+'</h1></center>'
        
    return render_template('waves-frequency.html')

@app.route('/waves/doppler-effect',methods = ['GET','POST'])
def doppler_effect():
    if request.method == 'POST':
        fs = float(request.form.get('one'))
        v = float(request.form.get('two'))
        vo = float(request.form.get('three'))
        vs = float(request.form.get('four'))
        frequency = wa.doppler_effect(fs,vo,v,vs)
        return '<br><br><br><br><br><br><br><br><center><h1>Doppler effect is: '+str(frequency)+' Hertz'+'</h1></center>'
        
    return render_template('waves-doppler-effect.html')

@app.route('/waves/harmonic-wave',methods = ['GET','POST'])
def harmonic_wave():
    if request.method == 'POST':
        A = float(request.form.get('one'))
        l = float(request.form.get('two'))
        x = float(request.form.get('three'))
        v = float(request.form.get('four'))
        t = float(request.form.get('five'))
        phi = float(request.form.get('six'))
        displacement = wa.harmonic_wave(A,l,x,v,t,phi)
        return '<br><br><br><br><br><br><br><br><center><h1>Displacement of a given point along the wave is: '+str(displacement)+' metre'+'</h1></center>'
        
    return render_template('waves-harmonic-wave.html')

@app.route('/waves/diffraction-grating',methods = ['GET','POST'])
def diffraction_grating():
    if request.method == 'POST':
        d = float(request.form.get('one'))
        m = float(request.form.get('two'))
        l = float(request.form.get('three'))
        D = float(request.form.get('four'))
        fringe = wa.diffraction_spacing(d,m,l,D)
        return '<br><br><br><br><br><br><br><br><center><h1>Fringe Spacing is: '+str(fringe)+' centimetre'+'</h1></center>'
        
    return render_template('waves-diffraction-grating.html')

@app.route('/waves/sound-pressure-level',methods = ['GET','POST'])
def sound_pressure_level():
    if request.method == 'POST':
        P = float(request.form.get('one'))
        Pref = float(request.form.get('two'))
        level = wa.sound_pressure_level(P,Pref)
        return '<br><br><br><br><br><br><br><br><center><h1>Sound Pressure Level is: '+str(level)+' decibel'+'</h1></center>'
        
    return render_template('waves-sound-pressure-level.html')

@app.route('/waves/alfven-velocity',methods = ['GET','POST'])
def alfven_velocity():
    if request.method == 'POST':
        B = float(request.form.get('one'))
        rho = float(request.form.get('two'))
        velocity = wa.alfven_velocity(B,rho)
        return '<br><br><br><br><br><br><br><br><center><h1>Alfvén Velocity is: '+str(velocity)+' metre sec'+'</h1></center>'
        
    return render_template('waves-alfven-velocity.html')

# Quantum mechanics

@app.route('/quantum')
def quantum():
    return render_template('quantum.html')

@app.route('/quantum/bohr_model',methods = ['GET','POST'])
def bohr_model():
    if request.method == 'POST':
        E1 = float(request.form.get('one'))
        E2 = float(request.form.get('two'))
        bohr_model = q.bohr_model(E1,E2)
        return '<br><br><br><br><br><br><br><br><center><h1>Bohr Model is: '+str(bohr_model)+'kg metre sec^-1'+'</h1></center>'
        
    return render_template('quantum_bohr.html')

@app.route('/quantum/compton_scattering',methods = ['GET','POST'])
def compton_scattering():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        theta = float(request.form.get('two'))
        c_scattering = q.compton_scattering(m,theta)
        return '<br><br><br><br><br><br><br><br><center><h1>Compton Scattering is: '+str(c_scattering)+' metre/sec'+'</h1></center>'
        
    return render_template('quantum_c_scattering.html')

@app.route('/quantum/compton_wavelength',methods = ['GET','POST'])
def compton_wavelength():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        c_wavelength = q.compton_wavelength(m)
        return '<br><br><br><br><br><br><br><br><center><h1>Compton Wavelength is: '+str(c_wavelength)+' metre sec^2'+'</h1></center>'
        
    return render_template('quantum_c_wavelength.html')

@app.route('/quantum/curie_constant',methods = ['GET','POST'])
def curie_constant():
    if request.method == 'POST':
        N = float(request.form.get('one'))
        a = float(request.form.get('two'))
        u = float(request.form.get('three'))
        cu_con = q.curie_constant(N,a,u)
        return '<br><br><br><br><br><br><br><br><center><h1>Curie Constant is: '+str(cu_con)+' metre sec^2'+'</h1></center>'
        
    return render_template('quantum_cu_con.html')

@app.route('/quantum/de_broglie_wavelength',methods = ['GET','POST'])
def de_broglie_wavelength():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        v = float(request.form.get('two'))
        p = float(request.form.get('three'))
        de_broglie = q.de_broglie_wavelength(m,v,p)
        return '<br><br><br><br><br><br><br><br><center><h1>de Broglie Wavelength is: '+str(de_broglie)+' metre sec^2'+'</h1></center>'
        
    return render_template('quantum_de_broglie.html')

@app.route('/quantum/hydrogen_energy',methods = ['GET','POST'])
def hydrogen_energy():
    if request.method == 'POST':
        n = float(request.form.get('one'))
        z = float(request.form.get('two'))
        hy_en = q.hydrogen_energy(n,z)
        return '<br><br><br><br><br><br><br><br><center><h1>Hydrogen Energy is: '+str(hy_en)+' Joule'+'</h1></center>'
        
    return render_template('quantum_hy_en.html')

@app.route('/quantum/photoelectric_effect',methods = ['GET','POST'])
def photoelectric_effect():
    if request.method == 'POST':
        f = float(request.form.get('one'))
        f0 = float(request.form.get('two'))
        PE = q.photoelectric_effect(f,f0)
        return '<br><br><br><br><br><br><br><br><center><h1>Photoelectric Effect is: '+str(PE)+' Joule'+'</h1></center>'
        
    return render_template('quantum_PE.html')

@app.route('/quantum/photon_energy',methods = ['GET','POST'])
def photon_energy():
    if request.method == 'POST':
        w = float(request.form.get('one'))
        ph_en = q.photon_energy(w)
        return '<br><br><br><br><br><br><br><br><center><h1>Photon Energy is: '+str(ph_en)+' Joule'+'</h1></center>'
        
    return render_template('quantum_ph_en.html')

@app.route('/quantum/rydberg_eqn',methods = ['GET','POST'])
def rydberg_eqn():
    if request.method == 'POST':
        z = float(request.form.get('one'))
        n1 = float(request.form.get('two'))
        n2 = float(request.form.get('three'))
        ry_eqn = q.rydberg_eqn(z,n1,n2)
        return '<br><br><br><br><br><br><br><br><center><h1>Rydberg Equation is: '+str(ry_eqn)+' Watt'+'</h1></center>'
        
    return render_template('quantum_ry_eqn.html')

@app.route('/quantum/stefan_boltzmann',methods = ['GET','POST'])
def stefan_boltzmann():
    if request.method == 'POST':
        a = float(request.form.get('one'))
        t = float(request.form.get('two'))
        e = float(request.form.get('three'))
        st_bo = q.stefan_boltzmann(a,t,e)
        return '<br><br><br><br><br><br><br><br><center><h1>Stefan Boltzmann Constant is: '+str(st_bo)+' Kg metre^2'+'</h1></center>'
        
    return render_template('quantum_ste_boltz.html')

@app.route('/quantum/wein_law_pw',methods = ['GET','POST'])
def wein_law_pw():
    if request.method == 'POST':
        bbt = float(request.form.get('one'))
        pw = q.wein_law_pw(bbt)
        return '<br><br><br><br><br><br><br><br><center><h1>Peak Wavelength is: '+str(pw)+' Kg metre^2'+'</h1></center>'
        
    return render_template('quantum_wein_pw.html')

@app.route('/quantum/wein_law_pf',methods = ['GET','POST'])
def wein_law_pf():
    if request.method == 'POST':
        bbt = float(request.form.get('one'))
        pf = q.wein_law_pf(bbt)
        return '<br><br><br><br><br><br><br><br><center><h1>Peak Frequency is: '+str(pf)+' Metre'+'</h1></center>'
        
    return render_template('quantum_wein_pf.html')

# Thermodynamics Section

@app.route('/thermodynamics')
def thermodynamics():
    return render_template('thermodynamics.html')


# add your module functions here
# start of thermo subsection
@app.route('/thermodynamics/Absorbtive-power', methods=['GET', 'POST'])
def absorbtive_power():
    if request.method == 'POST':
        a = int(request.form.get('one'))
        b = int(request.form.get('two'))
        absorbpower = thermo.absorbtive_power(a, b)
        return '<br><br><br><br><br><br><br><br><center><h1>absorbtive Latent_Heat is: ' + str(
            absorbpower) + '</h1></center>'

    return render_template('Absorbtive-power.html')


@app.route('/thermodynamics/Emissivity', methods=['GET', 'POST'])
def Emissivity():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        r = float(request.form.get('two'))
        Emissivity = thermo.Emissivity(m, r)
        return '<br><br><br><br><br><br><br><br><center><h1>Emissivity is: ' + str(Emissivity) + '</h1></center>'

    return render_template('Emissivity.html')


@app.route('/thermodynamics/Enthalpy-of-Reaction', methods=['GET', 'POST'])
def Enthalpy_of_Reaction():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        a = float(request.form.get('two'))
        Enthalpy_of_Reaction = thermo.Enthalpy_of_Reaction(m, a)
        return '<br><br><br><br><br><br><br><br><center><h1>Enthalpy of Reaction is: ' + str(
            Enthalpy_of_Reaction) + ' Joule' + '</h1></center>'

    return render_template('Enthalpy-of-Reaction.html')


@app.route('/thermodynamics/Entropy', methods=['GET', 'POST'])
def Entropy():
    if request.method == 'POST':
        u = float(request.form.get('one'))
        n = float(request.form.get('two'))
        Entropy = thermo.Entropy(u, n)
        return '<br><br><br><br><br><br><br><br><center><h1>Frictional Enthalpy_of_Reaction is: ' + str(
            Entropy) + ' Joule/K' + '</h1></center>'

    return render_template('Entropy.html')


@app.route('/thermodynamics/first-law-of-thermodynamics', methods=['GET', 'POST'])
def first_law_of_thermodynamics():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        v = float(request.form.get('two'))
        Flot = thermo.first_law_of_thermodynamics(m, v)
        return '<br><br><br><br><br><br><br><br><center><h1>First law of thermodynamics is: ' + str(
            Flot) + ' Joule' + '</h1></center>'

    return render_template('first-law-of-thermodynamics.html')


@app.route('/thermodynamics/Gibbs-Energy', methods=['GET', 'POST'])
def Gibbs_Energy():
    if request.method == 'POST':
        f = float(request.form.get('one'))
        s = float(request.form.get('two'))
        thet = float(request.form.get('three'))
        GE = thermo.Gibbs_Energy(f, s, thet)
        return '<br><br><br><br><br><br><br><br><center><h1>Work is: ' + str(GE) + ' Joule' + '</h1></center>'

    return render_template('Gibbs-Energy.html')


@app.route('/thermodynamics/Heat-Capacity-Ratio', methods=['GET', 'POST'])
def Heat_Capacity_Ratio():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        v = float(request.form.get('two'))
        ratio = thermo.Heat_Capacity_Ratio(m, v)
        return '<br><br><br><br><br><br><br><br><center><h1>Heat Capacity Ratio is: ' + str(ratio) + '</h1></center>'

    return render_template('Heat-Capacity-Ratio.html')


@app.route('/thermodynamics/Isobaric-Work-done', methods=['GET', 'POST'])
def Isobaricwork():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        g = float(request.form.get('two'))
        h = float(request.form.get('three'))
        energy = thermo.Isobaricwork(m, g, h)
        return '<br><br><br><br><br><br><br><br><center><h1>Isobaric Work Done is: ' + str(
            energy) + ' Joule' + '</h1></center>'

    return render_template('Isobaric-Work-done.html')


@app.route('/thermodynamics/Latent-Heat', methods=['GET', 'POST'])
def Latent_Heat():
    if request.method == 'POST':
        w = float(request.form.get('one'))
        t = float(request.form.get('two'))
        Latent_Heat = thermo.Latent_Heat(w, t)
        return '<br><br><br><br><br><br><br><br><center><h1>Latent Heat is: ' + str(
            Latent_Heat) + ' Joule' + '</h1></center>'

    return render_template('Latent-Heat.html')


@app.route('/thermodynamics/Linear-Expansion', methods=['GET', 'POST'])
def Linear_Expansion():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        r = float(request.form.get('two'))
        c = float(request.form.get('three'))
        LinearExpansion = thermo.Linear_Expansion(m, r, c)
        return '<br><br><br><br><br><br><br><br><center><h1>Linear Expansion is: ' + str(
            LinearExpansion) + ' metre' + '</h1></center>'

    return render_template('Linear-Expansion.html')


@app.route('/thermodynamics/specific-heat', methods=['GET', 'POST'])
def Specific_Heat():
    if request.method == 'POST':
        f = float(request.form.get('one'))
        t = float(request.form.get('two'))
        x = float(request.form.get('three'))
        Specific_Heat = thermo.Specific_Heat(f, t, x)
        return '<br><br><br><br><br><br><br><br><center><h1>Specific Heat is: ' + str(
            Specific_Heat) + ' Joule/(kg*K)' + '</h1></center>'

    return render_template('specific-heat.html')


@app.route('/thermodynamics/Thermal-Resistance', methods=['GET', 'POST'])
def Thermal_Resistance():
    if request.method == 'POST':
        i = float(request.form.get('one'))
        m = float(request.form.get('two'))
        u = float(request.form.get('three'))
        rad = thermo.Thermal_Resistance(i, m, u)
        return '<br><br><br><br><br><br><br><br><center><h1>Thermal Resistance is: ' + str(
            rad) + ' K/watt' + '</h1></center>'

    return render_template('Thermal-Resistance.html')

# Relativity section

@app.route('/relativity')
def relativity():
    return render_template('relativity.html')

@app.route('/relativity/e_mc2',methods = ['GET','POST'])
def e_mc2():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        emc = r.e_mc2(m)
        return '<br><br><br><br><br><br><br><br><center><h1>Energy is: '+str(emc)+' Joule'+'</h1></center>'
        
    return render_template('relativity_emc2.html')

@app.route('/relativity/length_contraction',methods = ['GET','POST'])
def length_contraction():
    if request.method == 'POST':
        l = float(request.form.get('one'))
        v = float(request.form.get('two'))
        lc = r.length_contraction(l,v)
        return '<br><br><br><br><br><br><br><br><center><h1>Length Contraction is: '+str(lc)+' metre'+'</h1></center>'
        
    return render_template('relativity_lc.html')

@app.route('/relativity/relativistic_kinetic_energy',methods = ['GET','POST'])
def relativistic_kinetic_energy():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        v = float(request.form.get('two'))
        rke = r.relativistic_kinetic_energy(m,v)
        return '<br><br><br><br><br><br><br><br><center><h1>Relativistic Kinetic Energy is: '+str(rke)+' Joule'+'</h1></center>'
        
    return render_template('relativity_rke.html')

@app.route('/relativity/time_dilation',methods = ['GET','POST'])
def time_dilation():
    if request.method == 'POST':
        t = float(request.form.get('one'))
        v = float(request.form.get('two'))
        td = r.time_dilation(t,v)
        return '<br><br><br><br><br><br><br><br><center><h1>Time Dilation is: '+str(td)+' sec'+'</h1></center>'
        
    return render_template('relativity_td.html')

@app.route('/relativity/velocity_addition',methods = ['GET','POST'])
def velocity_addition():
    if request.method == 'POST':
        v = float(request.form.get('one'))
        w = float(request.form.get('two'))
        va = r.velocity_addition(v,w)
        return '<br><br><br><br><br><br><br><br><center><h1>Velocity Addition is: '+str(va)+' metre sec^2'+'</h1></center>'
        
    return render_template('relativity_va.html')

@app.route('/relativity/mass_variation',methods = ['GET','POST'])
def mass_variation():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        v = float(request.form.get('two'))
        mv = r.mass_variation(m,v)
        return '<br><br><br><br><br><br><br><br><center><h1>Mass Variation is: '+str(mv)+' Kg'+'</h1></center>'
        
    return render_template('relativity_mv.html')

if __name__ == '__main__':
    app.run(debug = True)