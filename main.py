import globals.constants as gc
import ui.menu as menu
import ui.instruction as instruction
import ui.clear as clear_console
import ui.graph as graph_creator
import ui.algorithm as algorithm_creator
import ui.runner as algorithm_runner
import ui.designer as diagram_designer
import ui.environment as quantum_env
import ui.jobs as jobs_loader
import algorithms.handler as handler

functions = [menu.display, instruction.display, graph_creator.display, algorithm_creator.display, 
             algorithm_runner.display, diagram_designer.display, handler.run_algorithm, quantum_env.display,
             jobs_loader.display]

if __name__ == "__main__":
    clear_console.run()
    print("Welcome in my tool to visualize behaviour of Quantum Walk. I hope you will find it useful :D \n " )
    (func_id,args) = menu.display( message="")
    while func_id != gc.quit_id: 
        try:
            clear_console.run()
            (func_id,args) = functions[func_id](*args)
        except Exception as e:
            print("Exception occur \n")
            print(e)
            func_id = gc.quit_id
    print("Bye ;) !")
