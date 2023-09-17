import globals.constants as gc
import globals.alg_interface as alg
import algorithms.classical_algorithms.random_walk as random_walk
import algorithms.quantum_models.quantum_walk as quantum_walk_model
import algorithms.quantum_algorithms.quantum_walk as quantum_walk
import algorithms.quantum_models.coin as coin
import globals.ui_interface as ui
import algorithms.constants as ac
import json
import os

def run_algorithm(algorithm_id,initial_pos,steps,trials):
    if steps <= 0 or trials <= 0 or steps == "Undefined" or trials == "Undefined":
        return(gc.algorithm_runner_id,["steps and trials should be positive integers"])
    else:
        #TODO it is true for random walk 
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
                alg.last_display_method = "Plot"
                if alg.real_quantum == False:
                    alg.last_result, diff = quantum_walk.solve_line(initial_pos,steps,trials,ui.beginnig_vertex,ui.ending_vertex,
                                                                    False,"")
                    alg.last_result = ac.zero_pagg(alg.last_result,ui.beginnig_vertex,ui.ending_vertex,diff)
                    return(gc.algorithm_runner_id,["",True])
                else :
                    if len(bin(ui.ending_vertex - ui.beginnig_vertex)) -2 > 6:
                        return(gc.algorithm_runner_id,["You can use only 6 qubits for position",False])
                    else:
                        job_id = quantum_walk.solve_line(initial_pos,steps,trials,ui.beginnig_vertex,ui.ending_vertex,
                                                                    True,alg.ibm_token)
                        path = os.path.realpath(__file__)
                        dir = os.path.dirname(path)
                        dir = dir.replace("algorithms", "jobs")
                        try :
                            json_content = {}
                            dir = dir+"/quantum_jobs.json"
                            if os.path.exists(dir):
                                with open(dir, "r+", encoding='utf-8') as file:
                                    json_content = json.load(file)
                                    results = {
                                        "Type" : "Quantum Walk on a Line",
                                        "Job ID" : job_id,
                                        "Beginnig " : ui.beginnig_vertex,
                                        "Ending " : ui.ending_vertex,
                                        "Initial Pos" : initial_pos,
                                        "Initial Coin" : str(coin.state)
                                    }
                                    json_content["jobs"].append(results)
                                    file.seek(0)
                                    json.dump(json_content,file,indent = "")
                                    file.truncate()
                            else:
                                with open(dir, "w", encoding='utf-8') as file:
                                    results = {
                                        "jobs" : [{
                                            "Type" : "Quantum Walk on a Line",
                                            "Job ID" : job_id,
                                            "Beginnig " : ui.beginnig_vertex,
                                            "Ending " : ui.ending_vertex,
                                            "Initial Pos" : initial_pos,
                                            "Initial Coin" : str(coin.state)
                                        }]
                                    }
                                    json.dump(results,file,indent = "")
                            return(gc.algorithm_runner_id,["Your job ID is :" + job_id + "  \n" 
                                                       "ID was save in jobs/quantum_jobs.json \n" 
                                                       "You have to wait in before get result, check Jobs in Quantum Lab"
                                                       ,False])
                        except Exception as e:
                            return(gc.algorithm_runner_id,["Your job ID is :" + job_id + "  \n" 
                                                       "ID was save in jobs/quantum_jobs.json \n" 
                                                       "You have to wait in before get result, check Jobs in Quantum Lab \n" +
                                                       "But during saving job locally ID you got " + str(e) + "\n"
                                                       "So please copy your ID, (or get from IBM Quantum Lab)" 
                                                       ,False])

            case _:
                return(gc.algorithm_runner_id,["Unknown Algorithm ID"])
    