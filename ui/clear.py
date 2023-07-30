import os
#Function for clearing console in Windows or Unix
def run():
    os.system('cls' if os.name=='nt' else 'clear')