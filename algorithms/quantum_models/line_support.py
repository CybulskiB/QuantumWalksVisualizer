import numpy as np
import scipy.sparse as sparse
import algorithms.quantum_models.constants as qc 

def sum_right(no_qubits,begining_vertex,ending_vertex):
    res = np.zeros((2**no_qubits,2**no_qubits))
    for i in range(begining_vertex,ending_vertex):
        res += np.outer(qc.to_ket(i+1,no_qubits),qc.to_bra(i,no_qubits))
    return res

#print(sum_right())
def sum_left(no_qubits,begining_vertex,ending_vertex):
    res = np.zeros((2**no_qubits,2**no_qubits))
    for i in reversed(range(begining_vertex+1,ending_vertex+1)):
        res += np.outer(qc.to_ket(i-1,no_qubits),qc.to_bra(i,no_qubits))
    return(res)
def S(no_qubits,begining_vertex,ending_vertex):
    # |0><0|
    projector_zero = sparse.csr_matrix(np.outer(qc.k_zero,qc.b_zero))
    # |1><1|
    projector_one = sparse.csr_matrix(np.outer(qc.k_one,qc.b_one))
    left_sum = sum_left(no_qubits,begining_vertex,ending_vertex)
    right_sum = sum_right(no_qubits,begining_vertex,ending_vertex)
    return sparse.kron(projector_zero,left_sum) + sparse.kron(projector_one,right_sum)
def H_I(no_qubits):
    Ip = qc.I
    for i in range(1,no_qubits):
        Ip = sparse.kron(Ip,qc.I)
    return sparse.kron(qc.H,Ip)

def U(no_qubits,begining_vertex,ending_vertex):
    return S(no_qubits,begining_vertex,ending_vertex).dot(H_I(no_qubits))

def create_projector(coin, pos,no_qubits):
    coin_projector = None
    if coin == 1:
        coin_projector = np.outer(qc.k_one,qc.b_one) 
    else:
        coin_projector = np.outer(qc.k_zero,qc.b_zero)
    pos_projector = np.outer(qc.to_ket(pos,no_qubits),qc.to_bra(pos,no_qubits))
    projector = np.kron(coin_projector,pos_projector)
    return projector

def measure(coin,pos,state,no_qubits):
    projector = create_projector(coin,pos,no_qubits)
    probability = np.sum(np.dot(projector,state))
    return probability

def normalize(initial_pos, beginnig_vertex,ending_vertex):
    diff = beginnig_vertex
    n_beginnig_vertex = 0 
    n_initial_pos = initial_pos - diff
    n_ending_vertex = ending_vertex - diff 
    return n_beginnig_vertex, n_initial_pos, n_ending_vertex, diff
