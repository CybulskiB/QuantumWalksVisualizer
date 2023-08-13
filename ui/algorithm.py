import globals.constants as gc
import globals.ui_interface as ui

#TODO for now both algorithms have Coin with probability 0.5 to left and 0.5 to right 
# That should be more general, user should have possibility to set Coin and runner should use that coin for algorithm 

def display(message):
    print(message)
    print("1.Discrete Random Walk (with p = 0.5)")
    print("2.Discrete Quantum Walk (with p = 0.5)")
    print("3.Print Current Algorithm")
    print("4.Back to menu")
    choice = input()
    match choice:
        case "1":
            ui.algorithm_name = "Discrete Random Walk"
            ui.algorithm_id =  gc.discrete_random_walk_id
            return (gc.algorithm_creator_id,["Press specified number for program behaviour"])
        case "2": 
            ui.algorithm_name = "Discrete Quantum Walk"
            ui.algorithm_id = gc.discrete_quantum_walk_id
            return (gc.algorithm_creator_id,["Press specified number for program behaviour"])
        case "3":
            return (gc.algorithm_creator_id,["Algorithm Name : " + str(ui.algorithm_name) + "\n"
                                             "Algorithm ID : " + str(ui.algorithm_id)])
        case "4":
            return(gc.menu_id,[""])
        case _:
            return(gc.graph_creator_id,["You selected bad option"])
