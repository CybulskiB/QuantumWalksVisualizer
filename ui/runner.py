import globals.constants as gc
def display(message):
    print(message)
    print("1.Back to menu")
    choice = input()[0]
    match choice:
        case "1":
            return(gc.menu_id,[""])
        case _:
            return(gc.algorithm_runner_id,["You selected bad option"])