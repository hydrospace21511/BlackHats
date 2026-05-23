import os
import sys
from time import sleep
from colorama import Fore, Back, Style

class CorruptedHatsuneMikuClass:
    def __init__(self):
        self.raceName = "V#c%l0id"
        self.Integrity = 12250
        self.Regen = 0
        self.Defense = 99
        self.Attacks = {
            "Log Injection": 2007,
            "Chmod": 5000,
            "Negative Space": 10000,
            "Kill": 999999999999999999

        }
        self.Cooldowns = {
            "Log Injection": 1,
            "Chmod": 2,
            "Negative Space": 4,
            "Kill": 6
        }
        self.ui_color = Fore.RED

        #████████

    def trigger_negative_space(self):
        try:
            colunas, linhas = os.get_terminal_size()
        except OSError:
            os.system('cls' if os.name == 'nt' else 'clear')

        sys.stdout.write(Back.WHITE + (" " * colunas + "\n") * (linhas - 1) + " " * colunas)
        sys.stdout.flush()

        sleep(0.08) 


        os.system('cls' if os.name == 'nt' else 'clear')
        msg = " >> You Can't Escape From Me << "
        
        meio = linhas // 2
        
        for _ in range(meio):
            sys.stdout.write(Back.WHITE + " " * colunas + "\n")

        sys.stdout.write(Back.WHITE + Fore.BLACK + Style.BRIGHT + msg.center(colunas) + "\n")

        for _ in range(linhas - meio - 2):
            sys.stdout.write(Back.WHITE + " " * colunas + "\n")

        sys.stdout.write(Back.WHITE + " " * colunas)
        sys.stdout.flush()

        sleep(1.8) 

        print(Style.RESET_ALL, end="")
        os.system('cls' if os.name == 'nt' else 'clear')