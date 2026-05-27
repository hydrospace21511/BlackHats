import os
import math
import random
from Classes.SecurityAnalyticClass import SecurityAnalyticClass
from Classes.HackerClass import HackerClass
from Classes.SocialEngineerClass import SocialEngineerClass
from Classes.ReverseEngineerClass import ReverseEngineerClass
from Classes.Classes import Classes 
from Classes.HardwareSpecialistClass import HardwareSpecialistClass
from Classes.SecretClasses.Hatsune import HatsuneMikuClass
from Classes.SecretClasses.CorruptedHatsune import CorruptedHatsuneMikuClass
import Player
from Player import integrity_bar
from Player import defense_bar
from Enemy import Enemy
import sys
from Classes.SecretClasses.Rimuru import RimuruClass
#import Test
import getpass
from COBALT import COBALT
from time import sleep
from colorama import Fore, Back, Style, init
from Color import cText
from UI import display_battle_ui


##### lista de erros q "criei": 04: Not found, 201: Not loaded, 302: Class so strong, 666: Secret Class
def user():
    return getpass.getuser()                                                                                                                                                                                                                                                    # ignora isso, é a maldade q quebra a quarta parede po

COBALT = COBALT()
Classes = Classes()
Hacker = HackerClass()
Rimuru = RimuruClass()
SecurityAnalytic = SecurityAnalyticClass()
HardwareSpecialist = HardwareSpecialistClass()
SocialEngineer = SocialEngineerClass()
Vocaloid = HatsuneMikuClass()
ReverseEngineer = ReverseEngineerClass()
CorruptedHatsuneMiku = CorruptedHatsuneMikuClass()
Player = Player.Player()
init(autoreset=True)
from Attacks.SpecialAttacks import DecompilerAttack, AlgorithmCloneAttack, ProtectionBypassAttack, InternalAccessAttack, BaitingAttack, FirewallAttack, SecurityPatchAttack, DesintegrationAttack, MikuMikuBeamAttack, NegativeSpaceAttack, GiveDamageAttack, PneumoultramicroscopicsilicovolcanoconioticAttack, WorldIsMineAttack, TellYourWorldAttack
attack_functions = {
    "Decompiler": DecompilerAttack,
    "Algorithm Clone": AlgorithmCloneAttack,
    "Protection Bypass": ProtectionBypassAttack,
    "Internal Access": InternalAccessAttack,
    "Miku Miku Beam": MikuMikuBeamAttack,
    "MMB": MikuMikuBeamAttack,
    "Tell Your World": TellYourWorldAttack,
    "World Is Mine": WorldIsMineAttack,
    "Baiting": BaitingAttack,
    "Firewall": FirewallAttack,
    "Security Patch": SecurityPatchAttack,
    "Pneumoultramicroscopicsilicovolcanoconiotic": PneumoultramicroscopicsilicovolcanoconioticAttack,
    "Desintegration": DesintegrationAttack,
    "Give Damage": GiveDamageAttack,
    "Negative Space": NegativeSpaceAttack
}

#pra but q n souber, cText é Colored Text (abreviei pq é games e seco filho, liso liso liso)
#isso tava aqui antes de eu colocar o cText em um arquivo diferente, fui moggado? games

print(Classes.ClassesAttacks())
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear() 

COBALT._Start() 
clear()
Classes._Classes() 
ClassesOptions = {
    "SecurityAnalytic": SecurityAnalytic,
    "Hacker": Hacker,
    "Social Engineer": SocialEngineer,
    "Reverse Engineer": ReverseEngineer
} 

while True:
    while True:
        if Player.Class == CorruptedHatsuneMiku:
            cText("▶  Choose your class >>","red")
        else:
         cText("▶  Choose your class >>","green")
        PlayerClass =  str(input("").strip().upper())
        match PlayerClass:

            case "Exit":
                print("""
        Initializing exit sequence...""")     
                sleep(3)
                print("""     
            Exiting the game.
                """)
                clear()
                sys.exit()

            case "SECURITY ANALYTIC" | "2":
                PlayerClass = SecurityAnalytic
                break
            
            case "REVERSE ENGINEER" | "4": # ta aqui só pro diogo ficar com toque de q o 4 ta entre 2 e 1 ao inves de seguir a ordem numerica
                PlayerClass = ReverseEngineer
                break
                
            case "HACKER" | "1":
                PlayerClass = Hacker
                break

            case "SOCIAL ENGINEER" | "3":
                PlayerClass = SocialEngineer
                break

            case "HARDWARE SPECIALIST" | "5":
                PlayerClass = HardwareSpecialist
                break

            case "HATSUNE MIKU" | "CV01":
                PlayerClass = Vocaloid
                break

            case "RIMURU" | "SLIME":
                PlayerClass = Rimuru
                break
                
            case "SECRET" | "666":
                clear()
                cText("⚠  ERROR 666: Secret Activated", "red")
                sleep(2)
                cText("Yes, there are secret classes", "red")
                sleep(1.5)
                
                while True:
                    clear()
                    cText("Wanna a hint?", "green")
                    sleep(2)
                    cText("Y/N", "blue")
                    hint = str(input("").strip().upper())
                    match hint:

                        case "YES" | "Y":
                            clear()
                            cText("https://pastebin.com/2snJpKM9", "cyan")
                            sleep(5)
                            clear()
                            Classes._Classes() 
                            break

                        case "NO" | "N":
                            clear()
                            Classes._Classes() 
                            break

                        case _:
                            clear()
                            cText("⚠  ERROR 04: Response not found", "red")

                            continue
                

            case _:
                clear()
                Classes._Classes() 
                cText("⚠  ERROR 04: Class not found", "red") #sim, o 04 significa not found, OUVIU THALLES? (alem do 404 btw)
                continue

    cText("▶  Enter your name >>","green")            
    Player.Name = input("")
    match Player.Name :

        case "Return" :
            print("returning to class selection...")
            clear()
            continue
        
        case _ :
            break

Player.Class = PlayerClass    
Player.Integrity = Player.Class.Integrity
Player.Defense = Player.Class.Defense
Player.Regen = Player.Class.Regen
clear()
cText(f">> Welcome {Player.Name}!","green")
sleep(2)
cText(f">> Your class is: {Player.Class.raceName}","green")
sleep(2)
clear()
#print(Player.Name) 
#print(f"Available attacks: {Player.Class.MostraAtaques()}")
print(f"Integrity: {integrity_bar(Player.Class.Integrity, PlayerClass.Integrity)}")

enemy_attacks = {
    "Shadow Strike": 20,
    "Inferno Blast": 60,
    "Phantom Slash": 70,
    "Chaos Roar": 100
}

current_enemy = Enemy(name="filth", max_health=500, defense=15, regen=0, attacks=enemy_attacks)
active_cooldowns = {}
#Protection
def Damage(D, Defense) :
    return D * (1 - Defense / 100)

#print("Available attacks:", list(Player.Class.Attacks.keys()))
clear()
display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)

while True :
    if type(Player.Class) == CorruptedHatsuneMikuClass:
        cText("▶  Choose an exploit >>","red")
    else:
        cText("▶  Choose an exploit >>","green")
    Attack = input("")    
    
    if Attack == "Reverse" and Player.Class.Decompiled == True:
        clear()
        display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
        cText(" Reversing the decompilation...", "warn")
        sleep(2)
        cText(" Decompilation reversed! Your original stats and attacks were restored!", "positive")
        sleep(2)
        Player.Class.Decompiled = False
        Player.Class.Attacks = Player.Class.OriginalAttacks
        Player.Class.Defense = Player.Class.DefenseBackup
        Player.Class.Integrity = Player.Class.IntegrityBackup
        clear()

    if Attack not in Player.Class.Attacks:
        clear()
        display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
        cText("⚠  ERROR 04: Exploit not found", "red")
        continue

    if Attack in active_cooldowns and active_cooldowns[Attack] > 0:
            clear()
            display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
            cText(f"⚠  ACCESS DENIED: '{Attack}' is cooling down! ({active_cooldowns[Attack]} turns left)", "yellow")
            continue

    Attack_Info = Player.Class.Attacks[Attack]
    context = Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, Player.Class

    if Attack in attack_functions:
        attack_functions[Attack](*context)
    else:
        clear()
        display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
        final_damage = Damage(Attack_Info, current_enemy.Defense)
        current_enemy.Health -= final_damage
        cText(f" >> You executed [{Attack}]! {current_enemy.Name} took {final_damage:.1f} damage!", "positive")


    if hasattr(Player.Class, 'Cooldowns') and Attack in Player.Class.Cooldowns:
        active_cooldowns[Attack] = Player.Class.Cooldowns[Attack]

    if current_enemy.Health <= 0:
        sleep(1.5)                                          #-
        clear()
        cText(f"\n   [>> NODE COMPROMISED <<]\n < -- {current_enemy.Name} Defeated! -- >\n", "green")
        break

    sleep(1.5)

    enemy_attack_name, enemy_attack_dmg = current_enemy.random_attack()
    enemy_final_damage = Damage(enemy_attack_dmg, Player.Defense)
    Player.Integrity -= enemy_final_damage
    
    #-
    cText(f" >> {current_enemy.Name} retaliates with [{enemy_attack_name}]! You took {enemy_final_damage:.1f} damage!", "error")
    sleep(2.5)

    if Player.Integrity <= 0:
        clear()
        cText(f"\n        [!]Error 404[!] \n < -- You have been hacked. -- >\n", "red")
        sleep(2)
        break

    for skill in active_cooldowns:
        if active_cooldowns[skill] > 0:
            active_cooldowns[skill] -= 1

    if Player.Regen > 0:
        Player.Integrity += Player.Regen
       # Player.Class.Integrity += Player.Class.Regen
        print(f"Available attacks: {Player.Class.MostraAtaques()}")
        print(f"Integrity: {integrity_bar(Player.Integrity, Player.Class.Integrity)}")
        if Player.Integrity >= Player.Class.Integrity: 
            Player.Integrity = Player.Class.Integrity
        Player.Regen = 0

    if Player.Defense >= 100:
        Player.Defense = 99
        
    clear() 
    display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
    