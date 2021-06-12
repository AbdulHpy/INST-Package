from getpass import getuser
from random import randint
from src.list import List
import platform
import shutil
import toml
import time
import git
import os

print(
    """                
 ____    ____  ____   ____  
|  _ \  / ___||  _ \ |  _ \ 
| | | || |    | |_) || | | |
| |_| || |___ |  __/ | |_| |
|____/  \____||_|    |____/                                                
""")

print("(1) Install dcpd\n(2) Remove dcpd\n(3) Reinstall dcpd\n(4) Update dcpd or packages\n(5) Repair dcpd\n(6) Abort\n ===> Default is (1)")
answer = input(">>> ")

answers = ["1", "3", ""]
if answer in answers:
    try:
        if platform.system() == "Windows":
            path = f"C:\\Users\\{getuser()}\\.dcpd\\dcpd"
            try:
                if os.path.isdir(path):
                    print("[ OK ] Reinstalling dcpd")
                    git.rmtree(f"C:\\Users\\{getuser()}\\.dcpd\\dcpd")
                    repo = git.Git(f"C:\\Users\\{getuser()}\\.dcpd")
                    repo.clone("https://github.com/DevCairo/dcpd")
                    print("[ OK ] Reinstalled dcpd!")
                    print(
                        "[ WARN ] If dcpd isn't added to path you might not be able to run it")
                else:
                    os.mkdir(f"C:\\Users\\{getuser()}\\.dcpd")
                    repo = git.Git(f"C:\\Users\\{getuser()}\\.dcpd")
                    repo.clone("https://github.com/DevCairo/dcpd")
                    print("[ OK ] Installed dcpd!")
                    print(
                        "[ WARN ] If dcpd isn't added to path you might not be able to run it")
            except Exception as e:
                print(f"[ ERR ] {e}")
        elif platform.system() == "Linux":
            path = f"/home/{getuser()}/.dcpd/dcpd"
            try:
                if os.path.isdir(path):
                    print("[ OK ] Reinstalling dcpd")
                    git.rmtree(f"/home/{getuser()}/.dcpd/dcpd")
                    repo = git.Git(f"/home/{getuser()}/.dcpd")
                    repo.clone("https://github.com/DevCairo/dcpd")
                    print("[ OK ] Reinstalled dcpd!")
                    print(
                        "[ WARN ] If dcpd isn't added to path you might not be able to run it")
                else:
                    os.mkdir(f"/home/{getuser()}/.dcpd/dcpd")
                    repo = git.Git(f"/home/{getuser()}/.dcpd")
                    repo.clone("https://github.com/DevCairo/dcpd")
                    print("[ OK ] Installed dcpd!")
                    print(
                        "[ WARN ] If dcpd isn't added to path you might not be able to run it")
            except Exception as e:
                print(f"[ ERR ] {e}")
        elif platform.system() == "Darwin":
            path = f"/Users/{getuser()}/.dcpd/dcpd"
            try:
                if os.path.isdir(path):
                    print("[ OK ] Reinstalling dcpd")
                    git.rmtree(f"/Users/{getuser()}/.dcpd/dcpd")
                    repo = git.Git(f"/Users/{getuser()}/.dcpd")
                    repo.clone("https://github.com/DevCairo/dcpd")
                    print("[ OK ] Reinstalled dcpd!")
                    print(
                        "[ WARN ] If dcpd isn't added to path you might not be able to run it")
                else:
                    os.mkdir(f"/Users/{getuser()}/.dcpd/dcpd")
                    repo = git.Git(f"/Users/{getuser()}/.dcpd")
                    repo.clone("https://github.com/DevCairo/dcpd")
                    print("[ OK ] Installed dcpd!")
                    print(
                        "[ WARN ] If dcpd isn't added to path you might not be able to run it")
            except Exception as e:
                print(f"[ ERR ] {e}")
    except Exception as e:
        print(f"[ ERR ] {e}")

elif answer == "2":
    try:
        if platform.system() == "Windows":
            path = f"C:\\Users\\{getuser()}\\.dcpd\\dcpd"
            if os.path.isdir(path):
                git.rmtree(f"C:\\Users\\{getuser()}\\.dcpd\\dcpd")
                shutil.rmtree(f"C:\\Users\\{getuser()}\\.dcpd")
                print("[ OK ] Removed dcpd from your computer :(")
            else:
                x = randint(0, 1000)
                if x > 932:
                    print("[ ERR ] Are you a magician?")
                else:
                    print(
                        "[ ERR ] I'm not installed but this script is somehow running")
        elif platform.system() == "Darwin":
            path = f"/Users/{getuser()}/.dcpd/dcpd"
            if os.path.isdir(path):
                git.rmtree(f"/Users/{getuser()}/.dcpd/dcpd")
                shutil.rmtree(f"/Users/{getuser()}/.dcpd")
                print("[ OK ] Removed dcpd from your computer :(")
            else:
                x = randint(0, 1000)
                if x > 932:
                    print("[ ERR ] Are you a magician?")
                else:
                    print(
                        "[ ERR ] I'm not installed but this script is somehow running")
        elif platform.system() == "Linux":
            path = f"/home/{getuser()}/.dcpd/dcpd"
            if os.path.isdir(path):
                git.rmtree(f"/home/{getuser()}/.dcpd/dcpd")
                shutil.rmtree(f"/home/{getuser()}/.dcpd")
                print("[ OK ] Removed dcpd from your computer :(")
            else:
                x = randint(0, 1000)
                if x > 932:
                    print("[ ERR ] Are you a magician?")
                else:
                    print(
                        "[ ERR ] I'm not installed but this script is somehow running")
    except Exception as e:
        print(f"[ ERR ] {e}")
elif answer == "4":
    try:
        if platform.system() == "Windows":
            f = open(f"C:\\Users\\{getuser()}\\.dcpd\\dcpd\\dcpd.toml")
            conf = toml.load(f)
            List()
            print(f"Main program: dcpd, Install: " + time.ctime(os.path.getctime(
                            f"C:\\Users\\{getuser()}\\.dcpd\\dcpd")) + f"{conf['package']['version']}")
            app = input("Enter program name (Default is dcpd) >> ")
            defaults = ["dcpd", ""]
            if app in defaults:
                f = open(f"C:\\Users\\{getuser()}\\.dcpd\\dcpd\\dcpd.toml")
                v = toml.load(f)
                git.cmd.Git().pull('https://github.com/DevCairo/dcpd')
                print(f"[ OK ] Updated dcpd to {v['package']['version']}")
            else:
                if os.path.isdir(f"C:\\Users\\{getuser()}\\.dcpd\\apps\\{app}"):    
                    try:      
                        f = open(f"C:\\Users\\{getuser()}\\.dcpd\\apps\\{app}\\dcpd.toml")
                        v = toml.load(f)
                        repo = git.Repo(f"C:\\Users\\{getuser()}\\.dcpd\\apps\\{app}")
                        git.cmd.Git().pull()
                        print(f"[ OK ] Updated {app} to {v['package']['version']}")
                    except FileNotFoundError:
                        repo = git.Repo(f"C:\\Users\\{getuser()}\\.dcpd\\apps\\{app}")
                        git.cmd.Git().pull()
                        print(f"[ OK ] Updated {app}")
        elif platform.system() == "Linux":
            pass
        elif platform.system() == "Darwin":
            pass
    except Exception as e:
        print(f"[ ERR ] {e}")
elif answer == "5":
    YN = input(
        "[ WARN ] Repairing will reinstall dcpd but won't remove apps, do you want to continue? [Y/n] ")
    try:
        answers = ["y", "yes", "yeah", ""]
        if YN.lower() in answers:
            try:
                if platform.system() == "Windows":
                    git.rmtree(f"C:\\Users\\{getuser()}\\.dcpd\\dcpd")
                    repo = git.Git(f"C:\\Users\\{getuser()}\\.dcpd")
                    repo.clone("https://github.com/DevCairo/dcpd")
                    print("[ OK ] Repaired dcpd")
                elif platform.system() == "Linux":
                    git.rmtree(f"/home/{getuser()}/.dcpd/dcpd")
                    repo = git.Git(f"/home/{getuser()}/.dcpd")
                    repo.clone("https://github.com/DevCairo/dcpd")
                    print("[ OK ] Repaired dcpd")
                elif platform.system() == "Darwin":
                    git.rmtree(f"/Users/{getuser()}/.dcpd/dcpd")
                    repo = git.Git(f"/Users/{getuser()}/.dcpd")
                    repo.clone("https://github.com/DevCairo/dcpd")
                    print("[ OK ] Repaired dcpd")
                else:
                    print("[ ERR ] Something went wrong")
            except Exception as e:
                print(f"[ ERR ] {e}")
    except Exception as e:
        print(f"[ ERR ] {e}")
elif answer == "6":
    print("[ OK ] Exiting")
