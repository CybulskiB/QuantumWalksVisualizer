import globals.constants as gc

algorithm_name = "Undefined"
algorithm_id = "Undefined"

def display(message):
    global algorithm_name, algorithm_id
    print(message)
    print("1.Discrete Random Walk")
    print("2.Discrete Quantum Walk")
    print("3.Print Current Algorithm")
    print("4.Back to menu")
    choice = input()[0]
    match choice:
        case "1":
            algorithm_name = "Discrete Random Walk"
            algorithm_id =  gc.discrete_random_walk_id
            return (gc.algorithm_creator_id,["Press specified number for program behaviour"])
        case "2": 
            algorithm_name = "Discrete Quantum Walk"
            algorithm_id = gc.discrete_quantum_walk_id
            return (gc.algorithm_creator_id,["Press specified number for program behaviour"])
        case "3":
            return (gc.algorithm_creator_id,["Algorithm Name : " + str(algorithm_name) + "\n"
                                             "Algorithm ID : " + str(algorithm_id)])
        case "4":
            return(gc.menu_id,[""])
        case _:
            return(gc.graph_creator_id,["You selected bad option"])
