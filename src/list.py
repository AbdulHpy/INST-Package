from getpass import getuser
import platform
import time
import toml
import os


class List():
    def __init__(self) -> None:
        self.PackageList()

    def PackageList(self):
        if platform.system() == "Windows":
            dirs = os.listdir(f"C:\\Users\\{getuser()}\\.dcpd\\apps")

            for dir in dirs:
                try:
                    f = open(
                        f"C:\\Users\\{getuser()}\\.dcpd\\apps\\{dir}\\dcpd.toml")
                    v = toml.load(f)
                    try:
                        print("Folder name: " + dir + ", Installed: " + time.ctime(os.path.getctime(
                            f"C:\\Users\\{getuser()}\\.dcpd\\apps\\{dir}")) + f" {v['package']['version']}")
                    except KeyError:
                        print("Folder name: " + dir + ", Installed: " + time.ctime(os.path.getctime(
                            f"C:\\Users\\{getuser()}\\.dcpd\\apps\\{dir}")))
                except FileNotFoundError:
                    print("Folder name: " + dir + ", Installed: " + time.ctime(os.path.getctime(
                        f"C:\\Users\\{getuser()}\\.dcpd\\apps\\{dir}")))
        elif platform.system() == "Darwin":
            dirs = os.listdir(f"/Users/{getuser()}/.dcpd/apps")

            for dir in dirs:
                try:
                    f = open(
                        f"/Users/{getuser()}/.dcpd/apps/{dir}/dcpd.toml")
                    v = toml.load(f)
                    try:
                        print("Folder name: " + dir + ", Installed: " + time.ctime(os.path.getctime(
                            f"/Users/{getuser()}/.dcpd/apps/{dir}")) + f" {v['package']['version']}")
                    except KeyError:
                        print("Folder name: " + dir + ", Installed: " + time.ctime(os.path.getctime(
                            f"/Users/{getuser()}/.dcpd/apps/{dir}")))
                except FileNotFoundError:
                    print("Folder name: " + dir + ", Installed: " + time.ctime(os.path.getctime(
                        f"/Users/{getuser()}/.dcpd/apps/{dir}")))
        elif platform.system() == "Linux":
            dirs = os.listdir(f"/home/{getuser()}/.dcpd/apps")

            for dir in dirs:
                try:
                    f = open(
                        f"/home/{getuser()}/.dcpd/apps/{dir}/dcpd.toml")
                    v = toml.load(f)
                    try:
                        print("Folder name: " + dir + ", Installed: " + time.ctime(os.path.getctime(
                            f"/home/{getuser()}/.dcpd/apps/{dir}")) + f" {v['package']['version']}")
                    except KeyError:
                        print("Folder name: " + dir + ", Installed: " + time.ctime(os.path.getctime(
                            f"/home/{getuser()}/.dcpd/apps/{dir}")))
                except FileNotFoundError:
                    print("Folder name: " + dir + ", Installed: " + time.ctime(os.path.getctime(
                        f"/home/{getuser()}/.dcpd/apps/{dir}")))
