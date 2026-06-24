import os
import sys
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
from rich import box
from colorama import Fore

console = Console()

COLORAMA_TO_RICH = {
    Fore.GREEN:   "green",
    Fore.RED:     "red",
    Fore.CYAN:    "cyan",
    Fore.YELLOW:  "yellow",
    Fore.MAGENTA: "magenta",
    Fore.BLUE:    "blue",
    Fore.WHITE:   "white",
}

def to_rich_color(colorama_color):
    return COLORAMA_TO_RICH.get(colorama_color, "green")

def make_bar(current, maximum, width=20, fill='━', empty='─'):
    if maximum <= 0:
        return empty * width
    filled = max(0, min(width, int((current / maximum) * width)))
    return fill * filled + empty * (width - filled)

def get_key():
    if os.name == 'nt':
        import msvcrt
        key = msvcrt.getch()
        if key == b'\xe0': 
            special = msvcrt.getch()
            if special == b'H': return 'UP'
            if special == b'P': return 'DOWN'
            if special == b'K': return 'LEFT'  
            if special == b'M': return 'RIGHT'
        elif key in (b'\r', b'\n'):
            return 'ENTER'
        elif key == b' ':
            return 'SPACE'
        return None
    else:
        import tty, termios, sys
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
                    if ch3 == 'C': return 'RIGHT' 
                    if ch3 == 'D': return 'LEFT'  
            elif ch in ('\r', '\n'):
                return 'ENTER'
            elif ch == ' ':
                return 'SPACE'
            return None
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


from rich.table import Table

def display_battle_ui(player_integrity, max_integrity, player_defense, available_attacks, ui_color, player_name="hydrogostosao", class_name="sla", selected_index=0):
        color = to_rich_color(ui_color)

        hp_bar  = make_bar(player_integrity, max_integrity, width=20)
        def_bar = make_bar(player_defense, 100, width=20)
        hp_pct  = f"{int(player_integrity)}/{int(max_integrity)}"
        def_pct = f"{int(player_defense)}%"

        hp_style = "green" if (player_integrity / max_integrity) > 0.3 else "red"
        
        status_table = Table.grid(expand=True, padding=(0, 1))
        status_table.add_column(style="dim", width=5) 
        status_table.add_column()                     
        status_table.add_column(justify="right")      

        status_table.add_row("HP", Text(hp_bar, style=hp_style), hp_pct)
        status_table.add_row("DEF", Text(def_bar, style="blue"), def_pct)
        status_table.add_row("", "", "") 
        
        status_table.add_row("[dim]LAT", "[bold cyan]━━━┯━━━━[/]", "[dim]12ms[/]") 
        status_table.add_row("[dim]NODE", "[bold green]ONLINE[/]", "[dim]v1.0.4[/]")

        header_text = Text()
        header_text.append(f"{player_name}", style="bold white")
        header_text.append(f" [{class_name}]", style=f"bold {color}")
        
        player_panel = Panel(
            status_table, 
            title=header_text,
            title_align="left",
            box=box.ROUNDED, 
            border_style=color, 
            padding=(1, 2), 
            expand=True 
        )

        top_layout = Table.grid(padding=(0, 1), expand=True)
        top_layout.add_column(ratio=6) 
        top_layout.add_column(ratio=4, justify="right") 
        top_layout.add_row("", player_panel)

        attacks = list(available_attacks)
        exploit_grid = Table.grid(padding=(0, 1), expand=True)
        exploit_grid.add_column(ratio=1)
        exploit_grid.add_column(ratio=1)

        current_idx = 0
        for i in range(0, max(len(attacks), 2), 2):
            left_att  = attacks[i]     if i < len(attacks)     else ''
            right_att = attacks[i + 1] if i + 1 < len(attacks) else ''

            def make_btn(att, idx):
                if not att:
                    return ""
                if idx == selected_index:
                    b_style = f"bold {color}"
                    t_style = f"bold {color}"
                else:
                    b_style = "dim"
                    t_style = "dim white"

                t = Text(att.upper(), style=t_style, justify="center", overflow="ellipsis", no_wrap=True)
                return Panel(t, box=box.ROUNDED, border_style=b_style, expand=True)

            exploit_grid.add_row(make_btn(left_att, current_idx), make_btn(right_att, current_idx + 1))
            current_idx += 2

        exploit_panel = Panel(
            exploit_grid,
            title=Text("EXPLOITS DISPONÍVEIS", style="dim"),
            title_align="left",
            box=box.ROUNDED,
            border_style=color,
            padding=(1, 2),
            expand=True
        )

        prompt_side = Text()
        prompt_side.append(f"O que {player_name}\nvai fazer?\n\n\n", style="dim white")
        prompt_side.append(">> INITIALIZE PROTOCOL...", style=color)

        prompt_panel = Panel(
            prompt_side, 
            box=box.ROUNDED, 
            border_style=color, 
            padding=(1, 2), 
            expand=True
        )

        bottom_layout = Table.grid(padding=(0, 1), expand=True)
        bottom_layout.add_column(ratio=6)
        bottom_layout.add_column(ratio=4) 
        bottom_layout.add_row(exploit_panel, prompt_panel)

        console.print(top_layout)
        console.print()
        console.print(bottom_layout)
        console.print(Text("\n  COBALT MAINFRAME v1.0.4  |  SYSTEM NODE OVERVIEW", style="dim black on black"), justify="left")

def enemy_life(current_enemy):
    name = str(current_enemy.Name)
    if len(name) > 24: name = name[:21] + "..."
    
    enemy_def = getattr(current_enemy, 'Defense', 0)
    
    hp_b = make_bar(current_enemy.Health, current_enemy.MaxHealth, width=25)
    def_b = make_bar(enemy_def, 100, width=25)
    
    hp_pct = f"{int(current_enemy.Health)}/{int(current_enemy.MaxHealth)}"
    def_pct = f"{int(enemy_def)}%"

    enemy_text = Text()
    enemy_text.append(name, style="bold red")
    enemy_text.append(" [VIRUS]", style="bold red")
    enemy_text.append("  NV.1\n\n", style="dim red") 
    
    enemy_text.append("HP  ", style="dim")
    enemy_text.append(f"{hp_b}", style="red")
    enemy_text.append(f"  {hp_pct}\n", style="red")

    enemy_text.append("DEF ", style="dim")
    enemy_text.append(f"{def_b}", style="blue") 
    enemy_text.append(f"  {def_pct}", style="blue")

    console.print(Panel(
        enemy_text, 
        box=box.ROUNDED, 
        border_style="red", 
        padding=(1, 2), 
        expand=False
    ))
    console.print()
