import os
from Classes.SecurityAnalyticClass import SecurityAnalyticClass
from Classes.HackerClass import HackerClass
from Classes.SocialEngineerClass import SocialEngineerClass
from Classes.Classes import Classes 
from Classes.SecretClasses.Hatsune import HatsuneMikuClass
import Player
from Player import integrity_bar
from Player import defense_bar
from Enemy import Enemy
import sys
from COBALT import COBALT
from time import sleep
from colorama import Fore, Back, Style, init
from Color import cText
from AttacksFX import slash_animation
 

COBALT = COBALT()
Classes = Classes()
Enemy = Enemy("a", 100, 1, 0)
Hacker = HackerClass()
SecurityAnalytic = SecurityAnalyticClass()
SocialEngineer = SocialEngineerClass()
HatsuneMiku = HatsuneMikuClass()
Player = Player.Player()
init(autoreset=True)

#pra but q n souber, cText é Colored Text (abreviei pq é games e seco filho, liso liso liso)
#isso tava aqui antes de eu colocar o cText em um arquivo diferente, fui moggado? games

print(Classes.ClassesAttacks())
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()
COBALT.Start()

print(SecurityAnalytic.MostraAtaques())
print(Hacker.MostraAtaques())
print(SocialEngineer.MostraAtaques())
print(HatsuneMiku.MostraAtaques())
clear()
print(Classes.Classes())
ClassesOptions = {
    "SecurityAnalytic": SecurityAnalytic,
    "Hacker": Hacker,
    "Social Engineer": SocialEngineer
}

while True:
    while True:
        PlayerClass = str(input("Choose your class: ").strip().upper())
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

            case "HACKER" | "1":
                PlayerClass = Hacker
                break

            case "SOCIAL ENGINEER" | "3":
                PlayerClass = SocialEngineer
                break

            case "HATSUNE MIKU" | "CV01":
                PlayerClass = HatsuneMiku
                break
                

            case _:
                clear()
                print("Invalid class. Please choose again.")
                continue

    Player.Name = input("Enter your name: ")
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
print(f"Welcome, {Player.Name}!")
sleep(2)
print(f"Your class is: {Player.Class.RaceName()}")
sleep(2)
clear()
#print(Player.Name)
print(f"Available attacks: {Player.Class.MostraAtaques()}")
print(f"Integrity: {integrity_bar(Player.Class.Integrity, PlayerClass.Integrity)}")

# ---- teste ataques ----

def Damage(D, Defense) :
    return D * (1 - Defense / 100)

def display_battle_ui(player_integrity, max_integrity, player_defense, available_attacks):
    """Display the battle UI in a bordered box"""
    integrity_display = integrity_bar(player_integrity, max_integrity)
    defense_display = defense_bar(player_defense)
    attacks_list = ", ".join(available_attacks)
    
    border_top = "╔" + "═" * 75 + "╗"
    border_bottom = "╚" + "═" * 75 + "╝"
    border_side = "║"
    
    print(border_top)
    print(f"{border_side} {'BATTLE STATUS':^73} {border_side}")
    print(f"{border_side} {'-' * 73} {border_side}")
    print(f"{border_side} Life:     {integrity_display:<65} {border_side}")
    print(f"{border_side} Defense:  {defense_display:<65} {border_side}")
    print(f"{border_side} {'-' * 73} {border_side}")
    print(f"{border_side} {'AVAILABLE ATTACKS:':^73} {border_side}")
    
    # Wrap attacks list if too long
    attack_lines = []
    current_line = ""
    for attack in available_attacks:
        if len(current_line) + len(attack) + 2 > 71:
            attack_lines.append(current_line)
            current_line = attack
        else:
            if current_line:
                current_line += ", " + attack
            else:
                current_line = attack
    if current_line:
        attack_lines.append(current_line)
    
    for line in attack_lines:
        print(f"{border_side} {line:<73} {border_side}")
    
    print(f"{border_side} {'-' * 73} {border_side}")
    print(f"{border_side} {'CHOOSE YOUR ATTACK':<73} {border_side}")
    print(border_bottom)

#print("Available attacks:", list(Player.Class.Attacks.keys()))

while True :
    display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.MostraAtaques().split(", "))
    Attack = input("╔═ Attack: ")
    
    if Attack not in Player.Class.Attacks:
        clear()
        print("Invalid attack, please choose a valid attack.")
        continue

    Attack_Info = Player.Class.Attacks[Attack]

    match Attack:
        case "Internal Access":
            Player.Class.Defense += Attack_Info[0]
            clear()
            print(f"Defense increased to {Player.Class.Defense}%.")

        case "Miku Miku Beam":
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
                    final_damage = Damage(Attack_Info, Player.Class.Defense)
                    cText(f"-{final_damage} life! ({x}%)", "red")
                    Player.Integrity -= final_damage
                    print(f"Integrity: {integrity_bar(Player.Integrity, Player.Class.Integrity)}")
                    sleep(0.03)
                    x += 1

        case "Baiting":
            Player.Class.Defense += Attack_Info[0]
            Player.Class.Regen += Attack_Info[1]
            clear()
            print(f"Available attacks: {Player.Class.MostraAtaques()}")
            print(f"Defense increased to {Player.Class.Defense}%.")
            print(f"Regen increased to {Player.Class.Regen}.")

        case "Firewall":
            slash_animation()
            Player.Defense += Attack_Info 
            if Player.Defense >= 100:
                Player.Defense = 99
                Player.Class.Defense = 99
            clear()
            print(f"Available attacks: {Player.Class.MostraAtaques()}")
            print(f"Defense: {defense_bar(Player.Defense)}")

        case "Security Patch":
            Player.Class.Regen += Attack_Info 
            clear()
            print(f"Available attacks: {Player.Class.MostraAtaques()}")
            print(f"Regen increased to {Player.Class.Regen}.")

        case "Pneumoultramicroscopicsilicovolcanoconiotic":
            print("U just got ball cancer, gng how u managed to do that is beyond me ngl")
            sleep(3)
            final_damage = Damage(100000000, Player.Class.Defense)
            Player.Integrity -= final_damage
            clear()
            print(f"Integrity: {integrity_bar(Player.Integrity, Player.Class.Integrity)}")
            sleep(3)
            clear()

        case _:
            print(f"integrity: {PlayerClass.Integrity}")
            final_damage = Damage(Attack_Info, Player.Class.Defense)
            Player.Integrity -= final_damage
            clear()
            print(f"Available attacks: {Player.Class.MostraAtaques()}")
            print(f"Integrity: {integrity_bar(Player.Integrity, Player.Class.Integrity)}")

    if Player.Class.Regen > 0:
        Player.Integrity += Player.Class.Regen
       # Player.Class.Integrity += Player.Class.Regen
        print(f"Available attacks: {Player.Class.MostraAtaques()}")
        print(f"Integrity: {integrity_bar(Player.Integrity, Player.Class.Integrity)}")
        if Player.Integrity >= Player.Class.Integrity: 
            Player.Integrity = Player.Class.Integrity
        Player.Class.Regen = 0

    if Player.Defense >= 100:
        Player.Defense = 99
        Player.Class.Defense = 99

    if Player.Integrity <= 0:
        sleep(2)
        clear()
        cText(f"\n         [!]Error 404[!] \n < -- You have been hacked. -- >\n", "red")
        sleep(2)
        clear()
        break

    