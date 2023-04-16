
"""""""""""
NumPy Coding

"""""""""""

import numpy as np

NumP_Array = np.array([[1,2,3],[4,6,7]])

NP1 = np.array([[1,3],[4,5]])

NP2 = np.array([[3,4],[5,7]])

# Multiplication of matrices
MNP = NP1@NP2
MNP3 = np.dot(NP1,NP2)

# Multiplication of individual numbers
MNP2 = NP1*NP2
MNP4 = np.multiply(NP1,NP2)

# Addition
Sum1 = NP1+NP2

# Subtraction
Sub1 = NP1-NP2

Sub2 = np.subtract(NP1,NP2)

# Element summation
np.sum(NP1)

Broad_Nump = NP1+3

NP3 = np.array([[3,4]])

NP1+NP3

# Division
D = np.divide([12,14,16],5)

D1 = np.floor_divide([12,14,16],5)

#Squareroot
np.math.sqrt(10)

#Distributions
#Normal distribution
ND = np.random.standard_normal((3,4))

#Uniform distribution
UD = np.random.uniform(1,12,(3,4))

# Generate random Float No.
np.random.rand()

# Generate Integer No.
Random_Ar= np.random.randint(1,50,(2,5))

#Zeros
Ze = np.zeros((3,4))
#Ones
Ones = np.ones((3,4))


Filter_Ar = np.logical_and(Random_Ar>30,Random_Ar<50)

F_Random_Ar = Random_Ar[Filter_Ar]


Data_N = np.array([1,3,4,5,7,9])

Mean_N = np.mean(Data_N)

Median_N = np.median(Data_N)

Var_N = np.var(Data_N)

SD_N = np.std(Data_N)


NumP_Array = np.array([[1,2,3],[4,6,7]])


Var_Nump = np.var(NumP_Array,axis=1)

Var_Nump2 = np.var(NumP_Array,axis=0)











