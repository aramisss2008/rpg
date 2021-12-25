import numpy as np

def xxx(x,y,z):
    print(x,y,z)

a = np.matrix([0.001,0.2,3]).tolist()[0]

xxx( *a)

