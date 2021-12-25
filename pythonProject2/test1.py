import numpy as np
from numpy.linalg import inv
from math import sin, cos, pi


def PxPyPzZxZz(q1, q2, q3, q4, q5):  # 5*1 vector
    return np.matrix([cos(q1) * (135 * cos(q2 + q3) - 160 * sin(q2 + q3 - q4) + 208 * cos(q2)), #px
                      sin(q1) * (135 * cos(q2 + q3) - 160 * sin(q2 + q3 - q4) + 208 * cos(q2)), #py
                      160 * cos(q2 + q3 - q4) + 135 * sin(q2 + q3) + 208 * sin(q2) + 154, #pz
                      -sin(q2 + q3 - q4) * cos(q1), #Zx
                      cos(q2+q3-q4)]).transpose() #Zz


def jacobian(q1, q2, q3, q4, q5):  # 5*5 matrix
    return np.matrix([[-sin(q1) * (135 * cos(q2 + q3) - 160 * sin(q2 + q3 - q4) + 208 * cos(q2)),
                       cos(q1) * (-135 * sin(q2 + q3) - 160 * cos(q2 + q3 - q4) - 208 * sin(q2)),
                       cos(q1) * (-135 * sin(q2 + q3) - 160 * cos(q2 + q3 - q4)),
                       cos(q1) * 160 * cos(q2 + q3 - q4), 0],
                      [cos(q1) * (135 * cos(q2 + q3) - 160 * sin(q2 + q3 - q4) + 208 * cos(q2)),
                       sin(q1) * (-135 * sin(q2 + q3) - 160 * cos(q2 + q3 - q4) - 208 * sin(q2)),
                       sin(q1) * (-135 * sin(q2 + q3) - 160 * cos(q2 + q3 - q4)),
                       sin(q1) * 160 * cos(q2 + q3 - q4), 0],
                      [0, -160 * sin(q2 + q3 - q4) + 135 * cos(q2 + q3) + 208 * cos(q2),
                       -160 * sin(q2 + q3 - q4) + 135 * cos(q2 + q3),
                       160 * sin(q2 + q3 - q4), 0],
                      [sin(q2 + q3 - q4) * sin(q1), -cos(q2 + q3 - q4) * cos(q1), -cos(q2 + q3 - q4) * cos(q1),
                       cos(q2 + q3 - q4) * cos(q1), 0.00000001],
                      [0, -sin(q2+q3-q4), -sin(q2+q3-q4), sin(q2+q3-q4), 0.0000001]])


qi = np.matrix([0.3, 1.0, 1.2, 0, -pi/3])
S = np.matrix([229.0, 183.0, 120.0, 0, -pi/3]).transpose()
fq = PxPyPzZxZz(*qi.tolist()[0])
diff = S - fq
i = 0
while (abs(float(diff[0])) > 1 or abs(float(diff[1])) > 1 or abs(float(diff[2])) > 1) and i < 30:
    invMatr = inv(jacobian(*qi.tolist()[0]))
    step = invMatr.dot(diff)
    qi = qi + step.transpose()
    fq = PxPyPzZxZz(*qi.tolist()[0])
    diff = S - fq
    i +=1
    print(fq)
print(i)



