import matplotlib.pyplot as plt
import globals.alg_interface as alg
#Shared data between UI options

#Components from Graph Creator
graph_name = "Undefined"
initial_pos = "Undefined"
isFinite = "Undefined"
vertices = "Undefined"
edges = "Undefined"

#Components from Algorithm Creator
algorithm_name = "Undefined"
algorithm_id = "Undefined"

#Components from Algorithm Runner
iterations = 0
trials = 0 

#Function for printing results

def print_alg_results():
    if alg.last_result != None:
        plt.title(algorithm_name)
        plt.scatter(list(alg.last_result.keys()),list(alg.last_result.values()))
        plt.xlabel("Positions")
        plt.ylabel("Frequency")
        plt.show()
        input("Press any key to continue")