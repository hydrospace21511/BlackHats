import os
import sys
from Color import cText
import re
import json
import unicodedata
from rich.console import Console, Group
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.live import Live
from rich.spinner import Spinner
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from time import sleep
from colorama import Fore, Style, init
import getpass
from typewriter import typewriter
from typewriter import text
import Game.Main.Player as PlayerStats
from Game.Main.RouteManager import RouteManager, EndingManager

def get_char_width(char):
    cat = unicodedata.category(char)
    if cat in ('Mn', 'Me', 'Cf', 'Cc'):
        return 0
    
    eaw = unicodedata.east_asian_width(char)
    if eaw in ('W', 'F'):
        return 2
    
    return 1

def strip_ansi(s):
    return re.sub(r'\x1b\[[0-9;]*[mK]', '', s)

def visual_width(s):
    clean_s = strip_ansi(s)
    return sum(get_char_width(c) for c in clean_s)


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
                    break
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
            f"{C_GREEN}Tempo de ativação:{C_WHITE}     2 horas, 31 minutos",
            "",
            f"{C_GREEN}Packages:{C_WHITE}   2400 (rpm)",
            "",
            f"{C_GREEN}Shell:{C_WHITE}      bash 5.1.8",
            "",
            f"{C_GREEN}Resolução:{C_WHITE} 1920x1080",
            "",
            f"{C_GREEN}Terminal:{C_WHITE}   cobalt-term",
            "",
            f"{C_GREEN}CPU:{C_WHITE}        Cobalt Core X-12 (8/24) 4.200GHz 120W",
            "",
            f"{C_GREEN}Memória:{C_WHITE}     7266MiB / 32768MiB",
            "", "", "", "", 
            f"            {C_CYAN}[ PRESSIONE ESPAÇO PARA DAR BOOT ]{Style.RESET_ALL}", 
        ]

        max_lenght = max(len(DarkHat), len(info_sis))
        #acho q o certo seria length soq enfim, é a quantidade de linhas do neofetch, pra garantir q o loop vai ler todas as linhas
        #print("\n" * 4) 
        
        for i in range(max_lenght):
            l_l = DarkHat[i] if i < len(DarkHat) else " " * 75
            l_r = info_sis[i] if i < len(info_sis) else ""
            
            print(f"  {Fore.GREEN}{l_l}{Style.RESET_ALL}        {l_r}")
        
        #print("\n" * 3)    

    def _welcome_screen(self):
        console = Console()
        user_name = getpass.getuser().upper()

        ascii_art = (
            " ____________________________________________\n"
            " __  ____/_  __ \\__  __ )__    |__  /___  __/\n"
            " _  /    _  / / /_  __  |_  /| |_  / __  /   \n"
            " / /___  / /_/ /_  /_/ /_  ___ |  /___  /    \n"
            " \\____/  \\____/ /_____/ /_/  |_/_____/_/     "
        )

        top_text = Text() 
        top_text.append(ascii_art, style="bold green")
        
        centered_top = Align.center(top_text)

        top_text.append("\n\n           B E M - V I N D O\n", style="bold white")
        top_text.append(f"             Usuario: {user_name}\n\n", style="dim green")

        clear()

        spinner = Spinner("dots", text="[green]Preparando o ambiente COBALT...", style="bold green")
        
        with Live(console=console, refresh_per_second=20) as live:
            for _ in range(75):
                content_loading = Group(
                    top_text,
                    Align.center(spinner),
                    Text("\n\n") 
                )
                panel_loading = Panel(
                    content_loading,
                    border_style="green",
                    padding=(3, 16),
                    title="[bold green]System Boot[/bold green]",
                )
                live.update(Align.center(panel_loading))
                sleep(0.05)

        clear() 
        
        ready_text = Text.from_markup("[bold green]Ambiente pronto.[/bold green]\n\n[bold white]> PRESSIONE ESPAÇO PARA CONTINUAR <[/bold white]", justify="center")
        
        content_ready = Group(
            top_text,
            ready_text
        )
        
        panel_ready = Panel(
            content_ready,
            border_style="green",
            padding=(3, 16),
            title="[bold green]Sistema Pronto[/bold green]",
        )
        
        console.print(Align.center(panel_ready))

        while True:
            key = get_key()
            if key == 'SPACE':
                break
            sleep(0.05)
                
        clear()
                
    def _terminal_loading(self):
        clear()
        
        tasks = [                                    
            "Iniciando os subsistemas...                     ",
            "Verificando a integridade do Cobalt Core X-12...", # em portugues parece q foi feito por IA plmds KKKKKKKKKKKKKKKKKKKKKKKK e olha q eu q pensei nesses texto, portugues estragando as nossas vidas dnv
            "Carregando os módulos DarkHats...",
            "Montando diretório criptografado...",
            "Estabilizando a segurança do sistema... "
        ]
        
        extra_tasks = [
            "Reiniciando subsistemas...",
            "Ativando protocolos de segurança...",
            "Sincrozinando com a nuvem DarkHats...",
            "Finalizando a configuração do ambiente...",
            "Iniciando o protocolo hydro..."
        ]

        with Progress(
            SpinnerColumn(spinner_name="dots2", style="bold green"),
            TextColumn("[bold green]{task.description}"),
            BarColumn(complete_style="green", finished_style="bold green", style="black"),
            TextColumn("[bold green]{task.percentage:>3.0f}%"),
        ) as progress:
            
            for task_name in tasks:
                task_id = progress.add_task(task_name, total=100)

                for _ in range(100):
                    progress.update(task_id, advance=1)
                    sleep(0.01875)

        print(f"\n{Fore.GREEN}  [!] Sincronização completa. Iniciando a interface....")
        sleep(3)
        clear()
        print(f"\n{Fore.RED}  [!] Erro: Interface não foi encontrada. Iniciando protocólo de recuperação...\n")
        sleep(3)

        with Progress(
            SpinnerColumn(spinner_name="line", style="bold green"),
            TextColumn("[bold green]{task.description}"),
            BarColumn(complete_style="green", finished_style="bold green", style="black"),
            TextColumn("[bold green]{task.percentage:>3.0f}%"),
        ) as progress:
            
            for e_task in extra_tasks:
                task_id = progress.add_task(e_task, total=100)
                
                for _ in range(100):
                    progress.update(task_id, advance=1)
                    sleep(0.01875)

        print(f"\n{Fore.GREEN}  [!] Successo: Interface recuperada. Iniciando o COBALT...")  
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
        self._welcome_screen()
        #isso seria consideraro criar um OS do 0? porém extremamente limitado? 
        #s seria, tem base linuc e tem funções de um ai, receba, criei um OS do 0
        #go drinking (vaitomano)

class COBALT_FS:
    
    def __init__(self):
        self.route = "None"
        self.player_level = 0 
        self.current_dir = "root"
        self.stats = PlayerStats.get_lifetime_stats()
        self.route_manager = RouteManager(seed=7)
        self.ending_manager = EndingManager()
        self.route_history = []
        self.current_ending = ""
        self.total_tasks = self.stats.get("tasks", 0)
        self.total_chests = self.stats.get("chests", 0)
        self.total_rebirths = self.stats.get("rebirths", 0)
        self.cursor = 0
        self.inner_w = 80
        self.desc_badges = {
            "Social Engineer": "Sobreviva 2 tasks.",
            "Reverse Engineer": "Sobreviva 10 tasks.",
            "Hardware Specialist": "Abra 5 baús.",
            "Security Bypass": "Complete a task: placeholder insano.",
            "Mr.Robot": "Complete o final bom.",                                        #ai dento
            "Normal Ending": "Eu não ligo sobre as minhas ações.",
            "Good Ending": "Ajude-os. Deixe pacífico.",
            "Bad Ending": "Destrua tudo. Não deixe um traço.",
            "???": "Requisito desconhecido...",
            "DarkHats": "Você completou o jogo!"
        }        
        self.stats = PlayerStats.get_lifetime_stats()
        self.badges = {
            "Social Engineer": False,
            "Hardware Specialist": False,
            "Security Bypass": False,
            "Reverse Engineer": False,
            "Mr.Robot": False,
            "Good Ending": False,
            "Bad Ending": False,
            "Normal Ending": False,
            "???": False,
            "DarkHats": False
        }
        self._system_archives_update()

    def reset_game_data(self):
        import Game.Main.Player as PlayerStats

        current_data = self.route_manager.load_progress(badges={})
        preserved_badges = current_data.get("badges", {})
        preserved_rebirths = current_data.get("rebirths", 0) + 1  # ← +1 aqui

        new_payload = {
            "level": 1,
            "badges": preserved_badges,
            "route_history": [],
            "mission_history": [],
            "inventory": [],
            "tasks": 0,
            "chests": 0,
            "ending": "",
            "seed": self.route_manager.seed,
            "rebirths": preserved_rebirths
        }

        self.route_manager.progress_path.write_text(
            json.dumps(new_payload, indent=2), encoding="utf-8"
        )

        PlayerStats.set_lifetime_stats(tasks=0, chests=0, rebirths=preserved_rebirths)

        self.route_history = []
        self.current_ending = ""
        self.player_level = 1
        self._system_archives_update()

        return new_payload
    
    def _system_archives_update(self):
        level = self.player_level
        self.route_manager = RouteManager(seed=7)#67
        self.ending_manager = EndingManager()

        saved = self.route_manager.load_progress(self.badges)
        self.route_history = list(saved.get("route_history", []))
        
        self.current_ending = saved.get("ending", "") 
        self.player_level = int(saved.get("level", self.player_level or 1))
        self.route_level = min(5, max(1, len(self.route_history) + 1)) if self.route_history else self.player_level

        self.stats = PlayerStats.get_lifetime_stats()
        self.total_tasks = self.stats.get("tasks", 0)
        self.total_chests = self.stats.get("chests", 0)
        self.total_rebirths = self.stats.get("rebirths", 0)

        saved_badges = saved.get("badges", {})

        self.badges = {
            "Social Engineer": saved_badges.get("Social Engineer", False) or (self.stats.get("tasks", 0) >= 2),
            "Hardware Specialist": saved_badges.get("Hardware Specialist", False) or (self.stats.get("chests", 0) >= 5),
            "Security Bypass": saved_badges.get("Security Bypass", False) or (self.stats.get("tasks", 0) >= 1),
            "Reverse Engineer": saved_badges.get("Reverse Engineer", False) or (self.stats.get("tasks", 0) >= 10),
            "Mr.Robot": saved_badges.get("Mr.Robot", False),
            "Normal Ending": saved_badges.get("Normal Ending", False),
            "Good Ending": saved_badges.get("Good Ending", False),
            "Bad Ending": saved_badges.get("Bad Ending", False),
            "???": saved_badges.get("???", False),
            "DarkHats": saved_badges.get("DarkHats", False)
        }

        self.file_system = {
            "root": [
                {"name": "Instruções.txt",              "type": "FILE", "icon": "📄", "color": Fore.WHITE},
                #{"name": "Desligar",                 "type": "EXIT", "icon": " ⏻", "color": Fore.RED}
            ],

            "root/Documentos": [
                {"name": "..",                       "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
                {"name": "Notas.txt",               "type": "FILE", "icon": "📄", "color": Fore.WHITE},
                {"name": "Logs.db",                 "type": "FILE", "icon": "📄", "color": Fore.WHITE},
            ],
            
            "root/Ajuda": [
                
                {"name": "..",                       "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
             #   {"name": "Instruções.txt",              "type": "FILE", "icon": "📄", "color": Fore.WHITE},
                {"name": "DarkHats.txt",            "type": "FILE", "icon": "📄", "color": Fore.WHITE},
                {"name": "Conquistas.txt",        "type": "FILE", "icon": "📄", "color": Fore.WHITE},
            ],
            
            "root/Configurações": [
                {"name": "..",                       "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
                {"name": "Contribuidores.flat",      "type": "FILE", "icon": "📄", "color": Fore.WHITE}, 
                {"name": "Admin.db",                "type": "FILE", "icon": "📄", "color": Fore.WHITE},
                #{"name": "ResetData.flat",                "type": "FILE", "icon": "📄", "color": Fore.WHITE},
            ],            

            "root/DarkHats": [
                {"name": "..",                       "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
          #      {"name": "DarkHats.txt",            "type": "FILE", "icon": "📄", "color": Fore.WHITE}
            ],

            "root/Jogos": [
                {"name": "..",                       "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
                {"name": "SnakeGame.flat",          "type": "EXEC", "icon": "⚙️", "color": Fore.WHITE},
                {"name": "RobuxGen_v2.exe", "type": "EXEC", "icon": "⚙️", "color": Fore.WHITE}
            ],

            "root/Conquistas": [
                {"name": "..",                       "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
               # {"name": "Conquistas.txt",        "type": "FILE", "icon": "📄", "color": Fore.WHITE}
            ]
        }
        
        paste_achievements = [
            {"name": "..",                           "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
            #{"name": "Conquistas.txt",             "type": "FILE", "icon": "📄", "color": Fore.WHITE}
        ]

        for name, unlocked in self.badges.items():
            color = Fore.YELLOW if unlocked else Fore.LIGHTBLACK_EX
            paste_achievements.append({
                "name": f" {name}", 
                "type": "BADGE",
                "icon": "🏅", 
                "color": color, 
                "raw_name": name
            })
        
        self.file_system["root/Conquistas"] = paste_achievements        

        if self.player_level >= 1:
            self.file_system["root"].insert(0, {"name": "DarkHats", "type": "DIR", "icon": "📁", "color": Fore.WHITE, "target": "root/DarkHats"})
            self.file_system["root"].insert(1, {"name": "Jogos", "type": "DIR", "icon": "📁", "color": Fore.WHITE, "target": "root/Jogos"})
            self.file_system["root"].insert(3, {"name": "Documentos",                "type": "DIR",  "icon": "📁", "color": Fore.WHITE, "target": "root/Documentos"})
            self.file_system["root"].insert(2, {"name": "Conquistas", "type": "DIR", "icon": "📁", "color": Fore.WHITE, "target": "root/Conquistas"})
            self.file_system["root"].insert(5, {"name": "Configurações", "type": "DIR", "icon": "📁", "color": Fore.WHITE, "target": "root/Configurações"})
            self.file_system["root"].insert(5, {"name": "Ajuda", "type": "DIR", "icon": "📁", "color": Fore.WHITE, "target": "root/Ajuda"})
            self.file_system["root"].insert(7, {"name": "Desligar",                 "type": "EXIT", "icon": " ⏻", "color": Fore.RED})
            try:
                self.file_system["root"].remove({"name": "Instruções.txt", "type": "FILE", "icon": "📄", "color": Fore.WHITE})
            except ValueError:
                pass
        
        if self.player_level >= 2:
            self.file_system["root/Documentos"].remove({"name": "Notas.txt", "type": "FILE", "icon": "📄", "color": Fore.WHITE})
            self.file_system["root/Documentos"].insert(2, {"name": "Mãe", "FILE": "DIR", "icon": "📄", "color": Fore.WHITE,"preview": " \"Filho, vi que finalmente conseguiu um trabalho...\""})        
            self.file_system["root/Documentos"].insert(3, {"name": "Morgan", "FILE": "DIR", "icon": "📄", "color": Fore.WHITE,"preview": " \"Vejo que conseguiu terminar sua primeira tarefa...\""}) 
        
        if self.player_level >= 1:
            self.route_level = min(5, max(1, len(self.route_history) + 1))
            choices = sorted(self.route_manager.get_choices_for_level(self.route_level), key=lambda item: item['display_position'])
            self.file_system["root/DarkHats"] = [
                {"name": "..", "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
               # {"name": "DarkHats.txt",            "type": "FILE", "icon": "📄", "color": Fore.WHITE},
                {"name": f">> Nível {self.route_level}/5", "type": "INFO", "icon": "💾", "color": Fore.CYAN},
                {"name": "───────────────────────", "type": "INFO", "icon": "", "color": Fore.LIGHTBLACK_EX},
            ]
            for choice in choices:
                numero = choice['display_position'] + 1 
                self.file_system["root/DarkHats"].append({
                    "name":f"[{numero}] {choice['mission']}",
                    "type": "ROUTE",
                    "icon": "⚙️ ",
                    "color": Fore.WHITE,
                    "route": choice['route'],
                    "mission": choice['mission'],
                    "level": choice['level'],
                    "display_position": choice['display_position'],
                })
            self.file_system["root/DarkHats"].append(  {"name": "───────────────────────", "type": "INFO", "icon": "", "color": Fore.LIGHTBLACK_EX})    
          #  self.file_system["root/DarkHats"].append({"name": " DarkHats.txt", "type": "FILE", "icon": "📄", "color": Fore.WHITE})

        #if self.player_level >= 2:
         #   self.file_system["root/Documentos"].append({"name": "test.txt", "type": "FILE", "icon": "📄", "color": Fore.YELLOW})

        #if self.player_level >= 3:
          #  self.file_system["root/DarkHats"].insert(2, {"name": "boss.flat", "type": "EXEC", "icon": "⚙️", "color": Fore.WHITE})

        self.files = self.file_system[self.current_dir]
        
        if self.cursor >= len(self.files):
            self.cursor = 0

    def get_route_choices(self, level=None):
        if level is None:
            level = max(1, min(5, self.player_level or 1))
        return self.route_manager.get_choices_for_level(level)

    def record_route_choice(self, route_name):
        route_name = str(route_name).upper().strip()
        if route_name not in ("BAD", "GOOD", "TRUE"):
            raise ValueError("route_name must be BAD, GOOD or TRUE")

        self.route_history.append(route_name)
        self.current_ending = self.ending_manager.evaluate(self.route_history)
        self.route_manager.save_progress(self.badges, self.route_history, self.current_ending, level=self.player_level, tasks=self.stats.get('tasks', 0), chests=self.stats.get('chests', 0), rebirths=self.stats.get('rebirths', 0), inventory=getattr(self, 'inventory', []))
        return self.current_ending

    def draw(self):
        self._system_archives_update()
        clear()
        
        C_BORDER = Fore.GREEN 
        C_TITLE = Fore.GREEN
        
        print(f"{C_BORDER}╔{'═' * self.inner_w}╗")
        
        title = f" ■ COBALT FILE EXPLORER [{self.current_dir}]"
        pad_title = self.inner_w - visual_width(title)
        print(f"{C_BORDER}║{C_TITLE}{title}{' ' * pad_title}{C_BORDER}║")
        print(f"{C_BORDER}╠{'═' * self.inner_w}╣")
        
        for i, f in enumerate(self.files):
            is_selected = (i == self.cursor)
            
            arrow = "►" if is_selected else " "
            text_color = Fore.GREEN if is_selected else f['color']
            
            item_string = f" {arrow} {f['icon']} {f['name']}"
            visual_length = visual_width(item_string)
            space = " " * (self.inner_w - visual_length)
            print(f"{C_BORDER}║{text_color}{item_string}{space}{C_BORDER}║")
            
        print(f"{C_BORDER}╠{'═' * self.inner_w}╣")

        item_selecionado = self.files[self.cursor]
        preview = item_selecionado.get('preview', '')

        if preview:
            status = f" {preview}"
        else:
            status = (
                f" Status: {len(self.files)} itens | "
                f"Player Lvl: {self.player_level} | "
                f"Tasks: {self.stats.get('tasks', 0)} | "
                f"Baús: {self.stats.get('chests', 0)} | "
                f"Rebirths: {self.stats.get('rebirths', 0)}"
            )

           

        pad_status = self.inner_w - visual_width(status)
        print(f"{C_BORDER}║{Fore.LIGHTBLACK_EX}{status}{' ' * pad_status}{C_BORDER}║")
        print(f"{C_BORDER}╚{'═' * self.inner_w}╝{Style.RESET_ALL}")

        print(f"\n  {Fore.LIGHTBLACK_EX}[ SETAS: Navegar | ENTER: Selecionar ]{Style.RESET_ALL}")
    
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

    def handle_action(self, file):
        type = file.get('type')
        name = (file.get('name') or "").strip()
        
        if type == "DIR" or type == "BACK":
            self.current_dir = file['target']
            self.files = self.file_system[self.current_dir]
            self.cursor = 0
            return

        if type == "ROUTE":
            self._open_route_mission(file)

        elif type == "EXEC" and name == "SnakeGame.flat":
            self._open_snake_game()
        
        elif type == "BADGE":
            self._open_badge(file['raw_name'])

        elif type == "FILE" and name == "Instruções.txt":
            self._open_tutorial()

        elif type == "EXEC" and name == "boss.flat":        #vai ser na base do if e elif mesmo, oq importa é workar
            self._open_boss()
            
        elif type == "FILE" and name == "Notas.txt":
            self._open_notes()
           
        elif type == "FILE" and name == "DarkHats.txt":
            self._open_DarkHatsText()

        elif type == "EXEC" and name == "RobuxGen_v2.exe":
            from Game.Main.Games.RobuxGame import robux_game
            robux_game()    

        elif type == "FILE" and name == "ResetData.flat":
            clear()
            cText("⚠  Tem certeza que deseja resetar os dados? (S/N)", "red")
            confirm = input("  >> ").strip().upper()
            if confirm in ("S", "SIM", "Y", "YES"):
                self.reset_game_data()
                cText("✓  Dados resetados com sucesso!", "green")
            else:
                cText("  Reset cancelado.", "warn")
            sleep(2)

        elif type == "FILE" and name == "Logs.db":
            self._open_logs()

        elif type == "FILE" and name == "Admin.db":
            self._open_admins()

        elif type == "FILE" and name == "Conquistas.txt":
            self._open_achievements()

        elif type == "FILE" and name == "Contribuidores.flat":
            self._open_contribuitors()
            
        elif type == "EXIT" and name == "Desligar":
            clear()
            print(f"{Fore.RED}[!] Desligando o sistema COBALT...{Style.RESET_ALL}")
            sleep(1.5)
            sys.exit()            

    def _open_darkhats(self):
        clear()
        print(f"{Fore.CYAN}[*] Extraindo darkhats.flat...{Style.RESET_ALL}")
        sleep(1)
        print(f"{Fore.GREEN}[*] Permissões do root concedidas.{Style.RESET_ALL}")
        sleep(1)

        from Game.Main.DarkHatsGame import DarkHatsGame
        game = DarkHatsGame()
        game.route_choice = getattr(self, 'selected_route', 'BAD')
        game.mission_name = getattr(self, 'selected_mission_name', None)
        game.Player.Level = self.player_level
       # print(f"[DEBUG COBALT] Level injection in player, cuz its not working and setting level 3, tf: {game.Player.Level}")
        sleep(2)
        dih = COBALT()
        dih.start()
        game.start()

        #self.player_level = game.Player.Level
        
        saved = self.route_manager.load_progress(self.badges)
        self.player_level = int(saved.get("level", 1))
        self.route_history = list(saved.get('route_history', self.route_history))

        clear()
        print(f"{Fore.YELLOW}[!] darkhats.flat finalizado. Retornando para o COBALT...{Style.RESET_ALL}")
        sleep(2)

    def _open_route_mission(self, file):
        route_name = str(file.get('route', 'BAD')).upper().strip()
        mission_name = str(file.get('mission', 'Unknown')).strip()
        level = int(file.get('level', self.route_level))

        clear()
        print(f"{Fore.CYAN}[*] Carregando rota: {route_name} missão: {mission_name}...{Style.RESET_ALL}")
        sleep(1)

        saved = self.route_manager.load_progress(self.badges)
        mission_history = list(saved.get('mission_history', [])) + [mission_name]

        self.selected_route = route_name
        self.selected_mission_name = mission_name
        self.route_history = list(saved.get('route_history', self.route_history)) + [route_name]
        self.current_ending = self.ending_manager.evaluate(self.route_history)
        next_level = min(5, len(self.route_history) + 1)
        self.route_manager.save_progress(self.badges, self.route_history, self.current_ending, mission_history, level=next_level, tasks=self.stats.get('tasks', 0), chests=self.stats.get('chests', 0), rebirths=self.stats.get('rebirths', 0), inventory=getattr(self, 'inventory', []))
        self.player_level = next_level

        if len(self.route_history) >= 5:
            self.current_ending = self.ending_manager.evaluate(self.route_history)
            self.badges['Normal Ending'] = self.current_ending == 'ENDING_NORMAL'
            self.badges['Good Ending'] = self.current_ending == 'ENDING_GOOD'
            self.badges['Bad Ending'] = self.current_ending == 'ENDING_BAD'
            self.badges['???'] = self.current_ending == 'ENDING_TRUE'

        self._open_darkhats()

    def _open_badge(self, badge_name):
        clear()
        
        unlocked = self.badges.get(badge_name, False)
        description = self.desc_badges.get(badge_name, "Sem informações providas.")
        
        if unlocked:
            border = Fore.YELLOW
            status_text = f"{Fore.GREEN}[ DESBLOQUEADO ]"
        else:
            border = Fore.LIGHTBLACK_EX
            status_text = f"{Fore.RED}[ BLOQUEADO ]"
        
        print(f"{border}╔══════════════════════════════════════════════╗")
        
        line_1 = f" {Fore.WHITE}🏅 DETALHES DA CONQUISTA"
        pad_1 = 46 - visual_width(line_1)
        print(f"{border}║{line_1}{' ' * pad_1}{border}║")
        
        print(f"{border}╠══════════════════════════════════════════════╣")
        
        line_2 = f" {Fore.WHITE}TITULO:  {Fore.CYAN}{badge_name}"
        pad_2 = 46 - visual_width(line_2)
        print(f"{border}║{line_2}{' ' * pad_2}{border}║")
        
        line_3 = f" {Fore.WHITE}STATUS: {status_text}"
        pad_3 = 46 - visual_width(line_3)
        print(f"{border}║{line_3}{' ' * pad_3}{border}║")
        
        print(f"{border}║{' ' * 46}║")
        
        line_5 = f" {Fore.WHITE}COMO DESBLOQUEAR:"
        pad_5 = 46 - visual_width(line_5)
        print(f"{border}║{line_5}{' ' * pad_5}{border}║")
        
        truncated_desc = description[:44]
        line_6 = f" {Fore.LIGHTBLACK_EX}{truncated_desc}"
        pad_6 = 46 - visual_width(line_6)
        print(f"{border}║{line_6}{' ' * pad_6}{border}║")
        
        print(f"{border}╚══════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        input(f"\n  {Fore.WHITE}[ Pressione ENTER para voltar ]{Style.RESET_ALL}")

    def _open_tutorial(self):
        clear()

        message = (
        f"Olá, {getpass.getuser()}.\n\n"
        f"Sistema inicializado com sucesso. Prazer, sou Arthur Morgan, ou apenas Morgan.\n"
        f"Fico feliz que aceitou meu convite para entrar no mundo da cibersegurança.\n\n"
        f"Para começarmos, aqui estão as mecânicas essenciais do sistema:\n"
        f"• Navegação: Use as setas do teclado para se mover e ENTER para selecionar.\n"
        f"• Missões: Na aba 'DarkHats', você encontrará as tarefas que eu te passarei e o seu progresso atual.\n"
        f"• Recompensas: Concluir missões rende baús com itens para os personagens e upgrades no sistema!\n"
        f"Lembre-se, o sistema possui um assistente virtual, em cada aba, você deve encontrá-lo.\n\n"
        f"Ah, e fique de olho: seu sistema receberá atualizações constantes.\n"
        f"OBS: Esta mensagem aparecerá apenas uma vez.\n"
        f"Aperte ENTER para fechar e começar."
        )

        text(message, "GREEN", "GREEN")
        self.player_level = 1

        input(f"\n  {Fore.LIGHTBLACK_EX}[ Pressione ENTER para voltar ]{Style.RESET_ALL}") #jenial a sacada do input, pq ele trava o caba, pra ai s n precisar usar varios sleep
        self.route_manager.save_progress(
            badges=self.badges, 
            route_history=self.route_history, 
            ending=self.current_ending, 
            level=self.player_level, 
            tasks=self.total_tasks, 
            chests=self.total_chests,
            rebirths=self.total_rebirths,
            inventory=getattr(self, 'inventory', [])
        )

        self._system_archives_update()     
    def _open_snake_game(self):
        clear()
        print(f"{Fore.CYAN}[*] Iniciando SnakeGame.flat...{Style.RESET_ALL}")
        sleep(1)

        try:
            from Game.Main.Games.SnakeGame import snake_game #joguin da cobrinha

            while True:
                death = snake_game()
                if death:
                    clear()
                    print(f"{Fore.YELLOW}[!] Você morreu. Retornando para a pasta Jogos...{Style.RESET_ALL}")
                    sleep(2)
                    self.current_dir = "root/Jogos"
                    self.files = self.file_system[self.current_dir]
                    self.cursor = 0
                    return

                clear()
                print(f"{Fore.GREEN}[!] You survived the round. Play again?{Style.RESET_ALL}")
                print(f"{Fore.LIGHTBLACK_EX}Press ENTER to replay, or Ctrl+C to exit the game.{Style.RESET_ALL}")
                try:
                    input()
                except KeyboardInterrupt:
                    break

        except Exception as exc:
            clear()
            print(f"{Fore.RED}[!] Erro para iniciar o SnakeGame.flat: {exc}{Style.RESET_ALL}")
            sleep(2)
            self.current_dir = "root/Jogos"
            self.files = self.file_system[self.current_dir]
            self.cursor = 0
            return

        clear()
        print(f"{Fore.YELLOW}[!] Retornando para o COBALT...{Style.RESET_ALL}")
        sleep(1)

    def _open_boss(self):
        clear()
        print(f"{Fore.RED}╔════════════════════════════════════════════╗")
        
        line_1 = f" {Fore.YELLOW}⚠️  WARNING: SYSTEM AT RISK"
        pad_1 = 44 - visual_width(line_1)
        print(f"║{line_1}{' ' * pad_1}{Fore.RED}║")
        
        print(f"╠════════════════════════════════════════════╣")
        
        line_2 = " Connecting to serve..."
        pad_2 = 44 - visual_width(line_2)
        print(f"║{line_2}{' ' * pad_2}║")
        
        line_3 = " Executing."
        pad_3 = 44 - visual_width(line_3)
        print(f"║{line_3}{' ' * pad_3}║")
        
        print(f"╚════════════════════════════════════════════╝{Style.RESET_ALL}")
        sleep(2)
        
        # carrega boss
        from Game.Main.DarkHatsGame import DarkHatsGame
        game = DarkHatsGame()
        game.Player.Level = self.player_level
        
        # game.boss()
        game.start() 
        
        self.player_level = game.Player.Level
        clear()              

    def _open_contribuitors(self):
        clear()
        print(f"{Fore.YELLOW}[!] ABRINDO Contribuidores.flat...{Style.RESET_ALL}")
        sleep(0.5)
        clear()
        print(f"{Fore.GREEN}╔══════════════════════════════════════════════════╗")
        
        line_1 = f" {Fore.GREEN}✏️  VISUALIZADOR DE TEXTO: Contribuidores.flat"
        pad_1 = 44 - visual_width(line_1)
        print(f"{Fore.GREEN}║{line_1}{' ' * pad_1}{Fore.GREEN}║")
        
        print(f"{Fore.GREEN}╠══════════════════════════════════════════════════╣")
        
        line_2 = " Hydro"
        pad_2 = 44 - visual_width(line_2)
        print(f"{Fore.GREEN}║{line_2}{' ' * pad_2}║")
        
        line_3 = " Apogavi"
        pad_3 = 44 - visual_width(line_3)
        print(f"{Fore.GREEN}║{line_3}{' ' * pad_3}║")
        
        line_4 = " DiscorDANdo"
        pad_4 = 44 - visual_width(line_4)
        print(f"{Fore.GREEN}║{line_4}{' ' * pad_4}║")
        
        line_5 = " Guilherme"
        pad_5 = 44 - visual_width(line_5)
        print(f"{Fore.GREEN}║{line_5}{' ' * pad_5}║")
        
        print(f"{Fore.GREEN}╚══════════════════════════════════════════════════╝{Style.RESET_ALL}")
        input(f"\n  {Fore.LIGHTBLACK_EX}[ Pressione ENTER para retornar ]{Style.RESET_ALL}")

    def _open_admins(self):
        clear()
        print(f"{Fore.YELLOW}[!] Abrindo Admin.db...{Style.RESET_ALL}")
        sleep(0.5)
        clear()        
        print(f"{Fore.GREEN}╔════════════════════════════════════════════╗")
        
        line_1 = f" {Fore.GREEN}⚙️  VISUALIZADOR DE TEXTO: Admin.db"
        pad_1 = 44 - visual_width(line_1)
        print(f"{Fore.GREEN}║{line_1}{' ' * pad_1}{Fore.GREEN}║")
        
        print(f"{Fore.GREEN}╠════════════════════════════════════════════╣")
        
        line_2 = " Você não é um adminstrador!"
        pad_2 = 44 - visual_width(line_2)
        print(f"{Fore.GREEN}║{line_2}{' ' * pad_2}║")
        
        print(f"{Fore.GREEN}╚════════════════════════════════════════════╝{Style.RESET_ALL}")
        input(f"\n  {Fore.LIGHTBLACK_EX}[ Pressione ENTER para retornar ]{Style.RESET_ALL}")    

    def _open_notes(self):
        clear()
        print(f"{Fore.YELLOW}[!] Abrindo Notas.txt...{Style.RESET_ALL}")
        sleep(0.5)
        clear()
        print(f"{Fore.WHITE}╔════════════════════════════════════════════╗")
        
        line_1 = f" {Fore.WHITE}📝 VISUALIZADOR DE TEXTO: Notas.txt"
        pad_1 = 44 - visual_width(line_1)
        print(f"║{line_1}{' ' * pad_1}║")
        
        print(f"╠════════════════════════════════════════════╣")
        
        lines = [
            " Finalmente consegui um emprego.",
            " Talvez minha mãe fique feliz com isso!",
            " Quando conseguir meu primeiro salário,",
            " com toda certeza mostrarei para ela.",
            #""
        ]
        for line in lines:
            pad = 44 - visual_width(line)
            print(f"║{line}{' ' * pad}║")
            
        print(f"╚════════════════════════════════════════════╝{Style.RESET_ALL}")
        input(f"\n  {Fore.LIGHTBLACK_EX}[ Pressione ENTER para retornar ]{Style.RESET_ALL}")
    
    def _open_logs(self):
        clear()
        print(f"{Fore.YELLOW}[!] ABRINDO logs.db...{Style.RESET_ALL}")
        sleep(0.5)
        clear()

        for _ in range(15):
                trash = os.urandom(30).hex()  # vulgo thalles
                print(f"{Fore.RED}ERR: BLOCO ENCRIPTADO >> {trash}{Style.RESET_ALL}")
                sleep(0.05)
                
        print(f"\n{Fore.RED}[ ACCESSO NEGADO: CHAVE ENCRIPTOGRAFADA NÃO ENCONTRADA ]{Style.RESET_ALL}")
        input(f"\n  {Fore.LIGHTBLACK_EX}[ Pressione ENTER para retornar ]{Style.RESET_ALL}")
    
    def _open_achievements(self):
        clear()
        
        message = (
        f"Olá, {getpass.getuser()}.\n\n"
        f"Você pode apertar enter em uma conquista para ver sua descrição e detalhes.\n"
        f"Conquistas dão personagens e mostram o seu avanço atual no jogo.\n"
        f"OBS: Seja cuidadoso.\n\n"
        f"Aperte ENTER para fechar esta mensagem!"
        )   
        typewriter(message, speed=0.06, anim_speed=3)

        input(f"\n  {Fore.LIGHTBLACK_EX}[ Pressione ENTER para retornar ]{Style.RESET_ALL}")

    def _open_DarkHatsText(self):
        clear()
        
        message = (
            f"E aí, {getpass.getuser()}.\n"
            f"\n"
            f"COMO ENTRAR EM UMA MISSÃO\n"
            f"Na pasta DarkHats, você verá 3 opções numeradas.\n"
            f"Cada uma é uma missão diferente. Escolha uma e pressione ENTER!\n"
            f"\n"
            f"CLASSES\n"
            f"Para navegar entre as classes, digite 'next' ou 'previous'.\n"
            f"Algumas classes precisam de uma conquista específica para serem desbloqueadas.\n"
            f"\n"
            f"NOME DE USUÁRIO\n"
            f"O nome que você usa aqui é apenas um apelido.\n"
            f"Nunca use seu nome real!\n"
            f"\n"
            f"Pressione ENTER para fechar."
        )   
        typewriter(message, speed=0.06, anim_speed=3)

        input(f"\n  {Fore.LIGHTBLACK_EX}[ Pressione ENTER para retornar ]{Style.RESET_ALL}")

def Explorer():
    clear()
    COBALT_FS().run()
# explorer = COBALT_FS()
# explorer.run()
# game = COBALT()
#game.start() #eita porra, funciono mesmo KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK (vou criar um backup do antigo pra vcs ver a bomba q era, pq to falando vcs sendo q provavelmente vc vai ta lendo solo? seco seco)