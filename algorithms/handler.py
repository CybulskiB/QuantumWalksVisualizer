import globals.constants as gc
import globals.alg_interface as alg
import algorithms.random_walk as random_walk

def run_algorithm(algorithm_id,initial_pos,iterations,trials):
    match algorithm_id:
        case 1:
            if iterations <= 0 or trials <= 0:
                return(gc.algorithm_runner_id,["Iterations and trialas should be positive integers"])
            else :
                alg.last_result = random_walk.run(initial_pos,iterations,trials)
                return(gc.algorithm_runner_id,["",True])
        case 2: 
            return(gc.algorithm_runner_id,["Quantum Algorithms not implemented yet"])
        case _:
            return(gc.algorithm_runner_id,["Unknown Algorithm ID"])
    