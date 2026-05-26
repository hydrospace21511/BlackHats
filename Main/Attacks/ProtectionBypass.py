import os
from time import sleep
from colorama import init
init(autoreset=True)
from Color import cText
from UI import display_battle_ui
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def ProtectionBypassAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
                #display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
            current_enemy.Health -= Attack_Info
            cText(cText(f" >> You executed {Attack}! {current_enemy.Name} took {Attack_Info:.1f} damage!", "positive"))
            clear()