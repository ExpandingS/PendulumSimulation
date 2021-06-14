from matplotlib.colors import Colormap
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
from math import sqrt, dist, floor
from mpl_toolkits.mplot3d import Axes3D
import json
from time import time
G = 9.8  # acceleration due to gravity, in m/s^2
L1 = 1.0  # length of pendulum 1 in m
L2 = 1.0  # length of pendulum 2 in m
M1 = 1.0  # mass of pendulum 1 in kg
M2 = 1.0  # mass of pendulum 2 in kg


def derivs(state, t):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    delta = state[2] - state[0]
    den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
    dydx[1] = ((M2 * L1 * state[1] * state[1] * sin(delta) * cos(delta)
                + M2 * G * sin(state[2]) * cos(delta)
                + M2 * L2 * state[3] * state[3] * sin(delta)
                - (M1+M2) * G * sin(state[0]))
               / den1)

    dydx[2] = state[3]

    den2 = (L2/L1) * den1
    dydx[3] = ((- M2 * L2 * state[3] * state[3] * sin(delta) * cos(delta)
                + (M1+M2) * G * sin(state[0]) * cos(delta)
                - (M1+M2) * L1 * state[1] * state[1] * sin(delta)
                - (M1+M2) * G * sin(state[2]))
               / den2)

    return dydx

def distance(x1,y1,x2,y2):
    return dist([x1,y1],[x2,y2])
    #return sqrt( (x1 - x2)**2 + (y1-y2)**2 )

def simPend(dTh,time): #Difference in theta2, sim time
    # create a time array from 0..100 sampled at 0.05 second steps
    dt = 0.0001
    t = np.arange(0, time, dt)

    # th1 and th2 are the initial angles (degrees)
    # w10 and w20 are the initial angular velocities (degrees per second)
    th1 = 120.0
    w1 = 0.0
    th2 = 120.0-dTh
    w2 = 0.0

    # initial state
    state = np.radians([th1, w1, th2, w2])


    y = integrate.odeint(derivs, state, t)

    x1 = L1*sin(y[:, 0])
    y1 = -L1*cos(y[:, 0])

    x2 = L2*sin(y[:, 2]) + x1
    y2 = -L2*cos(y[:, 2]) + y1
    return [x2[-1],y2[-1]]


def plot2d():
    dTh = [] #Start change in angle
    Rdist = [] #Resulting distance
    x1, y1 = simPend(0,5)
    for i in range(1,100):
        dTh.append(i)
        xi, yi = simPend(i*0.05,5)
        Rdist.append(distance(x1,y1,xi,yi))

        # x2, y2 = simPend(i/100,20)
        # print(100*distance(x1,y1,x2,y2))
    print(len(dTh))
    plt.scatter(dTh,Rdist)
    plt.show()
#plot2d()

def scale(num):
    return num/10


def create3d():
    print("Started!")
    dTh = [] #Start change in angle
    Rdist = [] #Resulting distance
    timeA  = []
    for time in map(scale,range(1,70)):
        x1, y1 = simPend(0,time)
        print(time)
        for i in range(70):
            timeA.append(time)
            dTh.append(i)
            xi, yi = simPend(i*0.05,time)
            Rdist.append(distance(x1,y1,xi,yi))
    return [dTh,Rdist,timeA]


start = time()
d = create3d() 
print(time() - start)

#save to file or stuff
f = open('data', 'w+')
json.dump(d,f)
f.close()


#now PLOT


#Pffft who needs this
# print(x1)
# fig = plt.figure()
# ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
# ax.set_aspect('equal')
# ax.grid()

# line, = ax.plot([], [], 'o-', lw=2)
# time_template = 'time = %.1fs'
# time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


# def init():
#     line.set_data([], [])
#     time_text.set_text('')
#     return line, time_text


# def animate(i):
#     thisx = [0, x1[i], x2[i]]
#     thisy = [0, y1[i], y2[i]]

#     line.set_data(thisx, thisy)
#     time_text.set_text(time_template % (i*dt))
#     return line, time_text


# ani = animation.FuncAnimation(fig, animate, range(1, len(y)),
#                               interval=dt*1000, blit=True, init_func=init)
# plt.show()  