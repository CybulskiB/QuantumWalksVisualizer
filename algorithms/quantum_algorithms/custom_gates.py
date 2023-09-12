from qiskit import *

#Returning circuit with controll by 1 from first qubit to target qubit
def create_control_gate(qc: QuantumCircuit,first_qubit_id: int, target_qubit_id: int) -> QuantumCircuit:
    if target_qubit_id == first_qubit_id:
        qc.x(target_qubit_id)
    else:
        control_qubits = [i for i in range(first_qubit_id, target_qubit_id)]
        qc.mcx(control_qubits, target_qubit_id)
    return qc
#Returning circuit with increment number by one
def inc_One(qc: QuantumCircuit,no_qubits: int,first_qubit_id: int) -> QuantumCircuit:
    for i in range(first_qubit_id + 1,no_qubits+1 ):
        qc = create_control_gate(qc,first_qubit_id, first_qubit_id -i  + no_qubits )
    return qc
#Returning circuit with controll by 0 from first qubit to target qubit
def create_control_zero_gate(qc: QuantumCircuit,first_qubit_id: int, target_qubit_id: int) -> QuantumCircuit:
    if target_qubit_id == first_qubit_id:
        qc.x(target_qubit_id)
    else:
        control_qubits = [i for i in range(first_qubit_id,target_qubit_id)]
        qc.x(control_qubits)
        qc.mcx(control_qubits, target_qubit_id)
        qc.x(control_qubits)
    return qc
#Returning circuit with decrement number by one
def dec_One(qc: QuantumCircuit,no_qubits: int, first_qubit_id: int) -> QuantumCircuit:
    for i in range(first_qubit_id + 1,no_qubits+1 ):
        qc = create_control_zero_gate(qc,first_qubit_id, first_qubit_id -i + no_qubits )
    return qc