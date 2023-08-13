import globals.constants as gc
import globals.ui_interface as ui

def display(message,print_res):
    print(message)
    if print_res == True:
        ui.print_alg_results()
    print("1.Set number of iterations")
    print("2.Set number of trials")
    print("3.Specify Quantum Environment (only for quantum algorithms)")
    print("4.Print current config")
    print("5.Run Algorithm")
    print("6.Print results of the last algorithm")
    print("7.Back to menu")
    choice = input()
    match choice:
        case "1":
            input_iterations = input("Number of iterations :")
            try:
                ui.iterations = int(input_iterations)
            except ValueError as e:
                ui.iterations = 0
            if ui.iterations <= 0:
                return(gc.algorithm_runner_id,["Number of iterations should be positive integer"])
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
            return(gc.algorithm_runner_id,["Quantum part is not ready yet",False])
        case "4":
            return(gc.algorithm_runner_id,["Graph Name : " + ui.graph_name + "\n" +
                                        "Algorithm Name : " + str(ui.algorithm_name) + "\n" + 
                                        "Number of Iterations : " + str(ui.iterations) + "\n" + 
                                        "Number of Trials :" + str(ui.trials) + "\n",False])
        case "5": return(gc.run_algorithm_id,[ui.algorithm_id,ui.initial_pos,ui.iterations,ui.trials])
        case "6": return(gc.algorithm_runner_id,["",False])
        case "7":
            return(gc.menu_id,[""])
        case _:
            return(gc.algorithm_runner_id,["You selected bad option",False])