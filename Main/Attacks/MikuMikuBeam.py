import os
from time import sleep
from colorama import init
init(autoreset=True)
from Color import cText
from UI import display_battle_ui
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def MikuMikuBeamAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
            i = 0
            PlayerClass.Defense = 0
            while i < 100:
                clear()
                if i < 50:
                    cText(f"Miku Miku Beam is charging... {i}%", "red")
                elif i < 80:
                    cText(f"Miku Miku Beam is charging... {i}%", "yellow") # tentei usar case mas fiquei com preguiça, ent vai ficar assim mesmo (pq vc ta lendo isso, thalles?)
                elif i <= 100:
                    cText(f"Miku Miku Beam is charging... {i}%", "green")
                sleep(0.03)
                i += 1
            if i >= 100:
                clear()
                cText("Miku Miku Beam is fully charged!", "positive")
                sleep(1)
                clear()
                x = 0
                while x <= 100:
                    clear()
                    final_damage = Damage(Attack_Info, current_enemy.Defense)
                    cText(f"-{final_damage} life! ({x}%)", "red")
                    current_enemy.Health -= final_damage
                    print(f"Integrity: {integrity_bar(current_enemy.Health, current_enemy.MaxHealth)}")
                    sleep(0.03)
                    x += 1