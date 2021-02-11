from flask import Flask, render_template,request
import mechanics as mec
import astrophysics as astro
import waves as wa
import thermo as th

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





if __name__ == '__main__':
    app.run(debug = True)