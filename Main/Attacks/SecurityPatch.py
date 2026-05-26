import os
from time import sleep
from colorama import init
init(autoreset=True)
from Color import cText
from UI import display_battle_ui
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def SecurityPatchAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
            Player.Class.Regen += Attack_Info 
            clear()
            print(f"Available attacks: {Player.Class.MostraAtaques()}")
            print(f"Regen increased to {Player.Class.Regen}.")