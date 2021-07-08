import argparse
from utils import downloader

class BaseParse():
    def __init__(self, *args, **kwargs):
        self.ParseIt()


    def ParseIt(self):
        parser = argparse.ArgumentParser(prog='dcpd')
        parser.add_argument(
                '-c', '--config', help='Configure dcpd', action='store_true')
        passed = parser.parse_args()

        if passed.config:
            print("Works")
        else:
            try:
                downloader.Download()
            except FileNotFoundError as e:
                parser.print_help()
                print(e)
            except Exception as e:
                print(f"{e}")




if __name__ == "__main__":
    BaseParse()
