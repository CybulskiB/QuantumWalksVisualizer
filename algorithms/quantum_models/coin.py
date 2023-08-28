import algorithms.quantum_models.constants as qc 
state = "Undefined"
d_state = False

def set(n_state):
    global state, d_state
    state = qc.to_ket(n_state,1)
    d_state = True