# Program to multiply two matrices using nested loops
import random
import numpy as np # import np

N = 250

# NxN matrix
X=[]
X = np.random.randint(0,100, size=(N,N))


#Nx(N+1) matrix
Y=[]
Y = np.random.randint(0,100, size=(N,N+1))


#for i in range(N):
#    Y.append([random.randint(0,100) for r in range(N+1)])

#for i in range(N):
#    Y.append([np.random.randint(0,100) for r in range(N+1)])


result = np.zeros(shape = (N,N+1),dtype = int)
result += np.matmul(X,Y)
[print(r) for r in result]









# result is Nx(N+1)
#result = []
#for i in rang):
#    result.append([0] * (N+1))

# iterate through rows of X
#for i in range(len(X)):
#    # iterate through columns of Y
#    for j in range(len(Y[0])):
#        # iterate through rows of Y
#        for k in range(len(Y)):
#            result[i][j] += X[i][k] * Y[k][j]

#for r in result:
#    print(r)