import os
from time import sleep
from colorama import init
init(autoreset=True)
from Color import cText
from UI import display_battle_ui
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def DesintegrationAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
            clear()
            cText("I summon the DeepWeb slimes", "red")
            sleep(2)
            for i in range(100):
                final_damage = Damage(80, Player.Class.Defense)
                Player.Integrity -= final_damage
                clear()
                display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
    
                sleep(0.03)