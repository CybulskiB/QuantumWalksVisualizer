from qiskit import *
import qiskit 
from  qiskit_ibm_provider import *
import numpy as np 
import algorithms.quantum_algorithms.custom_gates as cg
import algorithms.quantum_models.constants as cqm
import algorithms.quantum_models.coin as coin
import algorithms.quantum_models.line_support as ls


def step_on_line(qc: QuantumCircuit, no_qubits :int) -> QuantumCircuit:
    qubits = [i for i in range (0,no_qubits -1)]
    qubits = [no_qubits-1] + qubits
    qc.h(no_qubits -1)
    empty_circ = QuantumCircuit(no_qubits -1)
    inc_gate = cg.inc_One(empty_circ.copy(),no_qubits -1,0).to_gate().control(1)
    dec_gate = cg.dec_One(empty_circ.copy(),no_qubits -1,0).to_gate().control(1)
    qc.append(inc_gate,qubits)
    qc.x(no_qubits -1)
    qc.append(dec_gate,qubits)
    qc.x(no_qubits -1)
    return qc



def solve_line(initial_pos,steps,trials,beginnig_vertex,ending_vertex,is_real_quantum,token):
    print("Creating circuit")
    n_beginnig_vertex, n_initial_pos, n_ending_vertex, diff = ls.normalize(initial_pos, beginnig_vertex,ending_vertex)
    no_qubits_pos = len(bin(n_ending_vertex - n_beginnig_vertex)) -2
    no_qubits = no_qubits_pos + 1
    q_ids = [i for i in range(no_qubits)]
    qc = QuantumCircuit(no_qubits)
    finall_initial_pos = np.kron(coin.state,cqm.to_ket(n_initial_pos,no_qubits_pos))
    initial_state = [q for vector in finall_initial_pos for q in vector]
    qc.initialize(initial_state,q_ids)
    
    qubits = [i for i in range (0,no_qubits -1)]
    qubits = [no_qubits-1] + qubits
    empty_circ = QuantumCircuit(no_qubits -1)
    inc_gate = cg.inc_One(empty_circ.copy(),no_qubits -1,0).to_gate().control(1)
    dec_gate = cg.dec_One(empty_circ.copy(),no_qubits -1,0).to_gate().control(1)

    for i in range(steps):
        qc.h(no_qubits -1)
        qc.append(inc_gate,qubits)
        qc.x(no_qubits -1)
        qc.append(dec_gate,qubits)
        qc.x(no_qubits -1)
    qc.measure_all()
    print("Setting backend")
    if is_real_quantum :
        IBMProvider.save_account(token, overwrite=True)
        provider = IBMProvider()
        backend  = provider.get_backend('ibm_perth')
        job = execute(qc,backend ,shots = 20000)
        return job.job_id()
    else:
        backend = Aer.get_backend('qasm_simulator')
        job = qiskit.execute(qc,backend,shots=trials)
        result = job.result()
        counts = result.get_counts(qc)
        return counts, diff

    