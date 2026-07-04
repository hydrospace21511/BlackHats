import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from Game.Main.COBALT import COBALT, COBALT_FS
from colorama import init

init(autoreset=True)


def main():
    sistema = COBALT()
    #sistema._check_space()
    explorer = COBALT_FS()
    explorer.run()
    sistema.start()


if __name__ == "__main__":
    main()

