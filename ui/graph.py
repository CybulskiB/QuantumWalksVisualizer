import globals.constants as gc
#Data for graph - im using dynamic typing in python
graph_name = "Undefined"
initial_pos = "Undefined"
isFinite = "Undefined"
vertices = "Undefined"
edges = "Undefined"


def display(message):
    global graph_name,initial_pos,isFinite,vertices,edges
    print(message)
    print("1.Infinite line")
    print("2.Print current config")
    print("3.Back to menu")
    choice = input()[0]
    match choice:
        case "1":
            graph_name = "Infinite line"
            initial_pos = 0
            isFinite = False
            vertices = float('inf')
            edges = float('-inf')
            return(gc.graph_creator_id,["Press specified number for program behaviour"])
        case "2":
            return(gc.graph_creator_id,["Graph Name : " + graph_name + "\n" +
                                        "Initial pos : " + str(initial_pos) + "\n" + 
                                        "Is Finite? : " + str(isFinite) + "\n" + 
                                        "Number of Vertices :" + str(vertices) + "\n" +
                                        "Number of Edges :" + str(edges) + "\n"])
        case "3":
            return(gc.menu_id,[""])
        case _:
            return(gc.graph_creator_id,["You selected bad option"])
def get_info():
    return(graph_name,initial_pos,isFinite,vertices,edges)
            
