"""
            reader
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Copyright (c) 2021-present DevCairo
LICENSE GPL v2.0, view LICENSE for
more details
"""

import downloader
import toml
import os


class ReadProcess():
    def __init__(self) -> None:
        self.TomlRead()

    def TomlRead(self):
        cwd = os.getcwd()  # Go to the directory where the code is being executed
        f = open(f"{cwd}/dcpd.toml")
        repo = toml.load(f)  # Read the dcpd.toml file
        downloader.Download(repo)
        try:
            # Can be multiple instructions just like JSON
            for instruction in repo["package"]["instructions"]:
                print(f'==> {instruction}')
                # Compile the code, say something, make a directory, etc
                os.system(instruction)
        except KeyError:
            pass
        except toml.TomlDecodeError:
            print(f"[ ERR ] You mama'd your last mia")
