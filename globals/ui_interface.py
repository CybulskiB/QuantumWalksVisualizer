import matplotlib.pyplot as plt
import globals.alg_interface as alg
#Shared data between UI options

#Components from Graph Creator
graph_name = "Undefined"
initial_pos = "Undefined"
vertices = "Undefined"
beginnig_vertex = "Undefined"
ending_vertex = "Undefined"
edges = "Undefined"

#Components from Algorithm Creator
algorithm_name = "Undefined"
algorithm_id = "Undefined"

#Components from Algorithm Runner
steps = 0
trials = 0 
#Function for printing results

def print_alg_results():
    if alg.last_result != None and alg.last_display_method != None:
        plt.title(algorithm_name)
        if alg.last_display_method == "Plot":
            plt.plot(list(alg.last_result.keys()),list(alg.last_result.values()))
        else:
            plt.scatter(list(alg.last_result.keys()),list(alg.last_result.values()))
        plt.xlabel("Positions")
        plt.ylabel("Frequency")
        plt.show()
        input("Press any key to continue")