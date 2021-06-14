from matplotlib.colors import Colormap
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
from math import sqrt, dist, floor
from mpl_toolkits.mplot3d import Axes3D
import json

section = 4 # What time to display for the second graph

def plot3d(data):
    dTh, Rdist, timeA = data
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(dTh,timeA,Rdist,c = Rdist)
    ax.set_xlabel("Change in angle (Degrees)")
    ax.set_ylabel("Time (seconds)")
    ax.set_zlabel("Result distance (Metres)")
    ax.set_title("Simulation time vs Angle Difference vs Resulting Distance")
    plt.show()


def plotSection(data,time):
    _dTh, _Rdist, _timeA = data
    dTh, Rdist, timeA = [[],[],[]]
    for i in range(len(_timeA)):
        if(_timeA[i]) == time:
            dTh.append(_dTh[i])
            #timeA.append(_timeA[i])
            Rdist.append(_Rdist[i])
    
    # for i in range(len(dTh)): #For the table
    #     thingo2 = floor(Rdist[i]*1000)/1000
    #     if (dTh[i] % 5 == 0):
    #         print(str(dTh[i]) + " : " + str(thingo2))


    fig = plt.figure()
    # ax = fig.add_subplot(projection='3d')
    # ax.scatter(dTh,timeA,Rdist,c = Rdist)
    plt.scatter(dTh,Rdist)
    plt.plot(dTh,Rdist,c="red")

    plt.xlabel("Change in angle (Degrees)")
    plt.ylabel("Result distance (Meters)")
    plt.title("Starting angle difference vs final distance, at t = " + str(time))
    plt.show()


f = open('data', 'r')
d = json.load(f)
f.close()
print(len(d[0]))
plot3d(d)
plotSection(d,section)