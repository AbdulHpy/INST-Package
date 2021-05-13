from zipfile import ZIP_DEFLATED, ZipFile
import platform
import argparse
import requests
import getpass
import os
import io


class Base():
    def __init__(self, *args, **kwargs):
        pass

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
            url = f"https://mirrors.devcairo.xyz/macos/{zipfile}.zip"
            try:
                url = f"https://mirrors.devcairo.xyz/macos/{zipfile}.zip"
                r = requests.get(url)
                if r.ok:
                    print("[ OK ] Connected to mirrors.devcairo.xyz and beginning download!")
                    os.chdir(f'/Users/{getpass.getuser()}')
                    z = ZipFile(io.BytesIO(r.content))
                    newdir = os.mkdir(f'/Users/{getpass.getuser()}/dcpd/{zipfile}')
                    z.extractall(f'/Users/{getpass.getuser()}/dcpd/{zipfile}')
            except Exception as e:
                print(f"[ ERR ] {e}")
        elif platform.system() == "Windows":
            try:
                url = f"https://mirrors.devcairo.xyz/windows/{arch}/{zipfile}.zip"
                r = requests.get(url)
                if r.ok:
                    print("[ OK ] Connected to mirrors.devcairo.xyz and beginning download!")
                    os.chdir(f'C:\\Users\\{getpass.getuser()}\\dcpd')
                    z = ZipFile(io.BytesIO(r.content))
                    newdir = os.mkdir(f'C:\\Users\\{getpass.getuser()}\\dcpd\\{zipfile}')
                    z.extractall(f'C:\\Users\\{getpass.getuser()}\\dcpd\\{zipfile}')
            except Exception as e:
                print(f"[ ERR ] {e}")
        elif platform.system() == "Linux":
            url = f"https://mirrors.devcairo.xyz/linux/{arch}/{zipfile}.zip"
            try:
                url = f"https://mirrors.devcairo.xyz/linux/{arch}/{zipfile}.zip"
                r = requests.get(url)
                if r.ok:
                    print("[ OK ] Connected to mirrors.devcairo.xyz and beginning download!")
                    os.chdir(f'/home/{getpass.getuser()}')
                    z = ZipFile(io.BytesIO(r.content))
                    newdir = os.mkdir(f'/home/{getpass.getuser()}/dcpd/{zipfile}')
                    z.extractall(f'/home/{getpass.getuser()}/dcpd/{zipfile}')
            except Exception as e:
                print(f"[ ERR ] {e}")
        print("Retrieved important information..\nBeginning download ✔️")

if __name__ == "__main__":
    Base()
