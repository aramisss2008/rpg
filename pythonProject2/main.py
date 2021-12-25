import numpy as np
from numpy.linalg import inv
from math import sin, cos
'''
def f1(q1, d2, q3):
    return 1.6*sin(q3)*sin(q1)+d2*sin(q1)
def f2(q1, d2, q3):
    return 1.6*sin(q3)*cos(q1)+d2*cos(q1)
def f3(q1, d2, q3):
    return -1.6*cos(q3)+1.4
def fq(q1, d2, q3):
    return np.matrix([f1(q1, d2, q3), f2(q1, d2, q3),f3(q1, d2, q3)]).transpose()
def jacobian(q1, d2, q3):
    return np.matrix(
        [[1.6*sin(q3)*cos(q1)+d2*cos(q1), sin(q1), 1.6*cos(q3)*sin(q1)],
         [-1.6*sin(q3)*sin(q1)-d2*sin(q1), cos(q1), 1.6*cos(q3)*cos(q1)],
         [0, 0, 1.6*sin(q3)]])

divqi = np.matrix([0, 0, -1]).transpose()
S = np.matrix([0.5, -0.4, 0.3]).transpose()
i = 0
q1 = float(divqi[0])
d2 = float(divqi[1])
q3 = float(divqi[2])
diff = S-fq(q1, d2, q3)
while abs(float(diff[0])) > 0.0001 or abs(float(diff[1])) > 0.0001 or abs(float(diff[2])) > 0.0001:
    divqi = divqi + inv(jacobian(q1, d2, q3)).dot(diff)
    q1 = float(divqi[0])
    d2 = float(divqi[1])
    q3 = float(divqi[2])
    diff = S - fq(q1, d2, q3)
    i +=1
print(divqi)
'''


def fvx(q1, d2, q3, divq1, divd2, divq3):
    return (-1.6*sin(q3)*cos(q1)-d2*sin(q1))*divq1+sin(q1)*divd2
def fvy(q1, d2, q3, divq1, divd2, divq3):
    return (1.6*sin(q3)*sin(q1)+d2*sin(q1))*divq1+cos(q1)*divd2
def fvz(q1, d2, q3, divq1, divd2, divq3):
    return (1.6*cos(q3)*sin(q1)-1.6*sin(q3)*cos(q1))*divq3
def fq(q1, d2, q3, divq1, divd2, divq3):
    return np.matrix([fvx(q1, d2, q3, divq1, divd2, divq3), fvy(q1, d2, q3, divq1, divd2, divq3),fvz(q1, d2, q3, divq1, divd2, divq3)]).transpose()

def jacobianV(q1, d2, q3):
    return np.matrix(
        [[-1.6*sin(q3)*sin(q1)-d2*sin(q1), sin(q1), 0],
         [1.6*sin(q3)*cos(q1)+d2*sin(q1), cos(q1), 0],
         [0, 0, 1.6*cos(q3)*sin(q1)-1.6*sin(q3)*cos(q1)]])

q1 = -0.896
d2 = 0.5251
q3 = -0.8128
vx = 0
vy = 0.5
vz = 0.1
divqi = np.matrix([0, 0, -1]).transpose()
V = np.matrix([vx, vy, vz]).transpose()
qDiv = inv(jacobianV(q1,d2,q3)).dot(V)
print(qDiv)