# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 13:57:37 2019

@author: bvdai
"""
# import pylab as plb
import pylab as plb

x = plb.array([1,2,3,4,5])
y=x+3
plb.plot(x,y,'rx')
plb.title('my first graph')
plb.xlabel('Time (Fortnights)')
plb.ylabel('Distance (furlongs)')
plb.xlim(0,6)
plb.ylim(0,10)

# Graph 2
time = plb.linspace(0.0,10.0, 100)  # ************* Linspace fucntion ******
height = plb.exp(-time/3.0) * plb.sin(3*time)
plb.figure() # ********** Create new figure
plb.plot(time, height, 'm-^')
plb.plot(time, 0.3 * plb.sin(3*time), 'g-')
plb.title('graph 2')
plb.ylim(-1,1)
plb.grid()
plb.legend(['damped','constant amplitude'], loc = 'upper right')
plb.xlabel('Time (sec)')
plb.ylabel('Amplitute')