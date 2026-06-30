import os
import sys
import getpass
from time import sleep
from rich.console import Console, Group
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.live import Live
from rich.spinner import Spinner
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeRemainingColumn
from colorama import Fore, Back, Style, init
from Game.Main.Color import cText
init(autoreset=True)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
cText(f"A versão do seu sistema (4) está atualmente desatualizada.", "error")
sleep(1.5)
cText(f"Gostaria de atualizar a versão do seu sistema para 5?", "green")
sleep(1)
input(f"\n  {Fore.LIGHTBLACK_EX}[ Pressione ENTER para continuar ]{Style.RESET_ALL}")
clear()

with Progress(
    TextColumn("[bold green]COBALT OS"),
    BarColumn(bar_width=40, complete_style="green", finished_style="bright_green"),
    TextColumn("[green]{task.percentage:>3.0f}%"),
    TimeRemainingColumn(),
) as progress:
    task = progress.add_task("Atualizando...", total=100)
    while not progress.finished:
        progress.advance(task, 1)
        sleep(0.04)

sleep(1)
clear()
sleep(0.5)
cText(" Sistema atualizado com sucesso. Versão 5.0 instalada.", "positive")
sleep(1.5)
input(f"\n  {Fore.LIGHTBLACK_EX}[ Pressione ENTER para ver as novidades ]{Style.RESET_ALL}")


