import globals.constants as gc
import globals.ui_interface as ui
#Data for graph - im using dynamic typing in python


def display(message):
    print(message)
    print("1.Infinite line")
    print("2.Print current config")
    print("3.Back to menu")
    choice = input()
    match choice:
        case "1":
            ui.graph_name = "Infinite line"
            ui.initial_pos = 0
            ui.isFinite = False
            ui.vertices = float('inf')
            ui.edges = float('inf')
            return(gc.graph_creator_id,["Press specified number for program behaviour"])
        case "2":
            return(gc.graph_creator_id,["Graph Name : " + ui.graph_name + "\n" +
                                        "Initial pos : " + str(ui.initial_pos) + "\n" + 
                                        "Is Finite? : " + str(ui.isFinite) + "\n" + 
                                        "Number of Vertices :" + str(ui.vertices) + "\n" +
                                        "Number of Edges :" + str(ui.edges) + "\n"])
        case "3":
            return(gc.menu_id,[""])
        case _:
            return(gc.graph_creator_id,["You selected bad option"])
            
