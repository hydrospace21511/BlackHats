from Game.Missions.FinalMission import (
    navigate_menu, render_result, blocked_message, console
)
from rich.text import Text
from rich.panel import Panel
from rich import box
from time import sleep

ROUTE = "BAD"


def run(route_history=None):

    console.clear()
    console.print(Panel(
        Text("\nO dinheiro vai cair hoje.\nVocê passou semanas planejando isso.\n", style="dim red"),
        box=box.SQUARE, border_style="red", padding=(0, 2)
    ))
    sleep(3)

    detour_used = {"home": False, "casino": False}

    while True:
        choice = navigate_menu(
            title="CLÁUSULA FINAL",
            description="O plano está pronto. Falta só executar.\nPara onde vai?",
            options=[
                {"id": "bank", "label": "Ir para o banco", "sublabel": "É agora ou nunca."},
                {"id": "home", "label": "Voltar para casa", "sublabel": "Talvez eu repense."},
                {"id": "casino", "label": "Ir para o cassino", "sublabel": "Chance de perder tudo."},
            ],
            route=ROUTE
        )

        if choice == "bank":
            _ending_bank()
            return True

        elif choice == "home" and not detour_used["home"]:
            detour_used["home"] = True
            render_result(
                "Você chega na porta de casa.\nAntes da porta abrir, \nvocê para.\nAinda não.",
                style="white", pause=3
            )

        elif choice == "home":
            render_result("Você ja tentou isso.", style="white", pause=1.5)

        elif choice == "casino" and not detour_used["casino"]:
            detour_used["casino"] = True
            render_result(
                "Você entra no cassino.\nVai apostar.\nE perde tudo pro tigrinho.\nVocê se levanta e sai.",
                style="white", pause=3
            )

        elif choice == "casino":
            render_result("Não tenho mais dinheiro pra isso.", style="white", pause=1.5)


def _ending_bank():
    scenes = [
        ("Você entra pelo estacionamento dos fundos.", "white", 2),
        ("A câmera no corredor B, você sabia que estava quebrada.", "white", 2),
        ("Acesso ao sistema interno: 47 segundos.", "white", 2.5),
        ("A transferência completa. R$ 2.4 milhões.", "white", 3),
        ("Você sai pelo mesmo corredor.\nNinguém te viu.", "white", 3),
        ("Mas alguém sempre vê.", "white", 4),
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
        Text("\n\n  [ CLÁUSULA FINAL ]\n\n", style="bold white"),
        box=box.SQUARE, border_style="white", padding=(1, 4)
    ))
    sleep(4)
