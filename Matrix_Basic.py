import sympy as sp
from sympy import *

# angle
alpha, beta, gamma = sp.symbols("alpha, beta, gamma")

# geometry : a=link1, b=link2
a = sp.symbols("a")



# sine function

cos_alpha, cos_beta, cos_gamma = sp.cos(alpha), sp.cos(beta), sp.cos(gamma)
sin_alpha, sin_beta, sin_gamma = sp.sin(alpha), sp.sin(beta), sp.sin(gamma)

R_x_alpha = sp.Matrix([[1, 0, 0],[0, cos_alpha, -sin_alpha],[0, sin_alpha, cos_alpha]])
R_y_beta = sp.Matrix([[cos_beta, 0, sin_beta],[0, 1, 0],[-sin_beta, 0, cos_beta]])
R_z_gamma = sp.Matrix([[cos_gamma, -sin_gamma, 0],[sin_gamma, cos_gamma, 0],[0, 0, 1]])
#print(R_x_alpha) #print(R_y_beta) #print(R_z_gamma)

x = sp.Matrix([1, 0, 0])
y = R_z_gamma * x

deg=45
print(y.subs(gamma, pi/180 * deg))
print(N(y.subs(gamma, pi/180 * deg)))



"""
y1 = sp.cos(theta)
print(y1)

y1d = sp.diff(sp.cos(theta))
print(y1d)


x1 = sp.Matrix([1, 2, 3])
print(x1)

Rx = sp.Matrix([[sp.cos(x), 0, -sp.sin(x)],[0, 1, 0],[sp.sin(x), 0, sp.cos(x)]])
print(Rx)

Rxx1 = Rx * x1
print(Rxx1)
"""