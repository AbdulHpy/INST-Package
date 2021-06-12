"""
          downloader
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Copyright (c) 2021-present DevCairo
LICENSE GPL v2.0, view LICENSE for
more details
"""

from getpass import getuser
from git import Git
import platform
import os


class Download():
    def __init__(self, f) -> None:
        self.RCI(f)

    # Read, clone, install

    def RCI(self, f):
        try:
            if platform.system() == "Windows":
                path = f"C:\\Users\\{getuser()}\\.dcpd\\apps"
                try:
                    if os.path.isdir(path):
                        # "Git" ready for cloning ( pun intended :) )
                        repo = Git(path)
                        repo.clone(f["package"]["link"])  # Clone
                        print(
                            f'[ OK ] Cloned {f["package"]["name"]} version: {f["package"]["version"]}')
                    else:
                        # if the path does not exist then write make it
                        os.mkdir(path)
                        repo = Git(path)
                        repo.clone(f["package"]["link"])
                        print(
                            f'[ OK ] Cloned {f["package"]["name"]} version: {f["package"]["version"]}')
                except Exception as e:
                    print(f"[ ERR ] {e} ")
            elif platform.system() == "Linux":
                path = f"/home/{getuser()}/.dcpd/apps"
                try:
                    if os.path.isdir(path):
                        repo = Git(path)
                        repo.clone(f["package"]["link"])
                        print(
                            f'[ OK ] Cloned {f["package"]["name"]} version: {f["package"]["version"]}')
                    else:
                        os.mkdir(path)
                        repo = Git(path)
                        repo.clone(f["package"]["link"])
                        print(
                            f'[ OK ] Cloned {f["package"]["name"]} version: {f["package"]["version"]}')
                except Exception as e:
                    print(f"[ ERR ] {e}")
            elif platform.system() == "Darwin":
                path = f"/Users/{getuser()}/.dcpd/apps"
                try:
                    if os.path.isdir(path):
                        repo = Git(path)
                        repo.clone(f["package"]["link"])
                        print(
                            f'[ OK ] Cloned {f["package"]["name"]} version: {f["package"]["version"]}')
                    else:
                        os.mkdir(path)
                        repo = Git(path)
                        repo.clone(f["package"]["link"])
                        print(
                            f'[ OK ] Cloned {f["package"]["name"]} version: {f["package"]["version"]}')
                except Exception as e:
                    print(f"[ ERR ] {e}")

        except Exception as e:
            print(f"[ ERR ] {e}")
