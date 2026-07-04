import os
import random
from time import sleep
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()

LAZY_MESSAGES = [
    "Estou com preguiça.",
    "Hoje não.",
    "Talvez amanhã.",
    "To com dor de cabelo.",
    "Nah.",
    "To jogando SAB.",
]

CLOSED_MESSAGES = [
    "Está fechado.",
    "Sem expediente hoje.",
    "Voltam na segunda.",
    "Porta trancada.",
    "Sistema offline.",
]


def get_key():
    if os.name == 'nt':
        import msvcrt
        key = msvcrt.getch()
        if key == b'\xe0':
            special = msvcrt.getch()
            if special == b'H':
                return 'UP'
            if special == b'P':
                return 'DOWN'
        elif key in (b'\r', b'\n'):
            return 'ENTER'
        return None
    else:
        import tty
        import termios
        import sys
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
            if ch == '\x1b':
                ch2 = sys.stdin.read(1)
                if ch2 == '[':
                    ch3 = sys.stdin.read(1)
                    if ch3 == 'A':
                        return 'UP'
                    if ch3 == 'B':
                        return 'DOWN'
            elif ch in ('\r', '\n'):
                return 'ENTER'
            return None
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def render_choice_menu(title, description, options, cursor, route):
    console.clear()

    color_map = {"TRUE": "cyan", "GOOD": "green", "BAD": "red"}
    color = color_map.get(route, "green")

    header = Text()
    header.append(f"\n{description}\n", style="dim white")

    console.print(Panel(
        header,
        title=Text(f" {title} ", style=f"bold {color}"),
        title_align="left",
        box=box.SQUARE,
        border_style=color,
        padding=(0, 2)
    ))
    console.print()

    grid = Table.grid(padding=(0, 1), expand=True)
    grid.add_column(ratio=1)

    for i, opt in enumerate(options):
        is_sel = i == cursor
        arrow = "► " if is_sel else "  "
        t_style = f"bold {color}" if is_sel else "dim white"
        b_style = color if is_sel else "dim"

        t = Text(f"{arrow}{opt['label']}", style=t_style)
        if opt.get("sublabel"):
            t.append(f"\n  {opt['sublabel']}", style="dim")

        grid.add_row(Panel(t, box=box.SQUARE, border_style=b_style, expand=True))

    console.print(Panel(
        grid,
        title=Text("O QUE FAZER?", style="dim"),
        title_align="left",
        box=box.SQUARE,
        border_style=color,
        padding=(0, 1)
    ))
    console.print(Text("  [↑↓] Navegar  [ENTER] Confirmar", style="dim"))


def render_result(text, style="green", pause=2.5):
    console.clear()
    console.print(Panel(
        Text(f"\n{text}\n", style=style),
        box=box.SQUARE,
        border_style=style,
        padding=(0, 2)
    ))
    sleep(pause)


def blocked_message(kind="closed"):
    if kind == "closed":
        msg = random.choice(CLOSED_MESSAGES)
    else:
        msg = random.choice(LAZY_MESSAGES)

    console.clear()
    console.print(Panel(
        Text(f"\n  {msg}\n", style="dim red"),
        box=box.SQUARE,
        border_style="dim red",
        padding=(0, 2)
    ))
    sleep(2)


def navigate_menu(title, description, options, route):
    cursor = 0
    while True:
        render_choice_menu(title, description, options, cursor, route)
        key = get_key()
        if key == 'UP':
            cursor = (cursor - 1) % len(options)
        elif key == 'DOWN':
            cursor = (cursor + 1) % len(options)
        elif key == 'ENTER':
            return options[cursor]["id"]
