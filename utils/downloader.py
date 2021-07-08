# Created on Arch Linux author is Cairo (DevCairo)

import os
import toml
import pycurl
import getpass
import platform
from colorama import Fore
from . import installer


class Download:
    def __init__(self, *args, **kwargs):
        self.conn = pycurl.Curl()
        self.eb = "[" + Fore.RED + " ERR " + Fore.RESET + "] "
        self.ob = "[" + Fore.GREEN + " OK " + Fore.RESET + "] "
        self.Download()

    def Download(self):
        """Reads the file and downloads and follows instructions"""
        f = open(f"{os.getcwd()}/dcpd.toml")
        d = toml.load(f)
        if platform.system() == "Windows":
            print(self.ob + "Running some checks..")

        elif platform.system() == "Linux":
            if os.path.isdir(f"/home/abdul/{getpass.getuser()}/.dcpd/apps/{d['package']['name']}"):
                print(self.ob + "You already have that package installed!")
            else:
                with open(f"{os.getcwd()}/dcpd.toml", "r") as f:
                    print(f.read())
                    ask = input("Install? [Y|n]$ ")
                    if ask == "":
                        print(self.ob + "Installing")
                        if d["package"]["method"] == "curl":
                            installer.InstallCurl(d["package"]["link"])
                    elif ask.lower() == "y":
                        print(self.ob + "Installing")
                    elif ask.lower() == "n":
                        print(self.eb + "Aborting")
                        return
                    else:
                        print(self.eb + f"Unknown option " + Fore.RED + f"{ask}" + Fore.RESET)
                        return