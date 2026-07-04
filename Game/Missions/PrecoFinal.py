from Game.Missions.FinalMission import (
    navigate_menu, render_result, blocked_message, console
)
from rich.text import Text
from rich.panel import Panel
from rich import box
from time import sleep

ROUTE = "GOOD"


def run(route_history=None):

    console.clear()
    console.print(Panel(
        Text("\nO alvo opera pelo cassino.\nVocê tem uma janela de 20 minutos.\n", style="dim green"),
        box=box.SQUARE, border_style="green", padding=(0, 2)
    ))
    sleep(3)

    detour_used = {"home": False, "bank": False}

    while True:
        choice = navigate_menu(
            title="PREÇO FINAL",
            description="O sistema deles tem uma brecha às 23h.\nVocê está na calçada do cassino.",
            options=[
                {"id": "casino", "label": "Entrar no cassino", "sublabel": "É agora."},
                {"id": "home", "label": "Voltar para casa", "sublabel": "Não consigo fazer isso."},
                {"id": "bank", "label": "Ir para o banco", "sublabel": "Tem outro jeito?"},
            ],
            route=ROUTE
        )

        if choice == "casino":
            _ending_casino()
            return True

        elif choice == "home" and not detour_used["home"]:
            detour_used["home"] = True
            render_result(
                "Você dá meia-volta.\nVocê para na esquina.\nPensa nas pessoas.\nE volta.",
                style="white", pause=3.5
            )

        elif choice == "home":
            render_result("Você está com a mente pesada.", style="white", pause=1.5)

        elif choice == "bank" and not detour_used["bank"]:
            detour_used["bank"] = True
            render_result(
                "O banco está fechado.\nE mesmo que não estivesse, \neles não são o problema.\nO cassino é.",
                style="white", pause=3
            )

        elif choice == "bank":
            render_result("Foco.", style="white", pause=1.5)


def _ending_casino():
    scenes = [
        ("Você entra. Luzes, barulho, fumaça.", "white", 2),
        ("Segundo andar. Sala VIP. Porta dos fundos.", "white", 2),
        ("O gerente não sabe que o sistema dele\nestá sendo drenado em tempo real.", "white", 3),
        ("R$ 1.8 milhões em contas de pessoas que foram roubadas por eles.\nDe volta.", "white", 3.5),
        ("Você sai pela cozinha.\nUm garçom te olha.\nVocê acena.", "white", 3),
        ("Ele acena de volta.", "white", 4),
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
        Text("\n\n  [ PREÇO FINAL ]\n\n", style="bold white"),
        box=box.SQUARE, border_style="white", padding=(1, 4)
    ))
    sleep(4)
