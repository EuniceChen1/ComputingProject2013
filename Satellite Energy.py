import scipy as sp
import numpy as np
import pylab as pl
import scipy.integrate as spi


RMars=3.4E6 # Radius of Mars
msat=260 # Mass of Satellite
G=6.67E-11 # Gravitational Constant
M=6.4E23 # Mass of Mars
vMars=24.1E3 #velocity of Mars
vyMars=0 #yvelocity of Mars
vxMars=24.1E3 #xvelocity of Mars

def f(initial,t):
    x=initial[0] #x position as initial condition 1
    y=initial[1] #y position as initial condition 2
    vx=initial[2] #x velocity as initial condition 3
    vy=initial[3] #y velocity - the change in velocity of Mars as initial condition 4
    G=6.67E-11
    M=6.4E23
    vyMars=0
    vxMars=24.1E3
    f=(vx, vy, -G*M*(x-(vxMars*t))/((x-(vxMars*t))**2+y**2)**1.5, -G*M*y/((x-(vxMars*t))**2+y**2)**1.5) 
    #RHS of the solutions
    #changing the distance of satellite according to the distance of Mars -->(x-(vxMars*t)
    #making Mars move in only the x-direction, so the y position remains the same, y=0
    return f
    #to give output of function f
    
t=np.linspace(0.,100000.,4000) #setting the time increments with (start, end, number of elements)

#FOR ENERGY CHANGES WHEN SATELLITE IS NOT CAPTURED 
#initial x position=3.E8 #This is the initial x position for satellite moving behind Mars
#initial x position=5.E8 #This is the initial x position for satellite moving in front of Mars
#initial y position is fixed at -10.*RMars with
#xvelocity=0 and yvelocity=2000.
#time from 0 - 100000.s
   
initial=[3.E8,-10.*RMars,0.,2000.] #setting initial conditions for [xposition,yposition,xvelocity and yvelocity]
    
satellite_soln=spi.odeint(f,initial,t)

xposition=(satellite_soln[:,0])
yposition=(satellite_soln[:,1])
xvelocity=(satellite_soln[:,2])
yvelocity=(satellite_soln[:,3])
    
pl.figure(1,)
pl.plot(xposition,yposition)
pl.xlabel("x Displacement (m)")
pl.ylabel("y Displacement (m)")

ax=pl.subplot(111) #to add grid line in the graph
ax.grid(True)

x=[5.E8]#to set initial x position of satellite
y=[-10.*RMars]#to set initial y position satellite

pl.plot(x,y,'gx',markersize=10) #the green x marked on the graph indicates the starting point of the satellite

#for total_energy in TE:
velocities=((satellite_soln[:,2])**2+satellite_soln[:,3]**2)
KE=0.5*msat*velocities
#velocities is the magnitude of the xvelocity and yvelocity

distance=((satellite_soln[:,0]-(vMars*t))**2+satellite_soln[:,1]**2)**0.5
PE=-G*M*msat/(distance) 
#taking the formula of Potential Energy
#distance will be (xposition-(distance of Mars))**2+yposition**2)**0.5 

TE=KE+PE #total energy should be conserved

pl.figure(2,)
pl.plot(t,KE)
pl.xlabel("Time (s)")
pl.ylabel("Energy (J)")
#to plot KE against time (blue line in graph)

pl.plot(t,PE,"r")
#to plot PE against time (red line in graph)
pl.legend(('Kinetic Energy','Potential Energy'),loc='upper right')

ax=pl.subplot(111)
ax.grid(True)

pl.figure(3,)
pl.plot (t,TE,"g") 
pl.xlabel("Time (s)")
pl.ylabel ("Total Energy (J)")
#plotting TE against time separately (green line in graph)

ax=pl.subplot(111)
ax.grid(True)

pl.show()