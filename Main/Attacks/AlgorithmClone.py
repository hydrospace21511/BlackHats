import os
from time import sleep
from colorama import init
init(autoreset=True)
from Color import cText
from UI import display_battle_ui
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def AlgorithmCloneAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
    final_damage = Damage(Attack_Info, current_enemy.Defense)
    if PlayerClass.Decompiled == True:
        display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
        cText(cText(f" >> You executed {Attack}! {current_enemy.Name} took {final_damage:.1f} damage!", "positive"))
        sleep(2)
        cText(" Algorithm cloned! You copied the enemy!", "positive")
        #Player.Class.Attacks["Reverse":10] = 0
        Player.Class.Attacks = current_enemy.Attacks
        Player.Class.Defense = current_enemy.Defense
        Player.Class.Integrity = current_enemy.Health - (Player.Integrity - Player.Class.Integrity)
        sleep(3)
        clear()
        current_enemy.Health -= final_damage
        clear()

    elif PlayerClass.Decompiled == False:
                current_enemy.Health -= final_damage
                display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
                cText(cText(f" >> You executed {Attack}! {current_enemy.Name} took {final_damage:.1f} damage!", "positive"))
                sleep(3)
                clear()