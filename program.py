from zipfile import ZIP_DEFLATED, ZipFile
import shutil
import platform
import argparse
import requests
import getpass
import os
import io


class colors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


class Program():
    def __init__(self, *args, **kwargs):
        try:
            os.environ["PROGRAMFILES(X86)"]
            arch = "x64"
        except:
            arch = "x32"
        url = "https://pkg.devcairo.xyz/version"
        version = 2021.1
        resp = requests.get(url=url)
        data = resp.json()
        if data["Version"] > version:
            ask = input("[ INFO ] DCPD Version 2021.1 is available, would you like to update? (Y/N) Default is Y. >> ")
            if ask.lower() == "y":
                try:
                    if platform.system() == "Windows":
                        try:
                            url = f"https://pkg.devcairo.xyz/version/windows/dcpd{arch}.zip"
                            r = requests.get(url)
                            if r.ok:
                                print(f"[ OK ] Downloading dcpd{arch}.zip...")
                                z = ZipFile(io.BytesIO(r.content))
                                z.extractall(f'C:\\Users\\{getpass.getuser()}\\dcpd')
                                print(f"[ OK ] Installed DCPD version {data['Version']}")
                            elif r.status_code == 404:
                                print("[ ERR ] Application not found! Please create an issue so the developers know.")
                        except Exception as e:
                            print(f"[ ERR ] {e}")
                except Exception as e:
                    print(f"[ ERR ] {e}")
            elif ask.lower() == "n":
                pass
            elif ask == "":
                print("Updating")
        
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--add', type=str, metavar='', dest='add',
                        help="Install a package from github")
    parser.add_argument(
        '-r', '--remove', help="Remove a package from your system")
    args = parser.parse_args()

    if args.add:
        zipfile = args.add
        try:
            os.environ["PROGRAMFILES(X86)"]
            arch = "x64"
        except:
            arch = "x32"
        if platform.system() == "Darwin":
            try:
                path = f'/Users/{getpass.getuser()}/dcpd/{zipfile}'
                if os.path.exists(path):
                    print("[ ERR ] Program already installed! Did you mean remove?")
                else:
                    url = f"https://mirrors.devcairo.xyz/macos/{zipfile}.zip"
                    r = requests.get(url)
                    if r.ok:
                        print("[ OK ] Connected to mirrors.devcairo.xyz!")
                        print("[ OK ] Retrieved important information..")
                        print("[ OK ] Beginning downloads...")
                        os.chdir(f'/Users/{getpass.getuser()}')
                        z = ZipFile(io.BytesIO(r.content))
                        newdir = os.mkdir(f'/Users/{getpass.getuser()}/dcpd/{zipfile}')
                        z.extractall(f'/Users/{getpass.getuser()}/dcpd/{zipfile}')
                        print(f"[ OK ] Installed {zipfile}")
                    elif r.status_code == 404:
                        print(  "[ ERR ] Application not found")
            except Exception as e:
               print( f"[ ERR ] {e}")
        elif platform.system() == "Windows":
            try:
                path = f"C:\\Users\\{getpass.getuser()}\\dcpd\\{zipfile}"
                if os.path.exists(path):
                    print("[ ERR ] Program already installed! Did you mean remove?")
                else:
                    url = f"https://mirrors.devcairo.xyz/windows/{arch}/{zipfile}.zip"
                    r = requests.get(url)
                    if r.ok:
                        print("[ OK ] Connected to mirrors.devcairo.xyz!")
                        print("[ OK ] Retrieved important information..")
                        print("[ OK ] Beginning download...")
                        os.chdir(f'C:\\Users\\{getpass.getuser()}\\dcpd')
                        z = ZipFile(io.BytesIO(r.content))
                        newdir = os.mkdir(f'C:\\Users\\{getpass.getuser()}\\dcpd\\{zipfile}')
                        z.extractall(f'C:\\Users\\{getpass.getuser()}\\dcpd\\{zipfile}')
                        print(f"[ OK ] Installed {zipfile}")
                    elif r.status_code == 404:
                        print(  "[ ERR ] Application not found")
            except Exception as e:
                print( f"[ ERR ] {e}")
        elif platform.system() == "Linux":
            try:
                path = f"/home/{getpass.getuser()}/dcpd/{zipfile}"
                if os.path.exists(path):
                    print( "[ ERR ] Application not found")
                else:
                    url = f"https://mirrors.devcairo.xyz/linux/{arch}/{zipfile}.zip"
                    r = requests.get(url)
                    if r.ok:
                        print("[ OK ] Connected to mirrors.devcairo.xyz!")
                        print("[ OK ] Retrieved important information..")
                        print("[ OK ] Beginning downloads...")
                        os.chdir(f'/home/{getpass.getuser()}')
                        z = ZipFile(io.BytesIO(r.content))
                        newdir = os.mkdir(f'/home/{getpass.getuser()}/dcpd/{zipfile}')
                        z.extractall(f'/home/{getpass.getuser()}/dcpd/{zipfile}')
                        print(f"[ OK ] Installed {zipfile}")
                    elif r.status_code == 404:
                        print( "[ ERR ] Application not found")
            except Exception as e:
                print( f"[ ERR ] {e}")
    elif args.remove:
        folder = args.remove
        if platform.system() == "Windows":
            path = f"C:\\Users\\{getpass.getuser()}\\dcpd\\{folder}"
            if os.path.exists(path):
                try:
                    print("[ OK ] Application found!")
                    print("[ WARN ] Removing directory..")
                    shutil.rmtree(f'C:\\Users\\{getpass.getuser()}\\dcpd\\{folder}')
                    print(f"[ OK ] Uninstalled {folder}")
                except Exception as e:
                    print( f"[ ERR ] {e}")
            else:
                print(  "[ ERR ] The application doesn't exist!")
        elif platform.system() == "Darwin":
            path = f"/Users/{getpass.getuser()}/dcpd/{folder}"
            if os.path.exists(path):
                try:
                    print("[ OK ] Application found!")
                    print("[ WARN ] Removing directory..")
                    shutil.rmtree(f"/Users/{getpass.getuser()}/dcpd/{folder}")
                    print(f"[ OK ] Uninstalled {folder}" )
                except Exception as e:
                    print( f"[ ERR ] {e}")
            else:
                print("[ ERR ] The application doesn't exist!")
        elif platform.system() == "Linux":
            path = f"/home/{getpass.getuser()}/dcpd/{folder}"
            if os.path.exists(path):
                try:
                    print("[ OK ] Application found!")
                    print("[ WARN ] Removing directory..")
                    shutil.rmtree(f"/home/{getpass.getuser()}/dcpd/{folder}")
                    print(f"[ OK ] Uninstalled {folder}")
                except Exception as e:
                    print( f"[ ERR ] {e}")
            else:
                print( "[ ERR ] The application doesn't exist!")

if __name__ == "__main__":
    Program()
