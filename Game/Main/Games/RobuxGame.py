from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
from rich import box
from colorama import Fore
import time
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


console = Console()

def robux_menu(selected_index=0):
    options = ["400", "800", "1,200", "1,700", "4,500", "10,000"]

    title = Text()
    title.append("ROBUX", style="bold green")
    title.append("GEN", style="bold yellow")
    title.append("  v2.4.1", style="dim")

    header = Text()
    header.append("\nQuantos ", style="dim white")
    header.append("Robux", style="bold green")
    header.append(" você quer gerar?\n", style="dim white")
    header.append("Selecione uma opção abaixo e aperte ", style="dim")
    header.append("ENTER", style="bold green")
    header.append(" para confirmar.\n", style="dim")

    header_panel = Panel(
        header,
        title=title,
        title_align="left",
        box=box.ROUNDED,
        border_style="green",
        padding=(0, 2),
        expand=True
    )

    grid = Table.grid(padding=(0, 1), expand=True)
    grid.add_column(ratio=1)
    grid.add_column(ratio=1)
    grid.add_column(ratio=1)

    def make_btn(label, idx):
        is_sel  = idx == selected_index
        t_style = "bold green" if is_sel else "dim white"
        b_style = "green"      if is_sel else "dim"
        t = Text(f"R$ {label}", style=t_style, justify="center")
        return Panel(t, box=box.ROUNDED, border_style=b_style, expand=True)

    grid.add_row(
        make_btn(options[0], 0),
        make_btn(options[1], 1),
        make_btn(options[2], 2),
    )
    grid.add_row(
        make_btn(options[3], 3),
        make_btn(options[4], 4),
        make_btn(options[5], 5),
    )

    options_panel = Panel(
        grid,
        title=Text("SELECIONE A QUANTIDADE", style="dim"),
        title_align="left",
        box=box.ROUNDED,
        border_style="green",
        padding=(1, 2),
        expand=True
    )

    console.print(header_panel)
    console.print()
    console.print(options_panel)
    console.print(Text(
        "\n  ROBUXGEN v2.4.1  |  GERADOR DE ROBUX GRÁTIS  |  100% SEGURO  |  FONTE: CONFIA",
        style="dim"
    ), justify="left")


def robux_game():
    from Game.Main.UI import get_key

    options  = ["400", "800", "1,200", "1,700", "4,500", "10,000"]
    selected = 0
    total    = len(options)

    while True:
        clear()
        robux_menu(selected_index=selected)

        key = get_key()

        if key == 'RIGHT':
            selected = (selected + 1) % total
        elif key == 'LEFT':
            selected = (selected - 1) % total
        elif key == 'DOWN':
            selected = (selected + 3) % total
        elif key == 'UP':
            selected = (selected - 3) % total
        elif key in ('ENTER', 'SPACE'):
            choice = options[selected]
            break

    clear()
    console.print(Panel(
        Text(f"Gerando {choice} Robux para sua conta...", style="bold green"),
        box=box.ROUNDED,
        border_style="green",
        padding=(1, 2)
    ))
    time.sleep(1)

    from rich.progress import Progress, BarColumn, TextColumn
    with Progress(
        TextColumn("[bold green]  Progresso"),
        BarColumn(bar_width=40, complete_style="green"),
        TextColumn("[green]{task.percentage:>3.0f}%"),
    ) as progress:
        task = progress.add_task("", total=100)
        for i in range(99):
            progress.advance(task, 1)
            time.sleep(0.03)
        time.sleep(5)

    clear()
    print(f"{Fore.GREEN}Sucesso! R$ {choice} foram gerados para sua conta!")
    time.sleep(2)
    print(f"{Fore.RED}Ou não... (Talvez isso seja um golpe)")
    time.sleep(2)

    input(f"\n  \033[90m[ Pressione ENTER para retornar ]\033[0m")