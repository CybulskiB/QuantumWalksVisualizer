import numpy as np
from math import sqrt


H = np.array([[1,1], [1,-1]]) * (1/sqrt(2))
I = np.array([[1,0],[0,1]])

k_zero = np.array([1,0])[:, np.newaxis]
k_one =  np.array([0,1])[:, np.newaxis]
b_zero = k_zero.transpose()
b_one = k_one.transpose()

def to_ket(number,no_qubits):
    first  = None
    binary = (bin(number)[2:]).zfill(no_qubits)
    if binary[0] == "1":
        first = k_one 
    else:
        first = k_zero
    res = first
    for i in range(1, no_qubits):
        next_p = None
        next_p = k_one if binary[i] == "1" else k_zero
        res = np.kron(res,next_p)
    return res

def to_bra(number,no_qubits):
    first  = None
    binary = (bin(number)[2:]).zfill(no_qubits)
    if binary[0] == "1":
        first = b_one
    else:
        first = b_zero
    res = first
    for i in range(1, no_qubits):
        next_p = b_one if binary[i] == "1" else b_zero
        res = np.kron(res,next_p)
    return res