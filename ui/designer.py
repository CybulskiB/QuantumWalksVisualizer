import globals.constants as gc
def display(message):
    print(message)
    print("1.Back to menu")
    choice = input()[0]
    match choice:
        case "1":
            return(gc.menu_id,[""])
        case _:
            return(gc.diagram_designer_id,["You selected bad option"])