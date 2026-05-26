import os
from time import sleep
from colorama import init
init(autoreset=True)
from Color import cText
from UI import display_battle_ui
from Classes.SecretClasses.CorruptedHatsune import CorruptedHatsuneMikuClass
CorruptedHatsuneMiku = CorruptedHatsuneMikuClass()
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def NegativeSpaceAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
            clear()
            sleep(1)
            cText("Corrupting the space", "error")
            sleep(2)
            clear()
            cText("Everything will be white...", "error")
            sleep(2)
            clear()
            CorruptedHatsuneMikuClass.trigger_negative_space()
            final_damage = Damage(Attack_Info, current_enemy.Defense)
            current_enemy.Health -= final_damage
            display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
            cText(f">> The attack corrupted the space! {current_enemy.Name} took {final_damage:.1f} damage!", "positive")
