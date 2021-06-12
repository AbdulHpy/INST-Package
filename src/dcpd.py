"""
              app
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Copyright (c) 2021-present DevCairo
LICENSE GPL v2.0, view LICENSE for
more details
"""

from toml import TomlDecodeError
from random import randint
import platform
import argparse
import remover
import reader
import list
import os


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="dcpd")
    parser.add_argument(
        '-r', '--remove', help="Remove a package from your system")  # Option to remove a program
    parser.add_argument(
        '-l', '--list', help="List all the packages", action='store_true')
    parser.add_argument(
        '-c', '--config', help="launch the config file", action='store_true')
    arg = parser.parse_args()
    if arg.remove:
        remover.Remove(arg.remove)
    elif arg.list:
        list.List()
    elif arg.config:
        try:
            if platform.system() == "Windows":
                os.system("powershell -Command ..\configuration.exe")
            elif platform.system() == "Linux":
                os.system("../configuration")
            elif platform.system() == "Darwin":
                os.system("../configuration")
        except Exception as e:
            print("[ ERR ] {e}")
    else:
        try:
            reader.ReadProcess()
        except TomlDecodeError:
            x = randint(0, 1000)
            if x > 932:
                print("[ ERR ] Damn bro you made a spelling mistake")
            else:
                print("[ ERR ] Failed to decode TOML file")
