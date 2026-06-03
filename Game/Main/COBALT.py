import os
import sys
from time import sleep
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_key():
    if os.name == 'nt':
        import msvcrt
        key = msvcrt.getch()
        if key == b'\xe0': 
            special = msvcrt.getch()
            if special == b'H': return 'UP'
            if special == b'P': return 'DOWN'
        elif key in (b'\r', b'\n'):
            return 'ENTER'
        return None
    else:
        import tty, termios
        fd = sys.stdin.fileno()         #ISSO TUDO É POR CAUSA DO SUPORTE DE LINUX, ME AGRADEÇAM (eu q to usando linux)
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            if ch == '\x1b': 
                ch2 = sys.stdin.read(1)
                if ch2 == '[':
                    ch3 = sys.stdin.read(1)
                    if ch3 == 'A': return 'UP'
                    if ch3 == 'B': return 'DOWN'
            elif ch in ('\r', '\n'):
                return 'ENTER'
            return None
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


class COBALT:
    def __init__(self):
        self.options = ["Play", "Help", "Exit"]

    def _print_menu(self, selected_idx):
        clear()
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

        for i, option in enumerate(self.options):
            if i == selected_idx:
                print(f"                                    {Fore.GREEN}>> {option} <<")
            else:
                print(f"                                       {option} ")
        print()

    def _Load_Menu(self):
        for i in range(1, 4):
            clear()
            self._print_menu(0) 
            print(f"{Fore.GREEN}                                  Starting COBALT" + ("." * i))
            sleep(0.5)
        print(f"\n{Fore.GREEN}                          Access Granted >> System Starting")
        sleep(2)

    def start(self):
        current_selection = 0

        while True:
            self._print_menu(current_selection)

            key = get_key()

            if key == 'UP':
                current_selection = (current_selection - 1) % len(self.options)
            elif key == 'DOWN':
                current_selection = (current_selection + 1) % len(self.options) #deveria ter feito isso pra seleção de classe ne?
            elif key == 'ENTER':
                if current_selection == 0:    # jugar
                    self._Load_Menu()
                    break 
                    
                elif current_selection == 1:  # ayuda
                    clear()
                    print(f"{Fore.GREEN} Accessing COBALT Help System...\n [DarkHats Updater é lindo]")
                    sleep(5)
                    
                elif current_selection == 2:  # salir (é salir msm? sla, corrige ai quem tiver lendo dps KKKKKKKKKKKKKKKKKKKKKKK)
                    clear()
                    print(f"{Fore.GREEN} Shutting down COBALT...")
                    sleep(2)
                    sys.exit()

#game = COBALT()
#game.start() #eita porra, funciono mesmo KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK (vou criar um backup do antigo pra vcs ver a bomba q era, pq to falando vcs sendo q provavelmente vc vai ta lendo solo? seco seco)