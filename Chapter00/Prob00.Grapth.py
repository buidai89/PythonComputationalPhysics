# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 15:55:16 2019

@author: bvdai
"""

"""
0-0 Graph both of the following functions on a single figure, 
with a usefullysized scale.
"""

import pylab as pl

try:
    x = pl.linspace(0.0,10.0,100)
    y1 = x**4*pl.exp(-2*x) # ** equivalent to ^ in C
    temp = x*x*pl.exp(-x)*pl.sin(x*x)
    y2 = temp*temp
    pl.figure()
    pl.plot(x,y1,'rx')
    pl.plot(x,y2)
    pl.xlabel('Time (sec)')
    pl.ylabel('Amplitude (mV)')
    pl.grid()
    pl.legend(['envelope', 'signal'], loc = 'top right')
    
    
except Exception as err:
    print ('Exception" '+str(err.message))
finally:
    print ('complete!')
