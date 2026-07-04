from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
from rich import box
import os

console = Console()

# ==========================================
# DEFINIÇÃO DAS CLASSES
# ==========================================

CLASSES = [
    {
        "id": "1",
        "name": "HACKER",
        "input": ["HACKER", "1"],
        "focus": "Raw damage & system exploitation.",
        "description": (
            "The Hacker is a pure offensive class, specialized in breaking "
            "through enemy defenses with brute force and raw system attacks. "
            "High damage output, low defense. Best for aggressive players."
        ),
        "stats": {"Integrity": "High", "Defense": "Low", "Regen": "None"},
        "badge_required": None,
    },
    {
        "id": "2",
        "name": "SECURITY ANALYTIC",
        "input": ["SECURITY ANALYTIC", "2"],
        "focus": "Ironclad defense & node integrity.",
        "description": (
            "The Security Analytic excels at protecting systems and sustaining "
            "long battles. Passive defense bonuses and integrity restoration "
            "make this class ideal for cautious players."
        ),
        "stats": {"Integrity": "Medium", "Defense": "High", "Regen": "Low"},
        "badge_required": "Security Analytic",
        "locked_msg": "Complete a conquista 'Security Analytic' para desbloquear.",
    },
    {
        "id": "3",
        "name": "SOCIAL ENGINEER",
        "input": ["SOCIAL ENGINEER", "3"],
        "focus": "Manipulation, regen & bypass.",
        "description": (
            "The Social Engineer wins battles through psychological warfare "
            "and resource manipulation. Cooldown management and turn skipping "
            "give this class a unique edge in prolonged conflicts."
        ),
        "stats": {"Integrity": "Medium", "Defense": "Medium", "Regen": "High"},
        "badge_required": "Social Engineer",
        "locked_msg": "Complete a conquista 'Social Engineer' para desbloquear.",
    },
    {
        "id": "4",
        "name": "REVERSE ENGINEER",
        "input": ["REVERSE ENGINEER", "4"],
        "focus": "Decompilation & adaptive attacks.",
        "description": (
            "The Reverse Engineer can dismantle enemy systems and turn their "
            "own tools against them. A complex class that rewards players who "
            "understand the mechanics deeply."
        ),
        "stats": {"Integrity": "Medium", "Defense": "Low", "Regen": "None"},
        "badge_required": "Reverse Engineer",
        "locked_msg": "Complete a conquista 'Reverse Engineer' para desbloquear.",
    },
    {
        "id": "5",
        "name": "HARDWARE SPECIALIST",
        "input": ["HARDWARE SPECIALIST", "5"],
        "focus": "Hardware manipulation & optimization.",
        "description": (
            "The Hardware Specialist operates at the physical layer of systems, "
            "dealing consistent damage while optimizing their own stats over time. "
            "Unique buff mechanics make this class grow stronger mid-battle."
        ),
        "stats": {"Integrity": "High", "Defense": "Medium", "Regen": "None"},
        "badge_required": "Hardware Specialist",
        "locked_msg": "Complete a conquista 'Hardware Specialist' para desbloquear.",
    },
    {
        "id": "6",
        "name": "SECURITY BYPASSER",
        "input": ["SECURITY BYPASSER", "6"],
        "focus": "Bypassing security measures & stealth.",
        "description": (
            "The Security Bypasser specializes in ignoring enemy defenses "
            "entirely. Stealth-based attacks deal true damage, making this class "
            "the bane of high-defense enemies."
        ),
        "stats": {"Integrity": "Low", "Defense": "Low", "Regen": "Medium"},
        "badge_required": "Security Bypass",
        "locked_msg": "Complete a conquista 'Security Bypass' para desbloquear.",
    },
    {
        "id": "CV01",
        "name": "HATSUNE MIKU",
        "input": ["HATSUNE MIKU", "CV01"],
        "focus": "Sonic attacks & rhythm-based combos.",
        "description": (
            "A secret class unlocked through a hidden badge. "
            "Miku attacks using sound frequencies and musical patterns, "
            "dealing massive burst damage with unique combo mechanics."
        ),
        "stats": {"Integrity": "Medium", "Defense": "Low", "Regen": "Medium"},
        "badge_required": "Mr.Robot",
        "locked_msg": "Complete a conquista 'Mr.Robot' para desbloquear.",
    },
    {
        "id": "LAMBDA",
        "name": "LAMBDA",
        "input": ["LAMBDA"],
        "focus": "Unknown.",
        "description": (
            "A class shrouded in mystery. Its attacks defy conventional "
            "classification. Only those who've seen everything will understand it."
        ),
        "stats": {"Integrity": "???", "Defense": "???", "Regen": "???"},
        "badge_required": "???",
        "locked_msg": "Complete a conquista '???' para desbloquear.",
    },
]

STATS_COLOR = {
    "High":   "bold green",
    "Medium": "bold yellow",
    "Low":    "bold red",
    "None":   "dim",
    "???":    "dim magenta",
}

PER_PAGE = 6


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
            if special == b'K':
                return 'LEFT'
            if special == b'M':
                return 'RIGHT'
        elif key in (b'\r', b'\n'):
            return 'ENTER'
        elif key == b' ':
            return 'SPACE'
        elif key == b'\x1b':
            return 'ESC'
        return None
    else:
        import tty, termios, sys
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
                    if ch3 == 'C':
                        return 'RIGHT'
                    if ch3 == 'D':
                        return 'LEFT'
                else:
                    return 'ESC'
            elif ch in ('\r', '\n'):
                return 'ENTER'
            return None
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


# ==========================================
# RENDERIZADORES
# ==========================================


def render_class_list(classes_page, cursor, badges, page, total_pages):
    console.clear()

    title = Text()
    title.append(" ■ ", style="green")
    title.append("CLASS SELECTION", style="bold white")
    title.append(f"  —  Page {page}/{total_pages}", style="dim")

    rows = Table.grid(padding=(0, 1), expand=True)
    rows.add_column(ratio=1)
    rows.add_column(ratio=1)

    panels = []
    for i, cls in enumerate(classes_page):
        is_locked = cls.get("badge_required") and not badges.get(cls["badge_required"], False)
        is_selected = i == cursor
        arrow = "► " if is_selected else "  "

        if is_locked:
            name_style = "bright_black"
            border_style = "bright_black"
            class_text = Text(f"{arrow}🔒 {cls['name']}", style=name_style)
            class_text.append(f"\n    {cls.get('locked_msg', 'Locked.')}", style="dim")
        else:
            name_style = "bright_white" if is_selected else "white"
            border_style = "green" if is_selected else "dim"

            class_text = Text()
            class_text.append(f"{arrow}{cls['name']}", style=name_style)
            class_text.append(f"\n    {cls['focus']}", style="dim")

        panels.append(Panel(class_text, box=box.SQUARE, border_style=border_style, expand=True))

    for row in range(3):
        left = panels[row] if row < len(panels) else Panel(Text(""), box=box.SQUARE, border_style="dim", expand=True)
        right_index = row + 3
        right = panels[right_index] if right_index < len(panels) else Panel(Text(""), box=box.SQUARE, border_style="dim", expand=True)
        rows.add_row(left, right)

    console.print(Panel(
        rows,
        title=title,
        title_align="left",
        box=box.SQUARE,
        border_style="green",
        padding=(0, 1)
    ))
    console.print(Text(
        "  [↑↓] Navegar  [ENTER] Selecionar  [←→] Trocar página  [ESC] Sair",
        style="dim"
    ))


def render_class_detail(cls, badges):
    console.clear()

    is_locked = cls.get("badge_required") and not badges.get(cls["badge_required"], False)

    stats_table = Table.grid(padding=(0, 2))
    stats_table.add_column(style="dim", min_width=12)
    stats_table.add_column()

    for stat, val in cls["stats"].items():
        stats_table.add_row(stat, Text(val, style=STATS_COLOR.get(val, "white")))

    desc = Text()
    desc.append(f"\n{cls['description']}\n", style="dim white")

    info = Table.grid(padding=(1, 2), expand=True)
    info.add_column(ratio=3)
    info.add_column(ratio=2)
    info.add_row(desc, Panel(stats_table, title="STATS", title_align="left", box=box.SQUARE, border_style="dim"))

    title = Text()
    title.append(f" {cls['name']} ", style="bold white")
    if is_locked:
        title.append("[LOCKED]", style="bold bright_black")
    else:
        title.append(f"[{cls['id']}]", style="bold green")

    console.print(Panel(
        info,
        title=title,
        title_align="left",
        box=box.SQUARE,
        border_style="bright_black" if is_locked else "green",
        padding=(0, 1)
    ))

    if is_locked:
        console.print(Panel(
            Text(f"  🔒  {cls.get('locked_msg', 'Locked.')}", style="bright_black"),
            box=box.SQUARE,
            border_style="bright_black",
            padding=(0, 2)
        ))
    else:
        options = Table.grid(padding=(0, 1), expand=True)
        options.add_column(ratio=1)
        options.add_column(ratio=1)
        options.add_row(
            Panel(Text("  ✓  SELECT", style="bold green"), box=box.SQUARE, border_style="green", expand=True),
            Panel(Text("  ←  BACK", style="dim white"), box=box.SQUARE, border_style="dim", expand=True),
        )
        console.print(options)

    console.print(Text("  [ENTER] Confirmar  [ESC / ←] Voltar", style="dim"))


def classes_menu(badges=None):
    """
    Retorna o input string da classe escolhida (ex: "HACKER", "CV01")
    ou None se o player sair.
    Para adicionar uma nova classe: basta inserir um novo dict em CLASSES.
    """
    if badges is None:
        badges = {}

    visible = list(CLASSES)

    total_pages = max(1, (len(visible) + PER_PAGE - 1) // PER_PAGE)
    page = 1
    cursor = 0

    while True:
        start = (page - 1) * PER_PAGE
        page_items = visible[start: start + PER_PAGE]

        render_class_list(page_items, cursor, badges, page, total_pages)

        key = get_key()

        if key == 'UP':
            cursor = (cursor - 1) % len(page_items)
        elif key == 'DOWN':
            cursor = (cursor + 1) % len(page_items)
        elif key == 'RIGHT':
            page = (page % total_pages) + 1
            cursor = 0
        elif key == 'LEFT':
            page = ((page - 2) % total_pages) + 1
            cursor = 0
        elif key == 'ESC':
            return None
        elif key == 'ENTER':
            selected = page_items[cursor]
            is_locked = selected.get("badge_required") and not badges.get(selected["badge_required"], False)

            while True:
                render_class_detail(selected, badges)
                dk = get_key()

                if is_locked or dk in ('LEFT', 'ESC'):
                    break
                elif dk == 'ENTER':
                    return selected["input"][0]
                elif dk == 'RIGHT':
                    break


class Classes:
    def _Classes(self):
        pass

    def _Classes2(self):
        pass

    def _Classes3(self):
        pass


class Classes:
    def _Classes(self):
        pass

    def _Classes2(self):
        pass

    def _Classes3(self):
        pass
