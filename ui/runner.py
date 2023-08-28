import globals.constants as gc
import globals.ui_interface as ui

def display(message,print_res):
    print(message)
    if print_res == True:
        ui.print_alg_results()
    print("1.Set number of steps")
    print("2.Set number of trials")
    print("3.Specify Quantum Environment (only for quantum algorithms)")
    print("4.Print current config")
    print("5.Run Algorithm")
    print("6.Print results of the last algorithm")
    print("7.Back to menu")
    choice = input()
    match choice:
        case "1":
            input_steps = input("Number of steps :")
            try:
                ui.steps = int(input_steps)
            except ValueError as e:
                ui.steps = 0
            if ui.steps <= 0:
                return(gc.algorithm_runner_id,["Number of steps should be positive integer"])
            return(gc.algorithm_runner_id,["",False])
        case "2":
            input_trials = input("Number of trials :")
            try:
                ui.trials = int(input_trials)
            except ValueError as e:
                ui.trials = 0 
            if ui.trials <= 0:
                return(gc.algorithm_runner_id,["Number of trials should be positive integer"])
            return(gc.algorithm_runner_id,["",False])
        case "3":
            return(gc.quantum_env_id,["Welcome in quantum environment specifier, press specified number for program behaviour"])
        case "4":
            return(gc.algorithm_runner_id,["Graph Name : " + ui.graph_name + "\n" +
                                        "Algorithm Name : " + str(ui.algorithm_name) + "\n" + 
                                        "Number of steps : " + str(ui.steps) + "\n" + 
                                        "Number of Trials :" + str(ui.trials) + "\n",False])
        case "5": return(gc.run_algorithm_id,[ui.algorithm_id,ui.initial_pos,ui.steps,ui.trials])
        case "6": return(gc.algorithm_runner_id,["",False])
        case "7":
            return(gc.menu_id,[""])
        case _:
            return(gc.algorithm_runner_id,["You selected bad option",False])