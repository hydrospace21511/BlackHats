import os
from time import sleep
from colorama import init
init(autoreset=True)
from Color import cText
from UI import display_battle_ui
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def PneumoultramicroscopicsilicovolcanoconioticAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
            print("U just got ball cancer, gng how u managed to do that is beyond me ngl")
            sleep(3)
            final_damage = Damage(100000000, Player.Class.Defense)
            Player.Integrity -= final_damage
            clear()
            print(f"Integrity: {integrity_bar(Player.Integrity, Player.Class.Integrity)}")
            sleep(3)
            clear()