from time import sleep
from colorama import Fore, Style, init
import os
import sys
from Game.Main.Color import cText
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
init(autoreset=True)
class COBALT:
    def __init__(self):
        pass

    def _print_menu(self):
            print(f"""{Fore.GREEN}
            ╔══════════════════════════════════════════════════════════╗
            ║                                                          ║
            ║         ____             _    _   _       _              ║
            ║        |  _ \  __ _ _ __| | _| | | | __ _| |_ ___        ║
            ║        | | | |/ _` | '__| |/ / |_| |/ _` | __/ __|       ║
            ║        | |_| | (_| | |  |   <|  _  | (_| | |_\__ \       ║
            ║        |____/ \__,_|_|  |_|\_\_| |_|\__,_|\__|___/       ║
            ║                                                          ║
            ║            > SYSTEM BOOT SEQUENCE INITIATED...           ║
            ║                                                          ║
            ║                  [ PRESS SPACE TO HACK ]                 ║
            ║                                                          ║
            ╚══════════════════════════════════════════════════════════╝
            """)

    
    def _Load_Menu(self):
        i = 0
        while True:
            print(f"{Fore.GREEN}                                  Starting COBALT.")
            sleep(0.5)
            clear()
            self._print_menu()
            print(f"{Fore.GREEN}                                  Starting COBALT..")
            sleep(0.5)
            clear()
            self._print_menu()
            print(f"{Fore.GREEN}                                  Starting COBALT...")
            sleep(0.5)
            clear()
            self._print_menu()
            i += 1
            if i == 3:
                cText("                          Access Granted >> System Starting", "green")
                sleep(2)
                break
        sleep(2)  

    def _wait_for_space(self):
        if os.name == 'nt':
            import msvcrt
            print(f"{Fore.GREEN}Press SPACE to hack...")
            while True:
                if msvcrt.kbhit() and msvcrt.getch() == b' ':
                    break
        else:
            try:
                import tty
                import termios
            except ImportError:
                input(f"{Fore.GREEN}Press SPACE then ENTER to hack...")
                return

            print(f"{Fore.GREEN}Press SPACE to hack...")
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setcbreak(fd)
                while True:
                    ch = sys.stdin.read(1)
                    if ch == ' ':
                        break
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    def _Start(self):
        self._print_menu()
        self._wait_for_space()
        self._Load_Menu()
        sleep(0.05)
            
                 

