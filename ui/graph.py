import globals.constants as gc
import globals.ui_interface as ui
import graphs.support as support

def display(message):
    print(message)
    print("1.Line")
    print("2.Print current config")
    print("3.Back to menu")
    choice = input()
    match choice:
        case "1":
            ui.graph_name = "Line"
            try:
                ui.initial_pos = int(input("Specify initial position : "))
                ui.beginnig_vertex = int(input("Specify beginnig of line : "))
                ui.ending_vertex = int(input("Specify end of line : "))
                if ui.ending_vertex <= ui.beginnig_vertex:
                    support.clear_graph()
                    return(gc.graph_creator_id,["End of line should be greater than begin"])
                elif ui.initial_pos not in range(ui.beginnig_vertex,ui.ending_vertex +1):
                    support.clear_graph()
                    return(gc.graph_creator_id,["Initial position should be between begin and end of line"])
                else:
                    ui.vertices = ui.ending_vertex - ui.beginnig_vertex + 1
                    ui.edges = ui.vertices - 1
                return(gc.graph_creator_id,["Press specified number for program behaviour"])
            except ValueError as e:
                support.clear_graph()
                return(gc.graph_creator_id,["Argument should be an integer"])
        case "2":
            return(gc.graph_creator_id,["Graph Name : " + ui.graph_name + "\n" +
                                        "Initial pos : " + str(ui.initial_pos) + "\n" + 
                                        "Begin of line : " + str(ui.beginnig_vertex) + "\n" + 
                                        "End of line : " + str(ui.ending_vertex) + "\n" +
                                        "Number of Vertices :" + str(ui.vertices) + "\n" +
                                        "Number of Edges :" + str(ui.edges) + "\n"])
        case "3":
            return(gc.menu_id,[""])
        case _:
            return(gc.graph_creator_id,["You selected bad option"])
            
