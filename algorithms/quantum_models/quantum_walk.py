import numpy as np
import math  as m
import scipy as sp
from tqdm import tqdm
import algorithms.quantum_models.constants as qc 
import algorithms.quantum_models.line_support as ls
import algorithms.quantum_models.coin as coin


def solve_line(initial_pos,steps,trials,beginnig_vertex,ending_vertex):
    n_beginnig_vertex, n_initial_pos, n_ending_vertex, diff = ls.normalize(initial_pos, beginnig_vertex,ending_vertex)
    no_qubits_pos = len(bin(n_ending_vertex - n_beginnig_vertex)) - 2
    print("Generating Evolution Matrix")
    U = ls.U(no_qubits_pos,n_beginnig_vertex,n_ending_vertex)
    print("Computing Final Evolution Matrix")
    U_f = U ** steps
    psi_0 = np.kron(coin.state,qc.to_ket(n_initial_pos,no_qubits_pos))
    print("Computing Final State")
    psi_f = U_f.dot(psi_0)
    result = {}
    print("Measuring")
    for pos in tqdm(range(n_beginnig_vertex,n_ending_vertex+1)):
        pos_probability = 0.0
        for c in range(0,2):
            probability = ls.measure(c,pos,psi_f,no_qubits_pos)**2
            pos_probability += probability
        pos_probability = pos_probability * trials
        result[pos + diff] = pos_probability
    return result




    