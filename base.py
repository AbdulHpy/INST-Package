from zipfile import ZIP_DEFLATED, ZipFile
from platform import system
from urllib import request
import argparse
import requests
import os


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
            repo = args.add
            try:
                os.environ["PROGRAMFILES(X86)"]
                arch = "x64"
            except:
                arch = "x32"
            if system() == "Windows":
                url = f"https://mirrors.devcairo.xyz/windows/{arch}/{repo}.zip"
                file = requests.get(url)
                zipf = ZipFile(file, 'r')
                ff = zipf.namelist()[0]
                deff = zipf.open(ff)
                content = deff.read()
            elif system() == "Darwin":
                url = f"https://mirrors.devcairo.xyz/macos/{repo}.zip"
                file = requests.get(url)
                zipf = ZipFile(file, 'r')
                ff = zipf.namelist()[0]
                deff = zipf.open(ff)
                content = deff.read()
            elif system() == "Linux":
                url = f"https://mirrors.devcairo.xyz/linux/{arch}/repo.zip"
                file = requests.get(url)
                zipf = ZipFile(file, 'r')
                ff = zipf.namelist()[0]
                deff = zipf.open(ff)
                content = deff.read()
                zipf.close()

            


if __name__ == "__main__":
    Base()
