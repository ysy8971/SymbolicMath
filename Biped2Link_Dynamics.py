import sympy as sp
from sympy import *

ths, thns, ths2 = sp.symbols("ths, thns ths2")
a, b, L = sp.symbols("a, b, L")

T_01 = sp.Matrix([[sp.cos(ths+pi/2), -sp.sin(ths+pi/2), 0, 0], [sp.sin(ths+pi/2), sp.cos(ths+pi/2), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
T_12 = sp.Matrix([[1, 0, 0, L], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
T_23 = sp.Matrix([[sp.cos(ths2), -sp.sin(ths2), 0, 0], [sp.sin(ths2), sp.cos(ths2), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
T_34 = sp.Matrix([[1, 0, 0, L], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

T_02 = T_01 * T_12
T_04 = simplify(T_01 * T_12 * T_23 * T_34)


Px1, Py1, Pz1 = T_02[0,3], T_02[1,3], T_02[2,3]
Px2, Py2, Pz2 = T_04[0,3], T_04[1,3], T_04[2,3]

print("Px1 = ", Px1)
print("Py1 = ", Py1)
print("Px2 = ", Px2)
print("Py2 = ", Py2)

thsval=pi/2
thnsval=0

tns2val=thnsval-pi

print("Px1, Py1= ", Px1.subs([(ths, thsval), (ths2, thnsval)]), Py1.subs([(ths, thsval), (ths2, thnsval)]))
print("Px2, Py2 = ", Px2.subs([(ths, thsval), (ths2, thnsval)]), Py2.subs([(ths, thsval), (ths2, thnsval)]))




"""



M11=Derivative(Px2, ths).doit()
M12=Derivative(Px2, thns).doit()
M21=Derivative(Py2, ths).doit()
M22=Derivative(Py2, thns).doit()




theta1, theta2 = sp.symbols("theta1, theta2")
theta1dot, theta2dot = sp.symbols("theta1dot, theta2dot")

L1, L2 = sp.symbols("L1, L2")


T_01 = sp.Matrix([[sp.cos(theta1), -sp.sin(theta1), 0, 0], [sp.sin(theta1), sp.cos(theta1), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
T_12 = sp.Matrix([[sp.cos(theta2), -sp.sin(theta2), 0, L1], [sp.sin(theta2), sp.cos(theta2), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
T_23 = sp.Matrix([[1, 0, 0, L2], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

T_02 = T_01 * T_12
T_03 = simplify(T_01 * T_12 * T_23)

Px1, Py1, Pz1 = T_02[0,3], T_02[1,3], T_02[2,3]
Px2, Py2, Pz2 = T_03[0,3], T_03[1,3], T_03[2,3]


print("Px1 = ", Px1, ", Py1 = ", Py1, ", Pz1 = ", Pz1)
print("Px2 = ", Px2, ", Py2 = ", Py2, ", Pz2 = ", Pz2)

M11=Derivative(Px2, theta1).doit()
M12=Derivative(Px2, theta2).doit()
M21=Derivative(Py2, theta1).doit()
M22=Derivative(Py2, theta2).doit()

J = sp.Matrix([[M11, M12], [M21, M22]])
#print(J)

x2dot = expand(M11 * theta1dot + M12 * theta2dot)
y2dot = expand(M21 * theta1dot + M21 * theta2dot)

print("x2dot**2=", expand(x2dot*x2dot))
print("y2dot**2=", expand(y2dot*y2dot))

x2vel = simplify(expand(sqrt(x2dot**2+y2dot**2)).doit())
print("x2vel =", x2vel)


#J = sp.Matrix([M11, M12], [M21, M22])


#print(J)

#print("T_01= ", T_01)
#print("T_02= ", T_01*T_12)
#print("T_03= ", T_01*T_12*T_23)



# angle
alpha, beta, gamma = sp.symbols("alpha, beta, gamma")
Px, Py, Pz = sp.symbols("Px, Py, Pz")
Px1, Px2 = sp.symbols("Px1, Px2")
Py1, Py2 = sp.symbols("Py1, Py2")
Pz1, Pz2 = sp.symbols("Pz1, Pz2")

theta1, theta2 = sp.symbols("theta1, theta2")


trs_xx, trs_yy, trs_zz = sp.symbols("trs_xx, trs_yy, trs_zz")
# geometry : a=link1, b=link2
a = sp.symbols("a")

# sine function

#cos_alpha, cos_beta, cos_gamma = sp.cos(alpha), sp.cos(beta), sp.cos(gamma)
#sin_alpha, sin_beta, sin_gamma = sp.sin(alpha), sp.sin(beta), sp.sin(gamma)



#R_x_alpha = sp.Matrix([[1, 0, 0, Px], [0, cos_alpha, -sin_alpha, Py],[0, sin_alpha, cos_alpha, Pz], [0, 0, 0, 1]])
#R_y_beta = sp.Matrix([[cos_beta, 0, sin_beta, Px], [0, 1, 0, Py],[-sin_beta, 0, cos_beta, Pz], [0, 0, 0, 1]])
#R_z_gamma = sp.Matrix([[cos_gamma, -sin_gamma, 0, Px], [sin_gamma, cos_gamma, 0, Py], [0, 0, 1, Pz], [0, 0, 0, 1]])
#R_trans = sp.Matrix([[1, 0, 0, trs_xx], [0, 1, 0, trs_yy], [0, 0, 1, trs_zz], [0, 0, 0, 1]])
#print(R_x_alpha) #print(R_y_beta) #print(R_z_gamma)







x_0 = Matrix([0, 1, 0, 1]) # init axis : x-100 y-010 z-001
x = sp.Matrix([1, 0, 0, 1])

y_z45 = R_z_gamma
y_z45z45 = R_z_gamma * R_z_gamma
y_z45trs4 = R_z_gamma * R_trans

y_z45x45 = R_x_alpha * y_z45


# value - deg & m
alp, bet, gam = (45, 0, 45)
trrx, trry, trrz = (2, 0, 0)
trsxx = 2




# substitute
print("y_z45=", y_z45)
print("y_z45=", y_z45.subs([(alpha, pi/180 * alp), (beta, pi/180 * bet), (gamma, pi/180 * gam), (trs_x, trrx), (trs_y, trry), (trs_z, trrz)]))

#print("y_z45z45=", y_z45z45)
#print("y_z45z45=", y_z45z45.subs([(alpha, pi/180 * alp), (beta, pi/180 * bet), (gamma, pi/180 * gam), (trs_x, trrx), (trs_y, trry), (trs_z, trrz)]))
#print("y_z45=", y_z45)

#print("y_z45trs4=", y_z45trs4.subs([(alpha, pi/180 * alp), (beta, pi/180 * bet), (gamma, pi/180 * gam), (trs_x, trrx), (trs_y, trry), (trs_z, trrz), (trs_xx, trsxx), (trs_yy, trry), (trs_zz, trrz)]))
#print("y_z45trs4=", y_z45trs4)

#print(y_z45x45.subs([(alpha, pi/180 * alp), (beta, pi/180 * bet), (gamma, pi/180 * gam), (trs_x, trrx), (trs_y, trry), (trs_z, trrz)]))


# edit after studying forward matrix and transformation matrix




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