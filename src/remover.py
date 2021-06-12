"""
            remover
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Copyright (c) 2021-present DevCairo
LICENSE GPL v2.0, view LICENSE for
more details
"""

from getpass import getuser
import platform
import git
import os


class Remove():
    def __init__(self, app) -> None:
        self.RemoveApp(app)  # Run the function

    def RemoveApp(self, app):
        try:
            if platform.system() == "Windows":
                try:
                    # Check if the directory of the app exists
                    if os.path.isdir(f"C:\\Users\\{getuser()}\\.dcpd\\apps\\{app}"):
                        # Removes the entire directory
                        git.rmtree(
                            f"C:\\Users\\{getuser()}\\.dcpd\\apps\\{app}")
                        print(f"[ OK ] Removed {app}")
                    else:
                        print(f"[ ERR ] You don't have {app} installed!")
                except Exception as e:
                    print(f"[ ERR ] {e}")
            elif platform.system() == "Linux":
                try:
                    if os.path.isdir(f"/home/.dcpd/apps/{app}"):
                        git.rmtree(f"/home/.dcpd/apps/{app}")
                        print(f"[ OK ] Removed {app}")
                    else:
                        print(f"[ ERR ] You don't have {app} installed!")
                except Exception as e:
                    print(f"[ ERR ] {e}")
            elif platform.system() == "Darwin":
                try:
                    if os.path.isdir(f"/Users/{getuser()}/.dcpd/apps/{app}"):
                        git.rmtree(f"/Users/.dcpd/apps/{app}")
                        print(f"[ OK ] Removed {app}")
                    else:
                        print(f"[ ERR ] You don't have {app} installed!")
                except Exception as e:
                    print(f"[ ERR ] {e}")
        except Exception as e:
            print(f"[ ERR ] {e}")
