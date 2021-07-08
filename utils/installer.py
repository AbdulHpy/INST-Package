from colorama import Fore
import platform
import certifi
import getpass
import pycurl
import toml
import git
import sys
import os



class InstallCurl():
    def __init__(self, link=None):
        """
        A way to install through curl.

        Args:
            link (str): The link of the package
        """
        self.eb = "[" + Fore.RED + " ERR " + Fore.RESET + "] "
        self.ob = "[" + Fore.GREEN + " OK " + Fore.RESET + "] "
        if link == None:
            print(self.eb + "The package you have attempted to instal!")
        self.install(link)
        


    def install(self, link=None):
        """
        A way to install through curl.

        Args:
            link (str): The link of the package
        """
        f = open(f'{os.getcwd()}/dcpd.toml')
        d = toml.load(f)
        try:
            # Most of this code is copied from stack overflow
            # https://stackoverflow.com/questions/13775892/pause-and-resume-downloading-with-pycurl
            c = pycurl.Curl() # Initialize curl
            c.setopt(pycurl.URL, link) # Load link
            c.setopt(c.CAINFO, certifi.where()) # HTTPS only
            c.setopt(pycurl.FOLLOWLOCATION, 2) # Set max load links
            c.setopt(pycurl.MAXREDIRS, 10) # Max amount of redirects
            filename = link.split("/")[-1].strip()
            f = open(filename, "wb")
            c.setopt(pycurl.WRITEDATA, f)
            try:
                c.perform()
            except Exception as e:
                print(self.eb + "")
            if platform.system() == "Linux":
                try:
                    os.mkdir(f"/home/{getpass.getuser()}/.dcpd/apps/")
                    os.system(f"mv {filename} /home/{getpass.getuser()}/.dcpd/apps/")
                except FileExistsError:
                    print(self.eb + f"You already have {d['package']['name']} installed!")
            elif platform.system() == "Windows":
                os.mkdir(f"C:/Users/{getpass.getuser()}/.dcpd/apps/{d['package']['name']}")

            print(self.ob + "Finished installing program")
        except Exception as e:
            print(self.eb + f"{e}")
        
        
