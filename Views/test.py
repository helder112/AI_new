from random import random

import numpy as np
import math
import time
teta=np.zeros(9)
x=np.zeros(9)

teta[0]=1
teta[1]=2
teta[2]=3
teta[3]=4
teta[4]=5
teta[5]=6
teta[6]=7
teta[7]=8
teta[8]=9
x[0]=1
x[1]=1
x[2]=1
x[3]=1
x[4]=1
x[5]=1
x[6]=1
x[7]=1
x[8]=1


teta0=1
print("NP.DOT-->" )
print(-1 * np.dot(teta,x)+1)

print("NP.mathmult-->")
print(-1 * np.matmul(teta,x) +1)

print("@-->")
print(-1* (teta @ x)+1)