import sympy as sp
from sympy import *

# angle
alpha, beta, gamma = sp.symbols("alpha, beta, gamma")
trs_x, trs_y, trs_z = sp.symbols("trs_x, trs_y, trs_z")
trs_xx, trs_yy, trs_zz = sp.symbols("trs_xx, trs_yy, trs_zz")
# geometry : a=link1, b=link2
a = sp.symbols("a")

# sine function

cos_alpha, cos_beta, cos_gamma = sp.cos(alpha), sp.cos(beta), sp.cos(gamma)
sin_alpha, sin_beta, sin_gamma = sp.sin(alpha), sp.sin(beta), sp.sin(gamma)



R_x_alpha = sp.Matrix([[1, 0, 0, trs_x], [0, cos_alpha, -sin_alpha, trs_y],[0, sin_alpha, cos_alpha, trs_z], [0, 0, 0, 1]])
R_y_beta = sp.Matrix([[cos_beta, 0, sin_beta, trs_x], [0, 1, 0, trs_y],[-sin_beta, 0, cos_beta, trs_z], [0, 0, 0, 1]])
R_z_gamma = sp.Matrix([[cos_gamma, -sin_gamma, 0, trs_x], [sin_gamma, cos_gamma, 0, trs_y], [0, 0, 1, trs_z], [0, 0, 0, 1]])
R_trans = sp.Matrix([[1, 0, 0, trs_xx], [0, 1, 0, trs_yy], [0, 0, 1, trs_zz], [0, 0, 0, 1]])
#print(R_x_alpha) #print(R_y_beta) #print(R_z_gamma)

x_0 = Matrix([0, 1, 0, 1]) # init axis : x-100 y-010 z-001


x = sp.Matrix([1, 0, 0, 1])

y_z45 = R_z_gamma * x
y_z45z45 = R_z_gamma * R_z_gamma * x
y_z45trs4 = R_trans * R_z_gamma * x

y_z45x45 = R_x_alpha * y_z45


# value - deg & m
alp, bet, gam = (45, 0, 45)
trrx, trry, trrz = (0, 0, 0)
trsxx = 2




# substitute
print("y_z45=", y_z45.subs([(alpha, pi/180 * alp), (beta, pi/180 * bet), (gamma, pi/180 * gam), (trs_x, trrx), (trs_y, trry), (trs_z, trrz)]))
#print("y_z45z45=", y_z45z45)
#print("y_z45z45=", y_z45z45.subs([(alpha, pi/180 * alp), (beta, pi/180 * bet), (gamma, pi/180 * gam), (trs_x, trrx), (trs_y, trry), (trs_z, trrz)]))
print("y_z45=", y_z45)

print("y_z45trs4=", y_z45trs4.subs([(alpha, pi/180 * alp), (beta, pi/180 * bet), (gamma, pi/180 * gam), (trs_x, trrx), (trs_y, trry), (trs_z, trrz), (trs_xx, trsxx), (trs_yy, trry), (trs_zz, trrz)]))
print("y_z45trs4=", y_z45trs4)

#print(y_z45x45.subs([(alpha, pi/180 * alp), (beta, pi/180 * bet), (gamma, pi/180 * gam), (trs_x, trrx), (trs_y, trry), (trs_z, trrz)]))




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