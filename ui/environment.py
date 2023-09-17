import globals.constants as gc
import globals.ui_interface as ui
import algorithms.quantum_models.coin as coin
import globals.alg_interface as alg
import os

def display(message):
    print(message)
    print("1.Set coin to |0>")
    print("2.Set coin to |1>")
    print("3.Print coin state")
    print("4.Switch to real quantum computer (only 6 qubits for line)")
    print("5.Switch to simulator")
    print("6.Back to Algorithm Runner")
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
            try:
                path = os.path.realpath(__file__)
                dir = os.path.dirname(path)
                dir = dir.replace("ui", "credentials")
                with open(dir + "/.pswd", "r") as file:
                    alg.ibm_token = file.read()
                    alg.real_quantum = True
                    return(gc.quantum_env_id,["Switched to real quantum"])
            except Exception as e:
                print(e)
                return(gc.quantum_env_id,[ str(e) + "  \n can't switch to real quantum, make sure you put your token in .pwd file in" 
                                         " credentials directory"])
        case "5":
            alg.real_quantum = False
            return(gc.quantum_env_id,["Switched to simulator"])
        case "6":
            return(gc.algorithm_runner_id,["",False])
        case _:
            return(gc.quantum_env_id,["You selected bad option"])