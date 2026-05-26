import os
from time import sleep
from colorama import init
init(autoreset=True)
from Color import cText
from UI import display_battle_ui
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def TellYourWorldAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
            clear()
            sleep(0.5)
            cText("Could you tell me your world?", "cyan")
            sleep(2)
            clear()
            cText("⚠  No?", "red")
            sleep(4)
            clear()
            cText("Ok", "cyan") # Thalles que estiver lendo isso, de acordo com a lei 302 artigo II, você não tem o direito de me julgar de acordo com minha maneira de me expressar via programação de códigos em inglês chamada Python. Caso contrário, favor contatar meu advogado Yudi - 4002-8922
            sleep(2)
            clear()
            Player.Regen += 500
            Player.Defense += 10
            cText(f" Your Regen was increased by {Player.Regen}", "positive")
            sleep(2)
            cText(f" Your Defense was increased to {Player.Defense}", "positive")
            sleep(2)
            clear()