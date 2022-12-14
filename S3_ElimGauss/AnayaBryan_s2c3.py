# -*- coding: utf-8 -*-
"""AnayaBryan_S2C2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gIQWM7DpMEq7bLZOk_NHmala3zSGxntc
"""

import numpy as np

# Sistemas de ecuaciones lineales
N = 6
A = (np.random.random((N,N))*10.0)-5.0
B = (np.random.random((N,1))*10.0)-5.0

def Elim_Gauss(A,B):
  for i in range(A.shape[0]):
    B[i] = B[i]/A[i,i]
    A[i,:] = A[i,:]/A[i,i]
    for j in range(i+1,A.shape[1]):
      B[j] = B[j] - B[i]*A[j,i]
      A[j,:] = A[j,:] - A[i,:]*A[j,i]
  x = np.zeros(A.shape[0])
  n = A.shape[1]
  for k in range(n-1,-1,-1):
    x[k] = B[k] - np.sum(A[k,:]*x)
    print(x)
  return A,B

A_g,B_g = Elim_Gauss(A,B)
print("Solución <numérica>:",B_g)
print("Solución <verdadera>:",np.linalg.solve(A,B))

# Terminar eliminacion Gauss
# Matriz de cov

np.size(B_g)

A.shape[1]

