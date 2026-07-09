import os
import sys
import pygame

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
attack_archive = os.path.dirname(os.path.abspath(__file__))
from time import sleep
from Game.Classes.SecretClasses.Hatsune import HatsuneMikuClass
from Game.Classes.SecretClasses.CorruptedHatsune import CorruptedHatsuneMikuClass
CorruptedHatsuneMiku = CorruptedHatsuneMikuClass()
pygame.mixer.init()
import getpass
from colorama import Fore, Back, Style

def user():
    return getpass.getuser()

from colorama import init
import random
init(autoreset=True)
from Game.Main.Color import cText
from Game.Main.UI import display_battle_ui

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def trigger_negative_space(self):
    try:
        colunas, linhas = os.get_terminal_size()
    except OSError:
        os.system('cls' if os.name == 'nt' else 'clear')
    sys.stdout.write(Back.WHITE + (" " * colunas + "\n") * (linhas - 1) + " " * colunas)
    sys.stdout.flush()
    sleep(0.08)
    os.system('cls' if os.name == 'nt' else 'clear')
    msg = " >> You Can't Escape From Me << "
    meio = linhas // 2
    for _ in range(meio):
        sys.stdout.write(Back.WHITE + " " * colunas + "\n")
    sys.stdout.write(Back.WHITE + Fore.BLACK + Style.BRIGHT + msg.center(colunas) + "\n")
    for _ in range(linhas - meio - 2):
        sys.stdout.write(Back.WHITE + " " * colunas + "\n")
    sys.stdout.write(Back.WHITE + " " * colunas)
    sys.stdout.flush()
    sleep(1.8)
    print(Style.RESET_ALL, end="")
    os.system('cls' if os.name == 'nt' else 'clear')

def AlgorithmCloneAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
    final_damage = Damage(Attack_Info, current_enemy.Defense)
    if PlayerClass.Decompiled:
        display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
        cText(cText(f" >> You executed {Attack}! {current_enemy.Name} took {final_damage:.1f} damage!", "positive"))
        sleep(2)
        cText(" Algorithm cloned! You copied the enemy!", "positive")
        Player.Class.Attacks = current_enemy.Attacks
        Player.Class.Defense = current_enemy.Defense
        Player.Class.Integrity = current_enemy.Health - (Player.Integrity - Player.Class.Integrity)
        sleep(3)
        clear()
        current_enemy.Health -= final_damage
        clear()
    else:
        current_enemy.Health -= final_damage
        display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
        cText(cText(f" >> You executed {Attack}! {current_enemy.Name} took {final_damage:.1f} damage!", "positive"))
        sleep(3)
        clear()

def BaitingAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
    Player.Defense += Attack_Info
    Player.Regen += 40
    if Player.Defense >= 100:
        Player.Defense = 99
    clear()
    print(f"Available attacks: {Player.Class.MostraAtaques()}")
    print(f"Defense: {defense_bar(Player.Defense)}")

def DecompilerAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
    clear()
    final_damage = Damage(Attack_Info, current_enemy.Defense)
    display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
    if not Player.Class.Decompiled:
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

def DesintegrationAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
    clear()
    cText("I summon the DeepWeb slimes", "red")
    sleep(2)
    for _ in range(100):
        final_damage = Damage(80, Player.Class.Defense)
        Player.Integrity -= final_damage
        clear()
        display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
        sleep(0.03)

def FirewallAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
    Player.Defense += Attack_Info
    if Player.Defense >= 100:
        Player.Defense = 99
        Player.Class.Defense = 99
    clear()
    print(f"Available attacks: {Player.Class.MostraAtaques()}")
    print(f"Defense: {defense_bar(Player.Defense)}")

def GiveDamageAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
    clear()
    Player.Integrity -= Attack_Info
    cText("Why would you do that? R u dumb?", "red")
    sleep(2)
    clear()

def InternalAccessAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
    Player.Defense += Attack_Info
    if Player.Defense >= 100:
        Player.Defense = 99
        clear()
        print(f"Available attacks: {Player.Class.MostraAtaques()}")
        print(f"Defense: {defense_bar(Player.Defense)}")

def MikuMikuBeamAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
    i = 0
    #PlayerClass.Defense = 0
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

def NegativeSpaceAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
    clear()
    sleep(1)
    cText("Corrupting the space", "error")
    sleep(2)
    clear()
    cText("Everything will be white...", "error")
    sleep(2)
    clear()
    trigger_negative_space(Player)
    final_damage = Damage(Attack_Info, current_enemy.Defense)
    current_enemy.Health -= final_damage
    display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
    cText(f">> The attack corrupted the space! {current_enemy.Name} took {final_damage:.1f} damage!", "positive")

def PneumoultramicroscopicsilicovolcanoconioticAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
    clear()
    final_damage = Damage(80, Player.Class.Defense)
    Player.Integrity -= final_damage
    clear()
    print(f"Integrity: {integrity_bar(Player.Integrity, Player.Class.Integrity)}")
    sleep(3)
    clear()

def ProtectionBypassAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
    current_enemy.Health -= Attack_Info
    cText(cText(f" >> You executed {Attack}! {current_enemy.Name} took {Attack_Info:.1f} damage!", "positive"))
    clear()

def SecurityPatchAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
    Player.Class.Regen += Attack_Info
    clear()
    print(f"Available attacks: {Player.Class.MostraAtaques()}")
    print(f"Regen increased to {Player.Class.Regen}.")

def TellYourWorldAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
    clear()
    sleep(0.5)
    cText("Could you tell me your world?", "cyan")
    sleep(2)
    clear()
    cText("⚠  No?", "red")
    sleep(4)
    clear()
    cText("Ok", "cyan")
    sleep(2)
    clear()
    Player.Regen += 500
    Player.Defense += 10
    cText(f" Your Regen was increased by {Player.Regen}", "positive")
    sleep(2)
    cText(f" Your Defense was increased to {Player.Defense}", "positive")
    sleep(2)
    clear()

def WorldIsMineAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
    if Player.Integrity <= 207:
        sleep(4)
        clear()
        for label, count in (("World.", 0), ("Is.", 0), ("Mine.", 0)):
            while count <= 3:
                cText(label, "cyan")
                sleep(0.5)
                count += 1
                clear()
                cText(label + ".", "cyan")
                sleep(0.5)
                count += 1
                clear()
                cText(label + "..", "cyan")
                sleep(0.5)
                count += 1
                clear()
                cText(label + "...", "cyan")
                sleep(0.5)
                count += 1
                clear()
                break
        final_damage = Damage(Attack_Info, current_enemy.Defense)
        current_enemy.Health -= final_damage
        cText(f"  >> You executed {Attack}! {current_enemy.Name} took {final_damage:.1f} damage!", "positive")
        sleep(2)
        clear()

def SystemOverrideAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
    current_enemy.SkipTurn = True
    clear()
    final_damage = Damage(Attack_Info, current_enemy.Defense)
    current_enemy.Health -= final_damage
    cText(" System overridden! Enemy systems frozen!", "positive")
    sleep(2)
    clear()