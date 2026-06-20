import os
import sys
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

        top_text.append("\n\n               W E L C O M E\n", style="bold white")
        top_text.append(f"                User: {user_name}\n\n", style="dim green")

        clear()

        spinner = Spinner("dots", text="[green]Preparing COBALT desktop environment...", style="bold green")
        
        with Live(console=console, refresh_per_second=20) as live:
            for _ in range(50):
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
        
        ready_text = Text.from_markup("[bold green]Environment Ready.[/bold green]\n\n[bold white]> PRESS SPACE TO CONTINUE <[/bold white]", justify="center")
        
        content_ready = Group(
            top_text,
            ready_text
        )
        
        panel_ready = Panel(
            content_ready,
            border_style="green",
            padding=(3, 16),
            title="[bold green]System Ready[/bold green]",
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

        print(f"\n{Fore.GREEN}  [!] Synchronization complete. Starting interface....")
        sleep(3)
        clear()
        print(f"\n{Fore.RED}  [!] Error: Interface not found. Starting recovery protocol...\n")
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
        self.cursor = 0
        self.inner_w = 80
        self.desc_badges = {
            "Social Engineer": "Survive 2 tasks.",
            "Reverse Engineer": "Survive 10 tasks.",
            "Hardware Specialist": "Open 5 chests",
            "Security Bypass": "Complete the task: placeholder insano",
            "Mr.Robot": "Complete the Good Ending",                                        #ai dento
            "Normal Ending": "I don't care about my actions.",
            "Good Ending": "Help them. Leave peace.",
            "Bad Ending": "Destroy everything. Don't leave any trace.",
            "???": "Unknown requirement..."
        }        
        self.stats = PlayerStats.get_lifetime_stats()
        self.badges = {
            "Social Engineer": False,
            "Hardware Specialist": False,
            "Security Bypass": False,
            "Reverse Engineer": False,
            "Robot": False,
            "Good Ending": False,
            "Bad Ending": False,
            "Normal Ending": False,
            "Mr.Robot": False,
            "???": False,
        }
        self._system_archives_update()

    def reset_game_data(self):
        current_data = self.load_progress(badges={})
        preserved_badges = current_data.get("badges", {})
        new_payload = {
            "level": 1,
            "badges": preserved_badges,
            "route_history": [],
            "mission_history": [],
            "inventory": [],
            "tasks": 0,
            "chests": 0,
            "ending": "",
            "seed": self.seed,
        }
        
        self.progress_path.write_text(json.dumps(new_payload, indent=2), encoding="utf-8")
        return new_payload
    
    def _system_archives_update(self):
        level = self.player_level
        self.route_manager = RouteManager(seed=7)
        self.ending_manager = EndingManager()

        saved = self.route_manager.load_progress(self.badges)
        self.route_history = list(saved.get("route_history", []))
        
        self.current_ending = saved.get("ending", "") 
        self.player_level = int(saved.get("level", self.player_level or 1))
        self.route_level = min(5, max(1, len(self.route_history) + 1)) if self.route_history else self.player_level

        self.stats = PlayerStats.get_lifetime_stats()
        self.total_tasks = self.stats.get("tasks", 0)
        self.total_chests = self.stats.get("chests", 0)

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
            "???": saved_badges.get("???", False)
        }

        self.file_system = {
            "root": [
                {"name": "README.flat",              "type": "FILE", "icon": "📄", "color": Fore.WHITE},
                {"name": "shutdown",                 "type": "EXIT", "icon": " ⏻", "color": Fore.RED}
            ],

            "root/Documents": [
                {"name": "..",                       "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
                {"name": " notes.txt",               "type": "FILE", "icon": "📄", "color": Fore.WHITE},
                {"name": " logs.db",                 "type": "FILE", "icon": "📄", "color": Fore.WHITE},
            ],

            "root/Settings": [
                {"name": "..",                       "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
                {"name": " Contribuitors.flat",      "type": "FILE", "icon": "📄", "color": Fore.WHITE}, 
                {"name": " Admin.db",                "type": "FILE", "icon": "📄", "color": Fore.WHITE},
            ],            

            "root/DarkHats": [
                {"name": "..",                       "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
                {"name": " DarkHats.txt",            "type": "FILE", "icon": "📄", "color": Fore.WHITE}
            ],

            "root/Games": [
                {"name": "..",                       "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
                {"name": " SnakeGame.flat",          "type": "EXEC", "icon": "⚙️", "color": Fore.WHITE},
            ],

            "root/Achievements": [
                {"name": "..",                       "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
                {"name": " Achievements.txt",        "type": "FILE", "icon": "📄", "color": Fore.WHITE}
            ]
        }
        
        paste_achievements = [
            {"name": "..",                           "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
            {"name": "Achievements.txt",             "type": "FILE", "icon": "📄", "color": Fore.WHITE}
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
        
        self.file_system["root/Achievements"] = paste_achievements        

        if self.player_level >= 1:
            self.file_system["root"].insert(0, {"name": "DarkHats", "type": "DIR", "icon": "📁", "color": Fore.WHITE, "target": "root/DarkHats"})
            self.file_system["root"].insert(1, {"name": "Games", "type": "DIR", "icon": "📁", "color": Fore.WHITE, "target": "root/Games"})
            self.file_system["root"].insert(3, {"name": "Documents",                "type": "DIR",  "icon": "📁", "color": Fore.WHITE, "target": "root/Documents"})
            self.file_system["root"].insert(2, {"name": "Achievments", "type": "DIR", "icon": "📁", "color": Fore.WHITE, "target": "root/Achievements"})
            self.file_system["root"].insert(5, {"name": "Settings", "type": "DIR", "icon": "📁", "color": Fore.WHITE, "target": "root/Settings"})
            try:
                self.file_system["root"].remove({"name": "README.flat", "type": "FILE", "icon": "📄", "color": Fore.WHITE})
            except ValueError:
                pass

        if self.player_level >= 1:
            self.route_level = min(5, max(1, len(self.route_history) + 1))
            choices = sorted(self.route_manager.get_choices_for_level(self.route_level), key=lambda item: item['display_position'])
            self.file_system["root/DarkHats"] = [
                {"name": "..", "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
                {"name": f"Route Level {self.route_level}", "type": "INFO", "icon": "🛰️  ", "color": Fore.CYAN},
            ]
            for choice in choices:
                self.file_system["root/DarkHats"].append({
                    "name": choice['mission'],
                    "type": "ROUTE",
                    "icon": "⚙️  ",
                    "color": Fore.WHITE,
                    "route": choice['route'],
                    "mission": choice['mission'],
                    "level": choice['level'],
                    "display_position": choice['display_position'],
                })
            self.file_system["root/DarkHats"].append({"name": " DarkHats.txt", "type": "FILE", "icon": "📄", "color": Fore.WHITE})

        if self.player_level >= 2:
            self.file_system["root/Documents"].append({"name": "test.txt", "type": "FILE", "icon": "📄", "color": Fore.YELLOW})

        if self.player_level >= 3:
            self.file_system["root/DarkHats"].insert(2, {"name": "boss.flat", "type": "EXEC", "icon": "⚙️", "color": Fore.WHITE})

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
        self.route_manager.save_progress(self.badges, self.route_history, self.current_ending, level=self.player_level, tasks=self.stats.get('tasks', 0), chests=self.stats.get('chests', 0), inventory=getattr(self, 'inventory', []))
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
        
        status = (
            f" Status: {len(self.files)} items | "
            f"Player Lvl: {self.player_level} | "
            f"Tasks: {self.stats.get('tasks', 0)} | "
            f"Chests: {self.stats.get('chests', 0)}"
        )
        pad_status = self.inner_w - visual_width(status)
        print(f"{C_BORDER}║{Fore.LIGHTBLACK_EX}{status}{' ' * pad_status}{C_BORDER}║")
        print(f"{C_BORDER}╚{'═' * self.inner_w}╝{Style.RESET_ALL}")

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

        elif type == "FILE" and name == "README.flat":
            self._open_tutorial()

        elif type == "EXEC" and name == "boss.flat":        #vai ser na base do if e elif mesmo, oq importa é workar
            self._open_boss()
            
        elif type == "FILE" and name == "notes.txt":
            self._open_notes()
           
        elif type == "FILE" and name == "DarkHats.txt":
            self._open_DarkHatsText()

        elif type == "FILE" and name == "logs.db":
            self._open_logs()

        elif type == "FILE" and name == "Admin.db":
            self._open_admins()

        elif type == "FILE" and name == "Achievements.txt":
            self._open_achievements()

        elif type == "FILE" and name == "Contribuitors.flat":
            self._open_contribuitors()
            
        elif type == "EXIT" and name == "shutdown":
            clear()
            print(f"{Fore.RED}[!] Shutting down COBALT OS...{Style.RESET_ALL}")
            sleep(1.5)
            sys.exit()            

    def _open_darkhats(self):
        clear()
        print(f"{Fore.CYAN}[*] Extracting darkhats.flat...{Style.RESET_ALL}")
        sleep(1)
        print(f"{Fore.GREEN}[*] Root permissions granted.{Style.RESET_ALL}")
        sleep(1)

        from Game.Main.DarkHatsGame import DarkHatsGame
        game = DarkHatsGame()
        game.route_choice = getattr(self, 'selected_route', 'BAD')
        game.mission_name = getattr(self, 'selected_mission_name', None)
        game.Player.Level = self.player_level

        game.start()

        #self.player_level = game.Player.Level
        
        saved = self.route_manager.load_progress(self.badges)
        self.player_level = int(saved.get("level", 1))
        self.route_history = list(saved.get('route_history', self.route_history))

        clear()
        print(f"{Fore.YELLOW}[!] darkhats.flat finished. Returning to COBALT...{Style.RESET_ALL}")
        sleep(2)

    def _open_route_mission(self, file):
        route_name = str(file.get('route', 'BAD')).upper().strip()
        mission_name = str(file.get('mission', 'Unknown')).strip()
        level = int(file.get('level', self.route_level))

        clear()
        print(f"{Fore.CYAN}[*] Loading route {route_name} mission {mission_name}...{Style.RESET_ALL}")
        sleep(1)

        saved = self.route_manager.load_progress(self.badges)
        mission_history = list(saved.get('mission_history', [])) + [mission_name]

        self.selected_route = route_name
        self.selected_mission_name = mission_name
        self.route_history = list(saved.get('route_history', self.route_history)) + [route_name]
        self.current_ending = self.ending_manager.evaluate(self.route_history)
        next_level = min(5, len(self.route_history) + 1)
        self.route_manager.save_progress(self.badges, self.route_history, self.current_ending, mission_history, level=next_level, tasks=self.stats.get('tasks', 0), chests=self.stats.get('chests', 0), inventory=getattr(self, 'inventory', []))
        self.player_level = next_level

        if len(self.route_history) >= 5:
            self.current_ending = self.ending_manager.evaluate(self.route_history)
            self.badges['Normal Ending'] = self.current_ending == 'ENDING_NORMAL'
            self.badges['Good Ending'] = self.current_ending == 'ENDING_GOOD'
            self.badges['Bad Ending'] = self.current_ending == 'ENDING_BAD'
            self.badges['Mr.Robot'] = self.current_ending == 'ENDING_TRUE'

        self._open_darkhats()

    def _open_badge(self, badge_name):
        clear()
        
        unlocked = self.badges.get(badge_name, False)
        description = self.desc_badges.get(badge_name, "No informations provided.")
        
        if unlocked:
            border = Fore.YELLOW
            status_text = f"{Fore.GREEN}[ UNLOCKED ]"
        else:
            border = Fore.LIGHTBLACK_EX
            status_text = f"{Fore.RED}[ LOCKED ]"
        
        print(f"{border}╔══════════════════════════════════════════════╗")
        
        line_1 = f" {Fore.WHITE}🏅 ACHIEVEMENT DETAILS"
        pad_1 = 46 - visual_width(line_1)
        print(f"{border}║{line_1}{' ' * pad_1}{border}║")
        
        print(f"{border}╠══════════════════════════════════════════════╣")
        
        line_2 = f" {Fore.WHITE}TITLE:  {Fore.CYAN}{badge_name}"
        pad_2 = 46 - visual_width(line_2)
        print(f"{border}║{line_2}{' ' * pad_2}{border}║")
        
        line_3 = f" {Fore.WHITE}STATUS: {status_text}"
        pad_3 = 46 - visual_width(line_3)
        print(f"{border}║{line_3}{' ' * pad_3}{border}║")
        
        print(f"{border}║{' ' * 46}║")
        
        line_5 = f" {Fore.WHITE}HOW TO UNLOCK:"
        pad_5 = 46 - visual_width(line_5)
        print(f"{border}║{line_5}{' ' * pad_5}{border}║")
        
        truncated_desc = description[:44]
        line_6 = f" {Fore.LIGHTBLACK_EX}{truncated_desc}"
        pad_6 = 46 - visual_width(line_6)
        print(f"{border}║{line_6}{' ' * pad_6}{border}║")
        
        print(f"{border}╚══════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        input(f"\n  {Fore.WHITE}[ Press ENTER to return ]{Style.RESET_ALL}")

    def _open_tutorial(self):
        clear()
        
        message = (
        f"Connection established. Welcome, {getpass.getuser()}.\n"
        f"To use the COBALT OS, you will need a keyboard with:\n"
        f"  Numpad,\n"
        f"  Arrows,\n"
        f"  And letters (optional for names!)\n" 
        f"To move in the archives, use arrows and for selecting then, just press enter.\n"
        f"How you opened this without knowing?"
        f"Remember, almost all the pages, have a tutorial explaining them, as txt or md!"
        f"P.S: This message will only appear once."
        f"\nPress enter to close this message"
        )   

        typewriter(message, speed=0.06, anim_speed=3)
        self.player_level = 1

        self.route_manager.save_progress(
            badges=self.badges, 
            route_history=self.route_history, 
            ending=self.current_ending, 
            level=self.player_level, 
            tasks=self.total_tasks, 
            chests=self.total_chests,
            inventory=getattr(self, 'inventory', [])
        )

        self._system_archives_update()        

        input(f"\n  {Fore.LIGHTBLACK_EX}[ Press ENTER to return ]{Style.RESET_ALL}") #jenial a sacada do input, pq ele trava o caba, pra ai s n precisar usar varios sleep

    def _open_snake_game(self):
        clear()
        print(f"{Fore.CYAN}[*] Launching SnakeGame.flat...{Style.RESET_ALL}")
        sleep(1)

        try:
            from Game.Main.Games.SnakeGame import snake_game #joguin da cobrinha

            while True:
                death = snake_game()
                if death:
                    clear()
                    print(f"{Fore.YELLOW}[!] You died. Returning to the Games folder...{Style.RESET_ALL}")
                    sleep(2)
                    self.current_dir = "root/Games"
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
            print(f"{Fore.RED}[!] Failed to launch SnakeGame.flat: {exc}{Style.RESET_ALL}")
            sleep(2)
            self.current_dir = "root/Games"
            self.files = self.file_system[self.current_dir]
            self.cursor = 0
            return

        clear()
        print(f"{Fore.YELLOW}[!] Returning to COBALT...{Style.RESET_ALL}")
        sleep(1)

    def _open_boss(self):
        clear()
        print(f"{Fore.RED}╔════════════════════════════════════════════╗")
        
        line_1 = f" {Fore.YELLOW}⚠️  WARNING: SYSTEM INTEGRITY AT RISK"
        pad_1 = 44 - visual_width(line_1)
        print(f"║{line_1}{' ' * pad_1}{Fore.RED}║")
        
        print(f"╠════════════════════════════════════════════╣")
        
        line_2 = " Connecting to highly secure server..."
        pad_2 = 44 - visual_width(line_2)
        print(f"║{line_2}{' ' * pad_2}║")
        
        line_3 = " Executing malware injection..."
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
        print(f"{Fore.YELLOW}[!] OPENING Contribuitors.flat...{Style.RESET_ALL}")
        sleep(0.5)
        clear()
        print(f"{Fore.GREEN}╔════════════════════════════════════════════╗")
        
        line_1 = f" {Fore.GREEN}✏️  TEXT VISUALIZER: Contribuitors.flat"
        pad_1 = 44 - visual_width(line_1)
        print(f"{Fore.GREEN}║{line_1}{' ' * pad_1}{Fore.GREEN}║")
        
        print(f"{Fore.GREEN}╠════════════════════════════════════════════╣")
        
        line_2 = " Hydro"
        pad_2 = 44 - visual_width(line_2)
        print(f"{Fore.GREEN}║{line_2}{' ' * pad_2}║")
        
        line_3 = " Apogavi"
        pad_3 = 44 - visual_width(line_3)
        print(f"{Fore.GREEN}║{line_3}{' ' * pad_3}║")
        
        line_4 = " DiscorDANdo"
        pad_4 = 44 - visual_width(line_4)
        print(f"{Fore.GREEN}║{line_4}{' ' * pad_4}║")
        
        print(f"{Fore.GREEN}╚════════════════════════════════════════════╝{Style.RESET_ALL}")
        input(f"\n  {Fore.LIGHTBLACK_EX}[ Press ENTER to return ]{Style.RESET_ALL}")

    def _open_admins(self):
        clear()
        print(f"{Fore.YELLOW}[!] OPENING Admin.db...{Style.RESET_ALL}")
        sleep(0.5)
        clear()        
        print(f"{Fore.GREEN}╔════════════════════════════════════════════╗")
        
        line_1 = f" {Fore.GREEN}⚙️  TEXT VISUALIZER: Admin.db"
        pad_1 = 44 - visual_width(line_1)
        print(f"{Fore.GREEN}║{line_1}{' ' * pad_1}{Fore.GREEN}║")
        
        print(f"{Fore.GREEN}╠════════════════════════════════════════════╣")
        
        line_2 = " You're not an admin!"
        pad_2 = 44 - visual_width(line_2)
        print(f"{Fore.GREEN}║{line_2}{' ' * pad_2}║")
        
        print(f"{Fore.GREEN}╚════════════════════════════════════════════╝{Style.RESET_ALL}")
        input(f"\n  {Fore.LIGHTBLACK_EX}[ Press ENTER to return ]{Style.RESET_ALL}")    

    def _open_notes(self):
        clear()
        print(f"{Fore.YELLOW}[!] OPENING notes.txt...{Style.RESET_ALL}")
        sleep(0.5)
        clear()
        print(f"{Fore.WHITE}╔════════════════════════════════════════════╗")
        
        line_1 = f" {Fore.WHITE}📝 TEXT VISUALIZER: notes.txt"
        pad_1 = 44 - visual_width(line_1)
        print(f"║{line_1}{' ' * pad_1}║")
        
        print(f"╠════════════════════════════════════════════╣")
        
        lines = [
            " Lembrete para a equipe DarkHats:",
            " Hydro é lindo",
            " Preciso de um café",
            " DarkHats Updater é lindo",
            " - Admin"
        ]
        for line in lines:
            pad = 44 - visual_width(line)
            print(f"║{line}{' ' * pad}║")
            
        print(f"╚════════════════════════════════════════════╝{Style.RESET_ALL}")
        input(f"\n  {Fore.LIGHTBLACK_EX}[ Press ENTER to return ]{Style.RESET_ALL}")
    
    def _open_logs(self):
        clear()
        print(f"{Fore.YELLOW}[!] OPENING logs.db...{Style.RESET_ALL}")
        sleep(0.5)
        clear()

        for _ in range(15):
                trash = os.urandom(30).hex()  # vulgo thalles
                print(f"{Fore.RED}ERR: ENCRYPTED BLOCK >> {trash}{Style.RESET_ALL}")
                sleep(0.05)
                
        print(f"\n{Fore.RED}[ ACCESS DENIED: ENCRYPTION KEY NOT FOUND ]{Style.RESET_ALL}")
        input(f"\n  {Fore.LIGHTBLACK_EX}[ Press ENTER to return ]{Style.RESET_ALL}")
    
    def _open_achievements(self):
        clear()
        
        message = (
        f"Hello, {getpass.getuser()}.\n"
        f"You can press enter in a badge to see it description and details.\n"
        f"Badges gives you new characters and shows the current progress in the game.\n"
        f"P.S: Be careful.\n"
        f"Press enter to close this message!"
        )   
        typewriter(message, speed=0.06, anim_speed=3)

        input(f"\n  {Fore.LIGHTBLACK_EX}[ Press ENTER to return ]{Style.RESET_ALL}")

    def _open_DarkHatsText(self):
        clear()
        
        message = (
        f"What's up, {getpass.getuser()}.\n"
        f"To look through the classes, you just need to type 'next' or 'previous'!\n"
        f"Remember, some classes may be locked without their respective badge.\n"
        f"P.S: The name you always put, it's only a pseudonym. NEVER put your real name on it.\n"
        f"Press enter to close this message!"
        )   
        typewriter(message, speed=0.06, anim_speed=3)

        input(f"\n  {Fore.LIGHTBLACK_EX}[ Press ENTER to return ]{Style.RESET_ALL}")

def Explorer():
    clear()
    COBALT_FS().run()
# explorer = COBALT_FS()
# explorer.run()
# game = COBALT()
#game.start() #eita porra, funciono mesmo KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK (vou criar um backup do antigo pra vcs ver a bomba q era, pq to falando vcs sendo q provavelmente vc vai ta lendo solo? seco seco)