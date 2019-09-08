# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 13:57:37 2019

@author: bvdai
"""
"""
In electronics, Kirchhoff’s laws are used to solve for the currents
# through components in circuit networks. Applying these laws
gives us systems of linear equations, which can then be expressed
as matrix equation
"""

"""
Refer to Python > Howto > Python_Scipy_Cheatsheet_Linear_Algebra for more info
"""

import numpy as np
from scipy import linalg, sparse

A = np.mat([[-13, 2, 4], [2, -11, 6], [4, 6, -15]])
B = np.array([[5], [-10], [5]])
C = linalg.solve(A,B)
print('Kirchhoff’s equation A*I = B \r\nCurrent [Ia Ib Ic] = ')
print(C)