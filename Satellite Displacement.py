import scipy as sp
import numpy as np
import pylab as pl
import scipy.integrate as spi


RMars=3.4E6 # Radius of Mars
msat=260 # Mass of Satellite
G=6.67E-11 # Gravitational Constant
M=6.4E23 # Mass of Mars

def f(initial,t):
    x=initial[0] #x position as initial condition 1
    y=initial[1] #y position as initial condition 2
    vx=initial[2] #x velocity as initial condition 3
    vy=initial[3] #y velocity as initial condition 4
    G=6.67E-11
    M=6.4E23
    f=(vx, vy, -G*M*x/(x**2+y**2)**1.5, -G*M*y/(x**2+y**2)**1.5) #RHS of the solutions
    
    if  (x**2+y**2)**0.5 < RMars: #to make Mars stop when the satellite crashes
        print "satellite crashed on Mars"
        return [0.,0.,0.,0.]
    
    else:
        return f
        #to give output of function f
    
t=np.linspace(0.,10000000.,40000) #setting the time increments with (start, end, number of elements)

xposition=[] 
yposition=[]
xvelocity=[]
yvelocity=[]
angular_deviation=[]
#creating empty lists at the beginning and append in the loop to avoid overwritting the values in the loop

initialv=np.linspace(400.,400.,1) 
pl.figure(1,)
for initial_velocity in initialv: #looping over the whole code with different initial velocities
   
    initial=[-1.E8,1.E8,initial_velocity,400.] #setting initial conditions for [xposition,yposition,xvelocity and yvelocity]
    
    satellite_soln=spi.odeint(f,initial,t)

    xposition.append(satellite_soln[:,0])
    yposition.append(satellite_soln[:,1])
    xvelocity.append(satellite_soln[:,2])
    yvelocity.append(satellite_soln[:,3])

    pl.plot(satellite_soln[:,0],satellite_soln[:,1])
        
pl.xlabel("x Displacement (m)")
pl.ylabel("y Displacement (m)")

axes=pl.axes() 
Mars=pl.Circle((0,0),radius=3.4E6,fc='r')
axes.add_patch(Mars) # plotting Mars

x=[-1.E8]#to set initial x position
y=[1.E8]#to set initial y position 

pl.plot(x,y,'gx', markersize=10) #the green X marked on the graph indicates the starting point of the satellite

velocities=(satellite_soln[:,2]**2+satellite_soln[:,3]**2)
KE=0.5*msat*velocities
# velocities is the magnitude of the xvelocity and yvelocity

distance=((satellite_soln[:,0]**2)+satellite_soln[:,1]**2)**0.5
PE=-G*M*msat/(distance) 
# taking the formula of Potential Energy
# distance will be (xposition**2+yposition**2)**0.5 

TE=KE+PE 
# total energy should be conserved

pl.figure(2,)
pl.plot(t,KE)
pl.xlabel("Time (s)")
pl.ylabel("Energy (J)")
# to plot KE against time (blue line in graph)

pl.plot(t,PE,"r")
# to plot PE against time (red line in graph)

pl.plot(t,TE,"g")
# to plot TE against time (green line in graph)
pl.legend(('Kinetic Energy','Potential Energy','Total Energy'),loc='upper right')
#to set the key for the graph

pl.figure(3,)
pl.plot (t,TE,"g") 
pl.xlabel("Time (s)")
pl.ylabel ("Total Energy (J)")
#plotting TE against time separately


pl.show()

#Total energy is not well conserved.
#This is shown from the fluctuations given in the graph of Total Energy against time

#when Vx and Vy are both 400, satellite forms circular orbit
#when Vx=770, Vy=0, does gravity sling shot and escapes
#From Vx=0 to 168, satellite crashes on Mars
#After Vx=168 (i.e from Vx=169 onwards to Vx=650), satellite is captured(forms orbit)
