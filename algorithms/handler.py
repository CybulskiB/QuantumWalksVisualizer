import globals.constants as gc
import globals.alg_interface as alg
import algorithms.classical_algorithms.random_walk as random_walk
import algorithms.quantum_models.quantum_walk as quantum_walk_model
import globals.ui_interface as ui

def run_algorithm(algorithm_id,initial_pos,steps,trials):
    if steps <= 0 or trials <= 0 or steps == "Undefined" or trials == "Undefined":
        return(gc.algorithm_runner_id,["steps and trials should be positive integers"])
    else:
        if steps > abs(ui.initial_pos - ui.beginnig_vertex):
            print("Warning: There is more steps than distance between initial position "
                "and begin of line. If walker reaches the begin, it will stop at that "
                "position instead of crossing it.")
        if steps > abs(ui.ending_vertex - ui.initial_pos):
                print("Warning: There is more steps than distance between initial position "
                "and end of line. If walker reaches the end, it will stop at that "
                "position instead of crossing it.")
        match algorithm_id:
            case 1:
                alg.last_display_method = "Scatter"
                alg.last_result = random_walk.run_line(initial_pos,steps,trials,ui.beginnig_vertex,ui.ending_vertex)
                return(gc.algorithm_runner_id,["",True])
            case 2:
                alg.last_display_method = "Plot"
                alg.last_result = quantum_walk_model.solve_line(initial_pos,steps,trials,ui.beginnig_vertex,ui.ending_vertex)
                return(gc.algorithm_runner_id,["",True])
            case 3:
                return(gc.algorithm_runner_id,["Not implemented yet"])
            case _:
                return(gc.algorithm_runner_id,["Unknown Algorithm ID"])
    