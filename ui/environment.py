import globals.constants as gc
import globals.ui_interface as ui
import algorithms.quantum_models.coin as coin


def display(message):
    print(message)
    print("1.Set coin to |0>")
    print("2.Set coin to |1>")
    print("3.Print coin state")
    print("4.Back to Algorithm Runner")
    choice = input()
    match choice:
        case "1":
            coin.set(0)
            return(gc.quantum_env_id,["You set coin to |0>"])
        case "2":
            coin.set(1)
            return(gc.quantum_env_id,["You set coin to |1>"])
        case "3":
            state_str = str(coin.state)
            return(gc.quantum_env_id,[state_str])
        case "4":
            return(gc.algorithm_runner_id,["",False])
        case _:
            return(gc.quantum_env_id,["You selected bad option"])