import os
from time import sleep
from colorama import init
init(autoreset=True)
from Color import cText
from UI import display_battle_ui
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def GiveDamageAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
            clear()
            Player.Integrity -= Attack_Info
            cText("Why would you do that? R u dumb?", "red") # só pra testa a classe e os bagui
            sleep(2)
            clear()