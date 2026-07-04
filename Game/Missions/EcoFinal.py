from Game.Missions.FinalMission import (
    navigate_menu, render_result, blocked_message, console
)
from rich.text import Text
from rich.panel import Panel
from rich import box
from time import sleep
import random

ROUTE = "TRUE"


def run(route_history=None):

    console.clear()
    console.print(Panel(
        Text("\nO terminal pisca. Você olha para a tela por um longo tempo.\nNão tem mais nada aqui.\n", style="dim cyan"),
        box=box.SQUARE, border_style="cyan", padding=(0, 2)
    ))
    sleep(3)

    while True:
        choice = navigate_menu(
            title="ECO FINAL",
            description="A noite está fria. Você suspira.\nPara onde vai agora?",
            options=[
                {"id": "home", "label": "Voltar para casa", "sublabel": "Acho que é hora."},
                {"id": "bank", "label": "Ir para o banco", "sublabel": "Talvez ainda de tempo."},
                {"id": "casino", "label": "Ir para o cassino", "sublabel": "Uma última aposta."},
            ],
            route=ROUTE
        )

        if choice == "home":
            _ending_home()
            return True

        elif choice == "bank":
            blocked_message(kind=random.choice(["closed", "lazy"]))

        elif choice == "casino":
            blocked_message(kind=random.choice(["closed", "lazy"]))


def _ending_home():
    scenes = [
        ("Você fecha o computador pela última vez.", "white", 2.5),
        ("O silêncio do apartamento nunca pareceu tão alto.", "white", 2.5),
        ("Você entra no quarto dela. Ela está quieta e pensativa.", "white", 3),
        ("Você senta na beira. Pensa em falar com ela, mas desiste.", "white", 4),
        ("No bolso, o pendrive com os arquivos. Você o coloca na gaveta.", "white", 5),
        ("Não era sobre o dinheiro.\nNunca foi.", "white", 4),
    ]

    for text, style, pause in scenes:
        console.clear()
        console.print(Panel(
            Text(f"\n{text}\n", style=style),
            box=box.SQUARE, border_style="white", padding=(0, 2)
        ))
        sleep(pause)

    console.clear()
    console.print(Panel(
        Text("\n\n  [ ECO FINAL ]\n\n", style="bold white"),
        box=box.SQUARE, border_style="white", padding=(1, 4)
    ))
    sleep(4)
