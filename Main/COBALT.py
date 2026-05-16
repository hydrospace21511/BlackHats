import keyboard
from time import sleep
from colorama import Fore, Style, init
init(autoreset=True)
class COBALT:
    def __init__(self):
        pass

    def Start(self):
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
            while True:
                if keyboard.is_pressed('space'):
                    print(f"{Fore.GREEN}                              Starting COBALT...")
                    sleep(2)
                    break