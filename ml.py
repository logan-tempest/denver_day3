#kaegel
#linear regression model 1:1
"""
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def predict(age):
    z=0.042 * age - 1.53
    y=sigmoid(z)
    return y

age = 30

print(predict(age))"""

import numpy as np
import matplotlib.pyplot as plt #graph oke print cheyan upoyogikuna library

ages=np.array([22,25,47,52,46,56,55,60,62,61,18,28,27,29,49])

#x= input y= output

have_insurance = np.array([0,0,1,0,1,1,0,1,1,1,0,0,0,0,1])

linear_output = 0.042 * ages - 1.53

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

sigmoid_op = sigmoid

#age, incom, educate

#y=0.042*x1+0.008*x2+0.2*x3-1.53   equation 3:1
#income=integer 10<1000
#