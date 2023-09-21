import globals.constants as gc
import globals.ui_interface as ui
import matplotlib.pyplot as plt
import globals.alg_interface as alg

#List of dictionaries to draw
plots = []

def display(message):
    print(message)
    print("1.Show current diagram")
    print("2.Show latest algorithm result")
    print("3.Add latest algorithm to diagram")
    print("4.Load result from Quantum Lab")
    print("5.Back to menu")
    choice = input()
    match choice:
        case "1":
            plt.title("Diagram from Designer")
            for plot in plots:
                if plot[2] == "Plot":
                    plt.plot(list(plot[0].keys()),list(plot[0].values()),label=plot[1])
                else:
                    plt.scatter(list(plot[0].keys()),list(plot[0].values()),label=plot[1])
            plt.xlabel("Positions")
            plt.ylabel("Frequency")
            plt.legend()
            plt.show()
            return(gc.diagram_designer_id,[""])
        case "2":
            ui.print_alg_results()
            return(gc.diagram_designer_id,[""])
        case "3":
            name = input("Specify series name")
            plots.append((alg.last_result,name,alg.last_display_method))
            return(gc.diagram_designer_id,[""])
        case "4":
            return(gc.jobs_loader_id,["Welcome in graph creator, press specified number for program behaviour"])
        case "5":
            return(gc.menu_id,[""])
        case _:
            return(gc.diagram_designer_id,["You selected bad option"])