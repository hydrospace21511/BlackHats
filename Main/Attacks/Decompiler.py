import os
from time import sleep
from colorama import init
init(autoreset=True)
from Color import cText
from UI import display_battle_ui
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def DecompilerAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack):
    clear()
    final_damage = Damage(Attack_Info, current_enemy.Defense)
    display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
    if Player.Class.Decompiled == False:
        cText(cText(f" >> You executed {Attack}! {current_enemy.Name} took {final_damage:.1f} damage!", "positive"))
        cText("Enemy decompiled!", "positive")
        sleep(2)
        current_enemy.Health -= final_damage
        Player.Class.Decompiled = True
    else:
        current_enemy.Health -= final_damage
        cText(f" >> You executed {Attack}! {current_enemy.Name} took {final_damage:.1f} damage!", "positive")
        sleep(3)
        clear()