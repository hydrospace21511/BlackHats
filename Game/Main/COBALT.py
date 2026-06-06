import os
import sys
from time import sleep
from colorama import Fore, Style, init
import getpass
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
        elif key== b' ':
            return 'SPACE'
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
            elif ch == ' ':
                return 'SPACE'
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
            print(f"{Fore.GREEN}                                 Starting COBALT" + ("." * i))
            sleep(0.5)
        print(f"\n{Fore.GREEN}                         Access Granted >> System Starting")
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

    def _neofetch(self):
        clear()
        #ta linha por linha pq poor algum motivo as 3 aspa la nn tava funcionando e tava retornando erro
        DarkHat_raw = [
            r"                                     .--.                                  ",
            r"                      .-------.   .-+*%%*+----.                            ",
            r"                     -*%%%%%%%*+-+*%%%%%%%%%%%*+--.                        ",
            r"                    .*%%%%%%%%%%%%%%%%%%%%%%%%%%%%*+--.                    ",
            r"                    +%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*+.                  ",
            r"                   -*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*#                 ",
            r"                  .*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@* ",
            r"                  +%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+                ",
            r"                 .*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*.               ",
            r"                @.*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+               ",
            r"                @@.+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*.              ",
            r"      .------- @@@@@.+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+              ",
            r"   .-+*%%%%%%%-@@@@@@@.-+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*:             ",
            r" @+*%%%%%%%%%%+@@@@@@@@@@.-=*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%-             ",
            r" @%%%%%%%%%%%%*+:@@@@@@@@@@@----+*%%%%%%%%%%%%%%%%%%%%%%%%%%*.             ",
            r"@@%%%%%%%%%%%%%%*-@@@@@@@@@@@@@@@.----+*%%%%%%%%%%%%%%%%%*+-.@@ .          ",
            r" +%%%%%%%%%%%%%%%*+.@@@@@@@@@@@@@@@@@@@.-----------------.@@@@@-*+-.       ",
            r" .*%%%%%%%%%%%%%%%%*+-.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-%%%*+.     ",
            r"  .+*%%%%%%%%%%%%%%%%%*+-.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+%%%%%*+.   ",
            r"    @@@%%%%%%%%%%%%%%%%%%*+--.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.+*%%%%%%%*-  ",
            r"      @+*%%%%%%%%%%%%%%%%%%%%*+----.@@@@@@@@@@@@@@@@@@@@@@@:+*%%%%%%%%%%*- ",
            r"        .+*%%%%%%%%%%%%%%%%%%%%%%%%*+---------------------+#%%%%%%%%%%%%%*.",
            r"          .-+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*.",
            r"             .-+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+ ",
            r"                .--+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*. ",
            r"                    .--+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*-  ",
            r"                        .---+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*+.   ",
            r"                             .----+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*+-.     ",
            r"                                   .-------+*%%%%%%%%%%%%%%*+-----         ",
            r"                                            .--------------:               "
        ]

        DarkHat = [line.ljust(75) for line in DarkHat_raw]
        
        #infos
        C_GREEN = Fore.GREEN
        C_WHITE = Fore.WHITE
        C_CYAN = Fore.CYAN

        info_sis = [  
            f"{C_GREEN}DarkHats@{getpass.getuser()}{Style.RESET_ALL}", 
            f"{C_WHITE}---------------------------------------{Style.RESET_ALL}",
            "",
            f"{C_GREEN}OS:{C_WHITE}         Cobalt OS (Fedora Edition) x86_64", 
            "",
            f"{C_GREEN}Host:{C_WHITE}       COBALT Terminal v1.0.0",
            "",
            f"{C_GREEN}Kernel:{C_WHITE}     6.5.0-secure-core",
            "",
            f"{C_GREEN}Uptime:{C_WHITE}     2 hours, 31 minutes",
            "",
            f"{C_GREEN}Packages:{C_WHITE}   2400 (rpm)",
            "",
            f"{C_GREEN}Shell:{C_WHITE}      bash 5.1.8",
            "",
            f"{C_GREEN}Resolution:{C_WHITE} 1920x1080",
            "",
            f"{C_GREEN}Terminal:{C_WHITE}   cobalt-term",
            "",
            f"{C_GREEN}CPU:{C_WHITE}        Cobalt Core X-12 (8/24) 4.200GHz 120W",
            "",
            f"{C_GREEN}Memory:{C_WHITE}     7266MiB / 32768MiB",
            "", "", "", "", 
            f"            {C_CYAN}[ PRESS SPACE TO BOOT ]{Style.RESET_ALL}", 
        ]

        max_lenght = max(len(DarkHat), len(info_sis))
        #acho q o certo seria length soq enfim, é a quantidade de linhas do neofetch, pra garantir q o loop vai ler todas as linhas
        #print("\n" * 4) 
        
        for i in range(max_lenght):
            l_l = DarkHat[i] if i < len(DarkHat) else " " * 75
            l_r = info_sis[i] if i < len(info_sis) else ""
            
            print(f"  {Fore.GREEN}{l_l}{Style.RESET_ALL}        {l_r}")
        
        #print("\n" * 3)    

    def _terminal_loading(self):
        
        clear()
        
        tasks = [
            "Starting subsystems...",
            "Verifying integrity of Cobalt Core X-12...",
            "Loading DarkHats modules...",
            "Mounting encrypted directories...",
            "Establishing secure connection..."
        ]
        
        extra_tasks = [
            "Restarting subsystems...",
            "Activating security protocols...",
            "Synchronizing with the DarkHats Cloud...",
            "Finalizing environment configuration...",
            "Initializing Hydro protocol..."
        ]

        for task in tasks:
           
            for i in range(11):  
                percent = i * 10
                bar = "▓" * i + "░" * (10 - i)
               
                print(f"{Fore.GREEN}  [{bar}] {percent}% | {task}", end='\r')
                sleep(0.15)
            print() 

        print(f"\n{Fore.GREEN}  [!] Synchronization complete. Starting interface....")
        sleep(3)
        clear()
        print(f"\n{Fore.RED}  [!] Error: Interface not found. Starting recovery protocol...")
        sleep(3)
        for e_task in extra_tasks:
           
            for i in range(11):  
                percent = i * 10
                bar = "▓" * i + "░" * (10 - i)
               
                print(f"{Fore.GREEN}  [{bar}] {percent}% | {e_task}", end='\r')
                sleep(0.15)
            print()

        print(f"\n{Fore.GREEN}  [!] Success: Interface recovered. Starting COBALT...")  
        sleep(3)     
        clear()  

    def _check_space(self):
        while True:
            self._neofetch()
            key = get_key()
            if key == 'SPACE':
                break
            else:
                continue
        self._terminal_loading()
        #isso seria consideraro criar um OS do 0? porém extremamente limitado?

class COBALT_FS:
    def __init__(self):
        self.files = [
            {"name": "darkhats.flat", "type": "EXEC", "icon": "📂", "color": Fore.WHITE},
            {"name": "notes.txt",     "type": "FILE", "icon": "📄", "color": Fore.WHITE},
            {"name": "logs.db",       "type": "FILE", "icon": "📄", "color": Fore.WHITE},
            {"name": "shutdown",      "type": "EXIT", "icon": " ⏻",  "color": Fore.RED},
        ]
        self.cursor = 0
        self.inner_w = 80

    def draw(self):
        clear()
        
        C_BORDA = Fore.GREEN 
        C_TITULO = Fore.GREEN
        
        print(f"{C_BORDA}╔{'═' * self.inner_w}╗")
        
        title = " ■ COBALT FILE EXPLORER"
        print(f"{C_BORDA}║{C_TITULO}{title.ljust(self.inner_w)}{C_BORDA}║")

        print(f"{C_BORDA}╠{'═' * self.inner_w}╣")
        
        for i, f in enumerate(self.files):
            is_selected = (i == self.cursor)
            
            arrow = "►" if is_selected else " "
            text_color = Fore.GREEN if is_selected else f['color']
            
            item_string = f" {arrow} {f['icon']} {f['name']}"

            emoji_offset = 1 if f['icon'] in ["📂", "📄"] else 0
            
            largura_visual = len(item_string) + emoji_offset
            espaco = " " * (self.inner_w - largura_visual)
     
            print(f"{C_BORDA}║{text_color}{item_string}{espaco}{C_BORDA}║")
            
        print(f"{C_BORDA}╠{'═' * self.inner_w}╣")
        
        status = f" Status: {len(self.files)} items"
        print(f"{C_BORDA}║{Fore.LIGHTBLACK_EX}{status.ljust(self.inner_w)}{C_BORDA}║")

        print(f"{C_BORDA}╚{'═' * self.inner_w}╝{Style.RESET_ALL}")

        print(f"\n  {Fore.LIGHTBLACK_EX}[ ARROWS: Navigate | ENTER: Select ]{Style.RESET_ALL}")
        
    def run(self):
        while True:
            self.draw()
            key = get_key()
            
            if key == 'UP':
                self.cursor = (self.cursor - 1) % len(self.files)
            elif key == 'DOWN':
                self.cursor = (self.cursor + 1) % len(self.files)
            elif key == 'ENTER':
                self.handle_action(self.files[self.cursor])

        clear()
    def handle_action(self, file):
        nome = file['name']
        
        if nome == "darkhats.flat":
            self._abrir_darkhats()
            
        elif nome == "notes.txt":
            self._abrir_notas()
            
        elif nome == "logs.db":
            self._abrir_logs()
            
        elif nome == "shutdown":
            clear()
            print(f"{Fore.RED}[!] Shutting down COBALT OS...{Style.RESET_ALL}")
            sleep(1.5)
            sys.exit()
    def _abrir_tela(self):
        print("tonotedio")
    def _abrir_darkhats(self):
        clear()
        print(f"{Fore.CYAN}[*] Extracting darkhats.flat...{Style.RESET_ALL}")
        sleep(1)
        print(f"{Fore.GREEN}[*] Root permissions granted.{Style.RESET_ALL}")
        sleep(1)

        boot = COBALT()
        boot.start()

        from Game.Main.DarkHatsGame import DarkHatsGame
        game = DarkHatsGame()
        game.start()
        clear()
        print(f"{Fore.YELLOW}[!] darkhats.flat finished. Returning to COBALT...{Style.RESET_ALL}")
        sleep(2)

    def _abrir_notas(self):
        clear()
        print(f"{Fore.WHITE}╔════════════════════════════════════════════╗")
        print(f"║ {Fore.WHITE}📝 TEXT VISUALIZER: notes.txt{Fore.WHITE}              ║")
        print(f"╠════════════════════════════════════════════╣")
        print(f"║ {Fore.WHITE}Lembrete para a equipe DarkHats:  {Fore.WHITE}         ║")
        print(f"║ {Fore.WHITE}Hydro é lindo                           {Fore.WHITE}   ║")
        print(f"║ {Fore.WHITE}Preciso de um café                      {Fore.WHITE}   ║")
        print(f"║ {Fore.WHITE}DarkHats Updater é lindo                {Fore.WHITE}   ║")
        print(f"║ {Fore.WHITE}- Admin{Fore.WHITE}                                    ║")
        print(f"╚════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        input(f"\n  {Fore.WHITE}[ Press ENTER to exit ]{Style.RESET_ALL}")

    def _abrir_logs(self):
 
        clear()
        print(f"{Fore.YELLOW}[!] OPENING logs.db...{Style.RESET_ALL}")
        sleep(0.5)
        
        for _ in range(15):
            lixo = os.urandom(30).hex() #vulgo thalles
            print(f"{Fore.RED}ERR: ENCRYPTED BLOCK >> {lixo}{Style.RESET_ALL}")
            sleep(0.05)
            
        print(f"\n{Fore.RED}[ ACCESS DENIED: ENCRYPTION KEY NOT FOUND ]{Style.RESET_ALL}")
        input(f"\n  {Fore.LIGHTBLACK_EX}[ Press ENTER to return ]{Style.RESET_ALL}")

def Explorer():
    clear()
    COBALT_FS().run()
# explorer = COBALT_FS()
# explorer.run()
# game = COBALT()
#game.start() #eita porra, funciono mesmo KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK (vou criar um backup do antigo pra vcs ver a bomba q era, pq to falando vcs sendo q provavelmente vc vai ta lendo solo? seco seco)