import os
import json
import asyncio
import site
from colorama import Fore
import time
from alive_progress import alive_bar




def compute():
    for i in range(1):
        time.sleep(.1)
        yield



bs = input("Run an INST command (help, install) ")
if bs == "install":
    try:
        m = open("configuration/config.json")
        dat = json.load(m)
        if dat["coloredText"] == "True":
            file = input(Fore.LIGHTBLUE_EX +
                         f"Enter a file name like main{dat['ReadFileType']}: " + Fore.RESET)
            print(Fore.RESET + "Proceeding.." + Fore.RESET)
        #with alive_bar(1) as bar:
            #for i in compute():
                #bar()
            if file.endswith(dat['ReadFileType']):
                try:
                    dirs = os.getcwd()
                    f = open(file)
                    data = json.load(f)
                    for i in data['packages']:
                        try:
                            o = data['type']
                            os.system(f"{o} install {i}")
                        except json.JSONDecodeError:
                            print(Fore.YELLOW +
                                  "Error decoding .inst file" + Fore.RESET)
                    print(Fore.RESET + "Finishing up and cleaning up.." + Fore.RESET)
                    with alive_bar(1) as bar:
                        for i in compute():
                            bar()

            # whatever
                except KeyboardInterrupt:
                    print(Fore.YELLOW + "\n⚠ Terminating program" + Fore.RESET)
                    print(Fore.RESET)
            else:
                try:
                    print(Fore.YELLOW +
                          f'NOT A {dat["ReadFileType"]} FILE!' + Fore.RESET)
                    print(Fore.RESET)
                except KeyboardInterrupt:
                    print(Fore.YELLOW + "\n⚠ Terminating program" + Fore.RESET)
                    print(Fore.RESET)
        elif dat["coloredText"] == "False":
            file = input(F"Enter a file name like main.inst: ")
        #with alive_bar(1) as bar:
            #for i in compute():
            #bar()
            if file.endswith(dat['ReadFileType']):
                try:
                    dirs = os.getcwd(dat['ReadFileType'])
                    f = open(file)
                    data = json.load(f)
                    for i in data['packages']:
                        try:
                            o = data['type']
                            os.system(f"{o} install {i}")
                        except json.JSONDecodeError:
                            print("Error decoding .inst file")
                    print("Finishing up and cleaning up..")
                    with alive_bar(1) as bar:
                        for i in compute():
                            bar()

            # whatever
                except KeyboardInterrupt:
                    print("\n⚠ Terminating program")
            else:
                try:
                    print(f'NOT A {dat["ReadFileType"]} FILE!')
                except KeyboardInterrupt:
                    print("\n⚠ Terminating program")
    except KeyboardInterrupt:
        print("\n⚠ Terminating program")



elif file == None:
    try:
        print("COMMANDS\n-help\n-install")
    except KeyboardInterrupt:
        print("\n⚠ Terminating program")
elif file == "help":
    try:
        print("COMMANDS\n-help\n-install")
    except KeyboardInterrupt:
        print("\n⚠ Terminating program")





