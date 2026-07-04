from Game.Main.COBALT import COBALT, COBALT_FS
from colorama import init

init(autoreset=True)


def main():
    sistema = COBALT()
    explorer = COBALT_FS()
    explorer.run()
    sistema.start()


if __name__ == "__main__":
    main()
