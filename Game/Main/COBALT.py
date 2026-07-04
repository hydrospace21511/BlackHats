import os
import sys
from Game.Main.Color import cText
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
from Game.Main.typewriter import typewriter
from Game.Main.typewriter import text
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
        elif key == b' ':
            return 'SPACE'
        return None
    else:
        import tty, termios
        fd = sys.stdin.fileno()
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


lore_files = {

    "Notas.txt": {
        "color": Fore.WHITE,
        "preview": " \"Finalmente consegui um emprego...\"",
        "lines": [
            " [ ARQUIVO: notas.log ]",
            " [ DATA: 01/03/1998 ]",
            " ─────────────────────────────────────────────",
            " ",
            " Finalmente consegui um emprego.",
            " Talvez minha mãe fique feliz com isso!",
            " Quando conseguir meu primeiro salário,",
            " com toda certeza mostrarei para ela.",
            " ",
            " ─────────────────────────────────────────────",
        ],
    },

    "Diário.txt": {
        "color": Fore.WHITE,
        "preview": " \"Filho, vi que finalmente conseguiu um trabalho...\"",
        "lines": [
            " [ ARQUIVO: mae_01.log ]",
            " [ DATA: 03/04/1998 ]",
            " ─────────────────────────────────────────────",
            " ",
            " Filho, vi que finalmente conseguiu um trabalho.",
            " Fico muito feliz mesmo.",
            " Só queria que você soubesse disso.",
            " ",
            " Se cuide.",
            " - Mãe",
            " ─────────────────────────────────────────────",
        ],
    },

    "Morgan.txt": {
        "color": Fore.WHITE,
        "preview": " \"Vejo que terminou sua primeira tarefa...\"",
        "lines": [
            " [ ARQUIVO: morgan_01.log ]",
            " [ DATA: 03/04/1998 ]",
            " ─────────────────────────────────────────────",
            " ",
            " Vejo que você terminou sua primeira tarefa.",
            " Bom trabalho.",
            " O sistema não perdoa iniciantes, mas você",
            " parece saber o que está fazendo.",
            " ",
            " Continue assim.",
            " — Arthur",
            " ─────────────────────────────────────────────",
        ],
    },

    "Relato.txt": {
        "color": Fore.WHITE,
        "preview": " \"Filho, perdão pela demora para responder...\"",
        "lines": [
            " [ ARQUIVO: mae_02.log ]",
            " [ DATA: 15/05/1998 ]",
            " ─────────────────────────────────────────────",
            " ",
            " Filho, estive com uma dor de cabeça,",
            " e acabei não respondendo.",
            " Porém agora já estou melhor.",
            " ",
            " Estou orgulhosa de você.",
            " - Mãe",
            " ─────────────────────────────────────────────",
        ],
    },

    "Morgan2.txt": {
        "color": Fore.WHITE,
        "preview": " \"Ei, vejo que realmente está se empenhando...\"",
        "lines": [
            " [ ARQUIVO: morgan_02.log ]",
            " [ DATA: 10/05/1998 ]",
            " ─────────────────────────────────────────────",
            " ",
            " Ei, vejo que realmente está se empenhando.",
            " Bom trabalho.",
            " Poderia me mandar os arquivos?",
            " Estarei aguardando seu retorno.",
            " ",
            " Continue assim.",
            " — Arthur",
            " ─────────────────────────────────────────────",
        ],
    },

    "Trabalho.txt": {
        "color": Fore.WHITE,
        "preview": " [CORROMPIDO] \"V0c3 3st4... 0 qu3.. 4c0nt3c3nd0?\"",
        "lines": [
            " [ ARQUIVO: m0rg4n_03.log ]",
            " [ DATA: 05/07/1998 ]",
            " ─────────────────────────────────────────────",
            " ",
            " V0c3 3st4 b3m? 3st4 tr4b4lh4nd0 m4s n4o m3",
            " r3t0rn4.",
            " 0 qu3 3st4 4c0nt3c3nd0?",
            " 3sp3r0 qu3 m3lh0r3.",
            " ",
            " N4o sum4.",
            " — Arthur",
            " ─────────────────────────────────────────────",
        ],
    },

    "Lembranças.txt": {
        "color": Fore.WHITE,
        "preview": " \"Finalmente consegui um trabalho.\"",
        "lines": [
            " [ PROCESSO: Eu.exe ]",
            " [ DATA: 26/02/1998 ]",
            " ──────────────────────────────────────────────",
            " ",
            " Consegui um trabalho hoje.",
            " Morgan me convenceu a entrar na área.",
            " ",
            " Ele mencionou uma tal de ACSD antes de ir.",
            " Associação Contra Distúrbio, disse ele.",
            " ",
            " Pareceu razoável na hora.",
            " ──────────────────────────────────────────────",
        ],
    },

    "A Raiz.txt": {
        "color": Fore.YELLOW,
        "preview": " [CORROMPIDO] \"...ela sabia. desde o início...\"",
        "lines": [
            " [ ARQUIVO: sistema_old_backup_1996.log ]",
            " [ INTEGRIDADE: 34% — PARCIALMENTE CORROMPIDOS ]",
            " ─────────────────────────────────────────────",
            " ",
            " ...enc0ntrei iss0 no backup antigo...",
            " não me lembro de ter escrito.",
            " ",
            " A Raiz está apodrecendo.",
            " eu continuo construindo em cima",
            " sem olhar para baixo.",
            " ",
            " ela tentou me dizer algo hoje.",
            " eu fechei a porta.",
            " ",
            " ...[ BLOCO 0x3A: ILEGÍVEL ]...",
            " ─────────────────────────────────────────────",
        ],
    },

    "NULL.txt": {
        "color": Fore.RED,
        "preview": " [SISTEMA] \"NULL não respondeu.\"",
        "lines": [
            " [ PROCESSO: Eu.exe ]",
            " [ TIMESTAMP: --/--/---- 03:17 ]",
            " ─────────────────────────────────────────────",
            " ",
            " NULL não está respondendo.",
            " Terceiro dia consecutivo.",
            " ",
            " Tentei um ping às 03:00.",
            " Sem resposta.",
            " ",
            " O quarto retornou NULL.",
            " ",
            " Não abri a porta.",
            " Não precisava.",
            " Ela não estava mais lá de qualquer forma.",
            " ",
            " [ processo encerrado ]",
            " ─────────────────────────────────────────────",
        ],
    },

    "SHEOL.txt": {
        "color": Fore.MAGENTA,
        "preview": " [SHEOL] \"O lugar dos mortos não é punição.\"",
        "lines": [
            " [ PARTITION: /dev/sheol ]",
            " [ STATUS: UNMOUNTED ]",
            " ─────────────────────────────────────────────",
            " ",
            " SHEOL não é inferno.",
            " SHEOL não é céu.",
            " ",
            " É ausência.",
            " É o lugar onde os nomes somem",
            " antes de alguém perceber que foram embora.",
            " ",
            " A ACSD nunca precisou agir.",
            " Eu me encarreguei disso sozinho.",
            " ",
            " O sonho é vívido.",
            " O sonho é inacabável.",
            " O sonho é o único lugar onde ela ainda existe.",
            " ",
            " [ FIM DO REGISTRO ]",
            " ─────────────────────────────────────────────",
        ],
    },
}


def _menu_border_color(player_level: int) -> str:
    if player_level >= 5:
        return Fore.MAGENTA
    if player_level >= 4:
        return Fore.RED
    if player_level >= 3:
        return Fore.YELLOW
    return Fore.GREEN


class COBALT:
    def __init__(self, player_level: int = 0):
        self.options = ["Play", "Help", "Exit"]
        self.player_level = player_level

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

    def _Load_Menu(self):
        G = Fore.GREEN
        for i in range(0, 6):
            clear()
            self._print_menu(0)
            print(f"{G}                                 Starting COBALT" + ("." * i))
            sleep(0.5)
        print(f"\n{G}                         Access Granted >> System Starting")
        sleep(2)

    def start(self):
        current_selection = 0
        while True:
            self._print_menu(current_selection)
            key = get_key()
            if key == 'UP':
                current_selection = (current_selection - 1) % len(self.options)
            elif key == 'DOWN':
                current_selection = (current_selection + 1) % len(self.options)
            elif key == 'ENTER':
                if current_selection == 0:
                    self._Load_Menu()
                    break
                elif current_selection == 1:
                    clear()
                    print(f"{Fore.GREEN} Accessing COBALT Help System...\n [DarkHats Updater é lindo]")
                    sleep(5)
                elif current_selection == 2:
                    clear()
                    print(f"{Fore.GREEN} Shutting down COBALT...")
                    sleep(2)
                    break

    def _neofetch(self):
        clear()
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
        for i in range(max_lenght):
            l_l = DarkHat[i] if i < len(DarkHat) else " " * 75
            l_r = info_sis[i] if i < len(info_sis) else ""
            print(f"  {Fore.GREEN}{l_l}{Style.RESET_ALL}        {l_r}")

    def _welcome_screen(self):
        console = Console()
        user_name = getpass.getuser().upper()
        ascii_art = (
            r" ____________________________________________" "\n"
            r" __  ____/_  __ \__  __ )__    |__  /___  __/" "\n"
            r" _  /    _  / / /_  __  |_  /| |_  / __  /   " "\n"
            r" / /___  / /_/ /_  /_/ /_  ___ |  /___  /    " "\n"
            r" \____/  \____/ /_____/ /_/  |_/_____/_/     "
        )
        top_text = Text()
        top_text.append(ascii_art, style="bold green")
        top_text.append("\n\n           B E M - V I N D O\n", style="bold white")
        top_text.append(f"             Usuario: {user_name}\n\n", style="dim green")
        clear()
        spinner = Spinner("dots", text="[green]Preparando o ambiente COBALT...", style="bold green")
        with Live(console=console, refresh_per_second=20) as live:
            for _ in range(75):
                content_loading = Group(top_text, Align.center(spinner), Text("\n\n"))
                panel_loading = Panel(content_loading, border_style="green", padding=(3, 16), title="[bold green]System Boot[/bold green]")
                live.update(Align.center(panel_loading))
                sleep(0.05)
        clear()
        ready_text = Text.from_markup("[bold green]Ambiente pronto.[/bold green]\n\n[bold white]> PRESSIONE ESPAÇO PARA CONTINUAR <[/bold white]", justify="center")
        content_ready = Group(top_text, ready_text)
        panel_ready = Panel(content_ready, border_style="green", padding=(3, 16), title="[bold green]Sistema Pronto[/bold green]")
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
            "Verificando a integridade do Cobalt Core X-12...",
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
            "Security Bypass": "Complete uma task: placeholder insano.",
            "Security Analytic": "Complete 3 auditorias de sistema.",
            "Mr.Robot": "Complete o final bom.",
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
            "Security Analytic": False,
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
        preserved_rebirths = current_data.get("rebirths", 0) + 1

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
        self.total_rebirths = self.stats.get("rebirths", 0)

        saved_badges = saved.get("badges", {})
        self.badges = {
            "Social Engineer":   saved_badges.get("Social Engineer", False)   or (self.stats.get("tasks", 0) >= 2),
            "Hardware Specialist": saved_badges.get("Hardware Specialist", False) or (self.stats.get("chests", 0) >= 5),
            "Security Bypass":   saved_badges.get("Security Bypass", False)   or (self.stats.get("tasks", 0) >= 1),
            "Reverse Engineer":  saved_badges.get("Reverse Engineer", False)  or (self.stats.get("tasks", 0) >= 10),
            "Security Analytic": saved_badges.get("Security Analytic", False) or (self.stats.get("tasks", 0) >= 3),
            "Mr.Robot":          saved_badges.get("Mr.Robot", False),
            "Normal Ending":     saved_badges.get("Normal Ending", False),
            "Good Ending":       saved_badges.get("Good Ending", False),
            "Bad Ending":        saved_badges.get("Bad Ending", False),
            "???":               saved_badges.get("???", False),
            "DarkHats":          saved_badges.get("DarkHats", False),
        }

        docs = [
            {"name": "..", "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
        ]

        lvl = self.player_level
        if lvl >= 1:
            info = lore_files["Notas.txt"]
            docs.append({
                "name": "Notas.txt", "type": "FILE", "icon": "📄",
                "color": info["color"], "preview": info["preview"],
            })
        if lvl >= 2:
            for fname in ("Diário.txt", "Morgan.txt"):
                info = lore_files[fname]
                docs.append({
                    "name": fname, "type": "FILE", "icon": "📄",
                    "color": info["color"], "preview": info["preview"],
                })

        if lvl >= 3:
            for fname in ("Relato.txt", "Morgan2.txt"):
                info = lore_files[fname]
                docs.append({
                    "name": fname, "type": "FILE", "icon": "📄",
                    "color": info["color"], "preview": info["preview"],
                })

        if lvl >= 4:
            for fname in ("Lembranças.txt", "A Raiz.txt"):
                info = lore_files[fname]
                docs.append({
                    "name": fname, "type": "FILE", "icon": "📄",
                    "color": info["color"], "preview": info["preview"],
                })
        if lvl >= 5:
            info = lore_files["NULL.txt"]
            docs.append({
                "name": "NULL.txt", "type": "FILE", "icon": "📄",
                "color": info["color"], "preview": info["preview"],
            })
        if lvl >= 6:
            info = lore_files["SHEOL.txt"]
            docs.append({
                "name": "SHEOL.txt", "type": "FILE", "icon": "📄",
                "color": info["color"], "preview": info["preview"],
            })

        paste_achievements = [
            {"name": "..", "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
        ]
        for name, unlocked in self.badges.items():
            color = Fore.YELLOW if unlocked else Fore.LIGHTBLACK_EX
            paste_achievements.append({
                "name": f" {name}", "type": "BADGE", "icon": "🏅",
                "color": color, "raw_name": name
            })

        self.file_system = {
            "root": [],

            "root/Documentos": docs,

            "root/Ajuda": [
                {"name": "..", "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
                {"name": "DarkHats.txt",   "type": "FILE", "icon": "📄", "color": Fore.WHITE},
                {"name": "Conquistas.txt", "type": "FILE", "icon": "📄", "color": Fore.WHITE},
            ],

            "root/Configurações": [
                {"name": "..",                  "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
                {"name": "Contribuidores.flat", "type": "FILE", "icon": "📄", "color": Fore.WHITE},
                {"name": "Admin.db",            "type": "FILE", "icon": "📄", "color": Fore.WHITE},
            ],

            "root/DarkHats": [
                {"name": "..", "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
            ],

            "root/Jogos": [
                {"name": "..",               "type": "BACK", "icon": "🔙",  "color": Fore.YELLOW, "target": "root"},
                {"name": "SnakeGame.flat",   "type": "EXEC", "icon": "⚙️", "color": Fore.WHITE},
                {"name": "RobuxGen_v2.exe",  "type": "EXEC", "icon": "⚙️", "color": Fore.WHITE},
            ],

            "root/Conquistas": paste_achievements,
        }

        if lvl >= 1:
            self.file_system["root"] = [
                {"name": "DarkHats",      "type": "DIR",  "icon": "📁", "color": Fore.WHITE, "target": "root/DarkHats"},
                {"name": "Jogos",         "type": "DIR",  "icon": "📁", "color": Fore.WHITE, "target": "root/Jogos"},
                {"name": "Conquistas",    "type": "DIR",  "icon": "📁", "color": Fore.WHITE, "target": "root/Conquistas"},
                {"name": "Documentos",    "type": "DIR",  "icon": "📁", "color": Fore.WHITE, "target": "root/Documentos"},
                {"name": "Ajuda",         "type": "DIR",  "icon": "📁", "color": Fore.WHITE, "target": "root/Ajuda"},
                {"name": "Configurações", "type": "DIR",  "icon": "📁", "color": Fore.WHITE, "target": "root/Configurações"},
                {"name": "Desligar",      "type": "EXIT", "icon": " ⏻", "color": Fore.RED},
            ]
        else:
            self.file_system["root"] = [
                {"name": "Instruções.txt", "type": "FILE", "icon": "📄", "color": Fore.WHITE},
            ]

        if lvl >= 1:
            self.route_level = min(5, max(1, len(self.route_history) + 1))
            choices = sorted(
                self.route_manager.get_choices_for_level(self.route_level),
                key=lambda item: item['display_position']
            )
            self.file_system["root/DarkHats"] = [
                {"name": "..", "type": "BACK", "icon": "🔙", "color": Fore.YELLOW, "target": "root"},
                {"name": f">> Nível {self.route_level}/5", "type": "INFO", "icon": "💾", "color": Fore.CYAN},
                {"name": "───────────────────────", "type": "INFO", "icon": "", "color": Fore.LIGHTBLACK_EX},
            ]
            for choice in choices:
                numero = choice['display_position'] + 1
                self.file_system["root/DarkHats"].append({
                    "name": f"[{numero}] {choice['mission']}",
                    "type": "ROUTE",
                    "icon": "⚙️ ",
                    "color": Fore.WHITE,
                    "route": choice['route'],
                    "mission": choice['mission'],
                    "level": choice['level'],
                    "display_position": choice['display_position'],
                })
            self.file_system["root/DarkHats"].append(
                {"name": "───────────────────────", "type": "INFO", "icon": "", "color": Fore.LIGHTBLACK_EX}
            )

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
        self.route_manager.save_progress(
            self.badges, self.route_history, self.current_ending,
            level=self.player_level,
            tasks=self.stats.get('tasks', 0),
            chests=self.stats.get('chests', 0),
            rebirths=self.stats.get('rebirths', 0),
            inventory=getattr(self, 'inventory', [])
        )
        return self.current_ending


    def draw(self):
        self._system_archives_update()
        clear()
        C_BORDER = _menu_border_color(self.player_level)
        C_TITLE  = C_BORDER
        print(f"{C_BORDER}╔{'═' * self.inner_w}╗")
        title = f" ■ COBALT FILE EXPLORER [{self.current_dir}]"
        pad_title = self.inner_w - visual_width(title)
        print(f"{C_BORDER}║{C_TITLE}{title}{' ' * pad_title}{C_BORDER}║")
        print(f"{C_BORDER}╠{'═' * self.inner_w}╣")
        for i, f in enumerate(self.files):
            is_selected = (i == self.cursor)
            arrow      = "►" if is_selected else " "
            text_color = Fore.GREEN if is_selected else f['color']
            item_string   = f" {arrow} {f['icon']} {f['name']}"
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
                f"Baús: {self.stats.get('chests', 0)} "
                #f"Rebirths: {self.stats.get('rebirths', 0)}"
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
        ftype = file.get('type')
        name  = (file.get('name') or "").strip()

        if ftype in ("DIR", "BACK"):
            self.current_dir = file['target']
            self.files = self.file_system[self.current_dir]
            self.cursor = 0
            return

        if ftype == "ROUTE":
            self._open_route_mission(file)

        elif ftype == "EXEC" and name == "SnakeGame.flat":
            self._open_snake_game()

        elif ftype == "BADGE":
            self._open_badge(file['raw_name'])

        elif ftype == "FILE" and name == "Instruções.txt":
            self._open_tutorial()

        elif ftype == "EXEC" and name == "boss.flat":
            self._open_boss()

        elif ftype == "FILE" and name in lore_files:
            self._open_lore_file(name)

        elif ftype == "FILE" and name == "DarkHats.txt":
            self._open_DarkHatsText()

        elif ftype == "EXEC" and name == "RobuxGen_v2.exe":
            from Game.Main.Games.RobuxGame import robux_game
            robux_game()

        elif ftype == "FILE" and name == "ResetData.flat":
            clear()
            cText("⚠  Tem certeza que deseja resetar os dados? (S/N)", "red")
            confirm = input("  >> ").strip().upper()
            if confirm in ("S", "SIM", "Y", "YES"):
                self.reset_game_data()
                cText("✓  Dados resetados com sucesso!", "green")
            else:
                cText("  Reset cancelado.", "warn")
            sleep(2)

        elif ftype == "FILE" and name == "Logs.db":
            self._open_logs()

        elif ftype == "FILE" and name == "Admin.db":
            self._open_admins()

        elif ftype == "FILE" and name == "Conquistas.txt":
            self._open_achievements()

        elif ftype == "FILE" and name == "Contribuidores.flat":
            self._open_contribuitors()

        elif ftype == "EXIT" and name == "Desligar":
            clear()
            print(f"{Fore.RED}[!] Desligando o sistema COBALT...{Style.RESET_ALL}")
            sleep(1.5)
            sys.exit()

    def _open_lore_file(self, file_name: str):
        info  = lore_files[file_name]
        lines = info["lines"]
        color = info.get("color", Fore.WHITE)

        clear()
        print(f"{Fore.YELLOW}[!] Abrindo {file_name}...{Style.RESET_ALL}")
        sleep(0.4)
        clear()

        border_color = color if color != Fore.WHITE else Fore.GREEN
        w = 48

        print(f"{border_color}╔{'═' * w}╗")

        header = f" 📄  {file_name}"
        pad_h  = w - visual_width(header)
        print(f"{border_color}║{Fore.WHITE}{header}{' ' * pad_h}{border_color}║")
        print(f"{border_color}╠{'═' * w}╣")

        for line in lines:
            pad = w - visual_width(line)
            if pad < 0:
                line = line[:w - 1]
                pad  = 0
            print(f"{border_color}║{color}{line}{' ' * pad}{border_color}║")

        print(f"{border_color}╚{'═' * w}╝{Style.RESET_ALL}")
        input(f"\n  {Fore.LIGHTBLACK_EX}[ Pressione ENTER para retornar ]{Style.RESET_ALL}")


    def _open_darkhats(self):
        clear()
        print(f"{Fore.CYAN}[*] Extraindo darkhats.flat...{Style.RESET_ALL}")
        sleep(1)
        print(f"{Fore.GREEN}[*] Permissões do root concedidas.{Style.RESET_ALL}")
        sleep(1)

        from Game.Main.DarkHatsGame import DarkHatsGame
        game = DarkHatsGame()
        game.route_choice    = getattr(self, 'selected_route', 'BAD')
        game.mission_name    = getattr(self, 'selected_mission_name', None)
        game.Player.Level    = self.player_level
        sleep(2)
        dih = COBALT(player_level=self.player_level)
        dih.start()
        game.start()

        saved = self.route_manager.load_progress(self.badges)
        self.player_level  = int(saved.get("level", 1))
        self.route_history = list(saved.get('route_history', self.route_history))

        clear()
        print(f"{Fore.YELLOW}[!] darkhats.flat finalizado. Retornando para o COBALT...{Style.RESET_ALL}")
        sleep(2)

    def _open_route_mission(self, file):
        route_name   = str(file.get('route', 'BAD')).upper().strip()
        mission_name = str(file.get('mission', 'Unknown')).strip()
        level        = int(file.get('level', self.route_level))

        FINAL_MISSIONS = {
            "Cláusula Final": "BAD",
            "Eco Final":      "TRUE",
            "Preço Final":    "GOOD",
        }

        if mission_name in FINAL_MISSIONS:
            self._open_final_mission(mission_name, route_name)
            return

        clear()
        print(f"{Fore.CYAN}[*] Carregando rota: {route_name} missão: {mission_name}...{Style.RESET_ALL}")
        sleep(1)

        saved = self.route_manager.load_progress(self.badges)
        mission_history = list(saved.get('mission_history', [])) + [mission_name]

        self.selected_route       = route_name
        self.selected_mission_name = mission_name
        self.route_history        = list(saved.get('route_history', self.route_history)) + [route_name]
        self.current_ending       = self.ending_manager.evaluate(self.route_history)
        next_level = min(5, len(self.route_history) + 1)
        self.route_manager.save_progress(
            self.badges, self.route_history, self.current_ending,
            mission_history, level=next_level,
            tasks=self.stats.get('tasks', 0),
            chests=self.stats.get('chests', 0),
            rebirths=self.stats.get('rebirths', 0),
            inventory=getattr(self, 'inventory', [])
        )
        self.player_level = next_level
        self._open_darkhats()

    def _open_final_mission(self, mission_name, route_name):
        clear()
        print(f"{Fore.CYAN}[*] Carregando missão final: {mission_name}...{Style.RESET_ALL}")
        sleep(1.5)

        if mission_name == "Eco Final":
            from Game.Missions.EcoFinal import run as final_run
        elif mission_name == "Cláusula Final":
            from Game.Missions.ClausulaFinal import run as final_run
        elif mission_name == "Preço Final":
            from Game.Missions.PrecoFinal import run as final_run
        else:
            return

        saved           = self.route_manager.load_progress(self.badges)
        mission_history = list(saved.get('mission_history', [])) + [mission_name]
        route_history   = list(saved.get('route_history', self.route_history)) + [route_name]
        ending          = self.ending_manager.evaluate(route_history)

        self.route_manager.save_progress(
            self.badges, route_history, ending,
            mission_history, level=5,
            tasks=self.stats.get('tasks', 0),
            chests=self.stats.get('chests', 0),
            rebirths=self.stats.get('rebirths', 0),
            inventory=getattr(self, 'inventory', [])
        )

        self.route_history  = route_history
        self.current_ending = ending
        self.player_level   = 5

        final_run(route_history=route_history)

        saved             = self.route_manager.load_progress(self.badges)
        self.player_level = int(saved.get('level', 5))
        self.route_history = list(saved.get('route_history', route_history))

        clear()
        print(f"{Fore.YELLOW}[!] Missão final concluída. Retornando ao COBALT...{Style.RESET_ALL}")
        sleep(2)

    def _open_badge(self, badge_name):
        clear()
        unlocked     = self.badges.get(badge_name, False)
        description  = self.desc_badges.get(badge_name, "Sem informações providas.")
        border       = Fore.YELLOW if unlocked else Fore.LIGHTBLACK_EX
        status_text  = f"{Fore.GREEN}[ DESBLOQUEADO ]" if unlocked else f"{Fore.RED}[ BLOQUEADO ]"

        print(f"{border}╔══════════════════════════════════════════════╗")
        line_1 = f" {Fore.WHITE}🏅 DETALHES DA CONQUISTA"
        pad_1  = 46 - visual_width(line_1)
        print(f"{border}║{line_1}{' ' * pad_1}{border}║")
        print(f"{border}╠══════════════════════════════════════════════╣")
        line_2 = f" {Fore.WHITE}TITULO:  {Fore.CYAN}{badge_name}"
        pad_2  = 46 - visual_width(line_2)
        print(f"{border}║{line_2}{' ' * pad_2}{border}║")
        line_3 = f" {Fore.WHITE}STATUS: {status_text}"
        pad_3  = 46 - visual_width(line_3)
        print(f"{border}║{line_3}{' ' * pad_3}{border}║")
        print(f"{border}║{' ' * 46}║")
        line_5 = f" {Fore.WHITE}COMO DESBLOQUEAR:"
        pad_5  = 46 - visual_width(line_5)
        print(f"{border}║{line_5}{' ' * pad_5}{border}║")
        truncated_desc = description[:44]
        line_6 = f" {Fore.LIGHTBLACK_EX}{truncated_desc}"
        pad_6  = 46 - visual_width(line_6)
        print(f"{border}║{line_6}{' ' * pad_6}{border}║")
        print(f"{border}╚══════════════════════════════════════════════╝{Style.RESET_ALL}")
        input(f"\n  {Fore.WHITE}[ Pressione ENTER para voltar ]{Style.RESET_ALL}")


    def _open_tutorial(self):
        clear()
        message = (
            f"Olá, {getpass.getuser()}.\n\n"
            f"Sistema inicializado com sucesso. Prazer, sou Arthur.\n"
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
        input(f"\n  {Fore.LIGHTBLACK_EX}[ Pressione ENTER para voltar ]{Style.RESET_ALL}")
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
            from Game.Main.Games.SnakeGame import snake_game
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
        pad_1  = 44 - visual_width(line_1)
        print(f"║{line_1}{' ' * pad_1}{Fore.RED}║")
        print(f"╠════════════════════════════════════════════╣")
        line_2 = " Connecting to serve..."
        pad_2  = 44 - visual_width(line_2)
        print(f"║{line_2}{' ' * pad_2}║")
        line_3 = " Executing."
        pad_3  = 44 - visual_width(line_3)
        print(f"║{line_3}{' ' * pad_3}║")
        print(f"╚════════════════════════════════════════════╝{Style.RESET_ALL}")
        sleep(2)
        from Game.Main.DarkHatsGame import DarkHatsGame
        game = DarkHatsGame()
        game.Player.Level = self.player_level
        game.start()
        self.player_level = game.Player.Level
        clear()


    def _open_contribuitors(self):
        clear()
        print(f"{Fore.YELLOW}[!] ABRINDO Contribuidores.flat...{Style.RESET_ALL}")
        sleep(0.5)
        clear()
        rows = [" Hydro", " Apogavi", " DiscorDANdo", " Guilherme"]
        w    = 50
        print(f"{Fore.GREEN}╔{'═' * w}╗")
        h = f" {Fore.GREEN}✏️  VISUALIZADOR DE TEXTO: Contribuidores.flat"
        print(f"{Fore.GREEN}║{h}{' ' * (w - visual_width(h))}{Fore.GREEN}║")
        print(f"{Fore.GREEN}╠{'═' * w}╣")
        for r in rows:
            print(f"{Fore.GREEN}║{r}{' ' * (w - visual_width(r))}║")
        print(f"{Fore.GREEN}╚{'═' * w}╝{Style.RESET_ALL}")
        input(f"\n  {Fore.LIGHTBLACK_EX}[ Pressione ENTER para retornar ]{Style.RESET_ALL}")

    def _open_admins(self):
        clear()
        print(f"{Fore.YELLOW}[!] Abrindo Admin.db...{Style.RESET_ALL}")
        sleep(0.5)
        clear()
        print(f"{Fore.GREEN}╔════════════════════════════════════════════╗")
        line_1 = f" {Fore.GREEN}⚙️  VISUALIZADOR DE TEXTO: Admin.db"
        pad_1  = 44 - visual_width(line_1)
        print(f"{Fore.GREEN}║{line_1}{' ' * pad_1}{Fore.GREEN}║")
        print(f"{Fore.GREEN}╠════════════════════════════════════════════╣")
        line_2 = " Você não é um adminstrador!"
        pad_2  = 44 - visual_width(line_2)
        print(f"{Fore.GREEN}║{line_2}{' ' * pad_2}║")
        print(f"{Fore.GREEN}╚════════════════════════════════════════════╝{Style.RESET_ALL}")
        input(f"\n  {Fore.LIGHTBLACK_EX}[ Pressione ENTER para retornar ]{Style.RESET_ALL}")

    def _open_logs(self):
        clear()
        print(f"{Fore.YELLOW}[!] ABRINDO logs.db...{Style.RESET_ALL}")
        sleep(0.5)
        clear()
        for _ in range(15):
            trash = os.urandom(30).hex()
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