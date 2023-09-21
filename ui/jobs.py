import globals.constants as gc
import globals.alg_interface as alg
from  qiskit_ibm_provider import *
import algorithms.constants as ac
import globals.ui_interface as ui
import json
import os

def display(message):
    print(message)
    print("1.Load job ID from file")
    print("2.Set ID manually")
    print("3.Print ID of last job")
    print("4.Load results from ID")
    print("5.Back to diagram designer")
    choice = input()
    match choice:
        case "1":
            try:
                file_path = os.path.realpath(__file__)
                json_path = os.path.dirname(file_path)
                json_path = json_path.replace("ui", "jobs")
                json_path = json_path+"/quantum_jobs.json"
                data = {}
                with open(json_path, "r",encoding='utf-8') as json_file:
                    data = json.load( json_file)
                    iteration = 1
                    for job in data.get("jobs", []):
                        job_id = job.get("Job ID", "")
                        type = job.get("Type", "")
                        print(f"{iteration}. Job ID: {job_id}, Type: {type}")
                        iteration +=1
                    choosen_job = input("Wchich Job you want to load?")
                    try:
                        choosen_job = int(choosen_job)
                        if choosen_job > iteration or choosen_job <= 0:
                            return(gc.jobs_loader_id,["You should specify number from list"])
                        else:
                            alg.lasy_job_id = data.get("jobs", [])[choosen_job - 1]["Job ID"]
                            ui.beginnig_vertex = int(data.get("jobs", [])[choosen_job - 1]["Beginnig "])
                            ui.ending_vertex = int(data.get("jobs", [])[choosen_job - 1]["Ending "])
                            ui.difference = int(data.get("jobs", [])[choosen_job - 1]["Difference"])
                            return(gc.jobs_loader_id,["You choose:" + str(alg.lasy_job_id)])
                    except ValueError as e:
                        return(gc.jobs_loader_id,["You should specify number from list"])
            except json.JSONDecodeError as e:
                return(gc.jobs_loader_id,["Error during reading json, make sure you have quantum_jobs.json file in jobs directory"])
        case "2":
            alg.lasy_job_id = input("Print Job ID")
            return(gc.jobs_loader_id,[""])
        case "3":
            return(gc.jobs_loader_id, ["Last job ID is : " + str(alg.lasy_job_id)]) 
        case "4":
            if alg.lasy_job_id != "":
                try:
                    path = os.path.realpath(__file__)
                    dir = os.path.dirname(path)
                    dir = dir.replace("ui", "credentials")
                    with open(dir + "/.pswd", "r") as file:
                        alg.ibm_token = file.read()
                        IBMProvider.save_account(alg.ibm_token, overwrite=True)
                        provider = IBMProvider()
                        job = provider.retrieve_job(alg.lasy_job_id)
                        result = job.result()
                        counts = result.get_counts()
                        alg.last_result = counts
                        alg.last_result = ac.zero_pagg(alg.last_result,ui.beginnig_vertex,ui.ending_vertex,ui.difference)
                        alg.last_display_method = "Plot"
                        return(gc.jobs_loader_id["Results was sucessfully loaded"])
                except Exception as e:
                    return(gc.jobs_loader_id,[" Can't log in to IBM account, make sure you put your token in .pwd file in" 
                                            " credentials directory"])
            else:
                return(gc.jobs_loader_id,["You have to set job ID first"])
        case "5":
            return(gc.diagram_designer_id,[""])
        case _:
            return(gc.jobs_loader_id,["You selected bad option"])