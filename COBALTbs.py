import keyboard
from time import sleep
import os
from colorama import Fore, Style, init
import threading

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
init(autoreset=True)

class COBALT:
    def __init__(self):
        pass

    def _ScreenMenu(self):
            print(f"""{Fore.GREEN}
        ╔══════════════════════════════════════════════════════════╗
        ║                                                          ║
        ║{Fore.GREEN}        ____             _    _   _       _           {Fore.GREEN}    ║
        ║{Fore.GREEN}       |  _ \  __ _ _ __| | _| | | | __ _| |_ ___     {Fore.GREEN}    ║
        ║{Fore.GREEN}       | | | |/ _` | '__| |/ / |_| |/ _` | __/ __|    {Fore.GREEN}    ║
        ║{Fore.GREEN}       | |_| | (_| | |  |   <|  _  | (_| | |_\__ \    {Fore.GREEN}    ║
        ║{Fore.GREEN}       |____/ \__,_|_|  |_|\_\_| |_|\__,_|\__|___/    {Fore.GREEN}    ║
        ║                                                          ║
        ║{Fore.GREEN}            > SYSTEM BOOT SEQUENCE INITIATED...           {Fore.GREEN}║
        ║                                                          ║
        ║{Fore.GREEN}                  [ PRESS SPACE TO HACK ]               {Fore.GREEN}  ║
        ║                                                          ║
        ╚══════════════════════════════════════════════════════════╝
            """)
    
    def _LoadCobalt(self):
         for _ in [".", "..", "..."]:
              print(f"\033[1A\033[2K", end="")
              print(f"\n\n{Fore.GREEN}{'                              Starting COBALT' + _:^68}\n")
              sleep(0.4)
    clear()

    def Start(self):
         clear()
         self._ScreenMenu()
         while True:
            if keyboard.is_pressed('space'):
                 print(f"\n{Fore.GREEN}{'':^68}")
                 loader = threading.Thread(target=self._LoadCobalt)
                 loader.start()
                 loader.join()
                 break
            sleep(0.05)