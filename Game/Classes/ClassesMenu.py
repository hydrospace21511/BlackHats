from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
from rich import box
import os

console = Console()

CLASSES = [
    {
        "id": "1",
        "name": "HACKER",
        "input": ["HACKER", "1"],
        "focus": "Dano bruto & exploiting de sistemas.",
        "description": (
            "O Hacker é uma classe puramente ofensiva, especializada em quebrar"
            "as defesas inimigas com força bruta e ataques diretos ao sistema."
            "Alto dano, baixa defesa. Ideal para jogadores agressivos."
        ),
        "stats": {"Integridade": "Alta", "Defesa": "Baixa", "Regeneração": "Nenhuma"},
        "badge_required": None,
    },
    {
        "id": "2",
        "name": "SECURITY ANALYTIC",
        "input": ["SECURITY ANALYTIC", "2"],
        "focus": "Defesa inquebrável & integridade de nodes",
        "description": (
            "O Security Analytic se destaca na proteção de sistemas e na sustentação de "
            "longas batalhas. Bônus de defesa passiva e restauração de integridade "
            "tornam esta classe ideal para jogadores cautelosos."
        ),
        "stats": {"Integridade": "Média", "Defesa": "Alta", "Regeneração": "Pouca"},
        "badge_required": "Security Analytic",
        "locked_msg": "Complete a conquista 'Security Analytic' para desbloquear.",
    },
    {
        "id": "3",
        "name": "SOCIAL ENGINEER",
        "input": ["SOCIAL ENGINEER", "3"],
        "focus": "Manipulação, regeneração & bypass.",
        "description": (
            "O Social Engineer vence batalhas através de guerra psicológica "
            "e manipulação de recursos. Gestão de cooldown e pulando turnos "
            "dão a esta classe uma vantagem única em conflitos prolongados."
        ),
        "stats": {"Integridade": "Média", "Defesa": "Média", "Regeneração": "Alta"},
        "badge_required": "Social Engineer",
        "locked_msg": "Complete a conquista 'Social Engineer' para desbloquear.",
    },
    {
        "id": "4",
        "name": "REVERSE ENGINEER",
        "input": ["REVERSE ENGINEER", "4"],
        "focus": "Descompilação e ataques adaptativos.",
        "description": (
            "O Reverse Engineer pode desmantelar sistemas inimigos e tornar as "
            "próprias armas deles contra eles. Uma classe complexa, mas recompensadora para aqueles que"
            "entendem profundamente as mecânicas dela."
        ),
        "stats": {"Integridade": "Média", "Defesa": "Baixa", "Regeneração": "Nenhuma"},
        "badge_required": "Reverse Engineer",
        "locked_msg": "Complete a conquista 'Reverse Engineer' para desbloquear.",
    },
    {
        "id": "5",
        "name": "HARDWARE SPECIALIST",
        "input": ["HARDWARE SPECIALIST", "5"],
        "focus": "Manipulação de hardware & otimização.",
        "description": (
            "O Hardware Specialist opera na camada física dos sistemas, "
            "causando dano consistente enquanto otimiza suas próprias estatísticas ao longo do tempo. "
            "Mecânicas únicas de buff fazem desta classe crescer mais forte durante a batalha."
        ),
        "stats": {"Integridade": "Alta", "Defesa": "Média", "Regeneração": "Nenhuma"},
        "badge_required": "Hardware Specialist",
        "locked_msg": "Complete a conquista 'Hardware Specialist' para desbloquear.",
    },
    {
        "id": "6",
        "name": "SECURITY BYPASSER",
        "input": ["SECURITY BYPASSER", "6"],
        "focus": "Ignora medidas de segurança & stealth.",
        "description": (
            "O Security Bypasser se especializa em ignorar completamente as defesas inimigas. "
            "Ataques baseados em furtividade causam dano real, tornando esta classe "
            "o inferno dos inimigos com alta defesa."
        ),
        "stats": {"Integridade": "Baixa", "Defesa": "Baixa", "Regeneração": "Média"},
        "badge_required": "Security Bypass",
        "locked_msg": "Complete a conquista 'Security Bypass' para desbloquear.",
    },
    {
        "id": "CV01",
        "name": "HATSUNE MIKU",
        "input": ["HATSUNE MIKU", "CV01"],
        "focus": "Ataques sonoros & combos baseados em ritmo.",
        "description": (
            "Uma classe secreta desbloqueada através de uma badge oculta. "
            "Miku ataca usando frequências sonoras e padrões musicais, "
            "causando dano massivo com mecânicas de combo únicas."
        ),
        "stats": {"Integridade": "Alta", "Defesa": "Alta", "Regeneração": "Alta"},
        "badge_required": "DarkHats",
        "locked_msg": "Complete a conquista 'DarkHats' para desbloquear.",
    },
    {
        "id": "LAMBDA",
        "name": "LAMBDA",
        "input": ["LAMBDA"],
        "focus": "Desconhecido.",
        "description": (
            "Uma classe envolvida no desconhecido. Seus ataques desafiam a "
            "classificação convencional. Apenas aqueles que viram de tudo a entenderão."
        ),
        "stats": {"Integridade": "???", "Defesa": "???", "Regeneração": "???"},
        "badge_required": "???",
        "locked_msg": "Complete a conquista '???' para desbloquear.",
    },
]

STATS_COLOR = {
    "Alto":   "bold green",
    "Alta":   "bold green",
    "Médio": "bold yellow",
    "Média": "bold yellow",
    "Baixo":    "bold red",
    "Baixa":    "bold red",
    "Nenhum":   "dim",
    "Nenhuma":   "dim",
    "???":    "dim magenta",
}
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
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

def render_class_list(classes_page, cursor, badges, page, total_pages):
    clear()

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
    clear()

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
    info.add_row(desc, Panel(stats_table, title="STATUS", title_align="left", box=box.SQUARE, border_style="dim"))

    title = Text()
    title.append(f" {cls['name']} ", style="bold white")
    if is_locked:
        title.append("[BLOQUEADO]", style="bold bright_black")
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
