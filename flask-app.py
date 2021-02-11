from flask import Flask, render_template,request
import mechanics as mec

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




if __name__ == '__main__':
    app.run(debug = True)