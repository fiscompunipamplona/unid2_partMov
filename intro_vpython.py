from vpython import sphere, scene, vector, rate, color, arrow
from numpy import sin, cos, pi


arrow_x = arrow(pos=vector(0,0,0), axis=vector(0.5,0,0), color=color.red)
arrow_y = arrow(pos=vector(0,0,0), axis=vector(0,0.5,0), color=color.green)
arrow_z = arrow(pos=vector(0,0,0), axis=vector(0,0,0.5))

R = 0.1 # m
xp = 0. # m
yp = 1. # m
zp = 0. # m

grv = 9.8 # m/s^2

th = 30.*(pi/180.)

scene.range = 2.*yp # m

prtcl = sphere(pos=vector(xp,yp,zp), radius=R, color=color.cyan)

ax = grv*sin(th)*cos(th)
ay = grv*(cos(th) - 1)
dt = 0.005
prtcl.velocity = vector(ax, ay, 0)

t = 0

while t < 3:
    rate(100)
    prtcl.pos = prtcl.pos + prtcl.velocity*dt
    t += dt
