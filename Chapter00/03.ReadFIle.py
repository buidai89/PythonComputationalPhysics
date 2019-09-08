# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 13:57:37 2019

@author: bvdai
"""

import pylab as pl

try:
    # Read data and put into seperate array, the procedure ignores line begin with #
    # data file can be csv or text, but must be seperated by SPACE, NOT commma
    No, Freq, Ls, Rs, Q = pl.loadtxt('DataToRead.csv', unpack = True)
    print('Result in seperate arrays\r\nNo:\r\n', No, '\r\nFreq:\r\n', Freq, '\r\n')
except Exception as err:
    print ('Exception" '+str(err.message))
finally:
    print ('complete!')

