import argparse
import os

class Base():
    def __init__(self, *args, **kwargs):
        print("Started app")
        
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', help="Gives me your name")


    args = parser.parse_args()

    print("Your name is {}" .format(args.name))


if __name__ == "__main__":
    Base()

