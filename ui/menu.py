import globals.constants as gc

#Main for User Interface
def display( message):
    if message != "":
        print(message)
    #Available commands + welcome for first startup
    print("Press specified number for program behaviour \n")
    print("1.Instruction \n")
    print("2.Go to Graph Creator \n")
    print("3.Go to Algorithm Creator \n")
    print("4.Go to Algorithm Runner \n")
    print("5.Go to Diagram Designer \n")
    print("6.Quit")
    #Reading command selected by user and running it
    choice = input("Select Option: ")
    match choice:
        case "1":
            return (gc.instruction_id,[])
        case "2":
            return (gc.graph_creator_id,["Welcome in graph creator, press specified number for program behaviour"])
        case "3":
            return (gc.algorithm_creator_id,["Welcome in algorithm creator, press specified number for program behaviour"])
        case "4":
            return (gc.algorithm_runner_id,["Welcome in algorithm runner, press specified number for program behaviour",False])
        case "5":
            return (gc.diagram_designer_id,["Welcome in diagram designer, press specified number for program behaviour"])
        case "6":
            return (gc.quit_id,[])
        case _:
            return (gc.menu_id,["You selected bad option"])