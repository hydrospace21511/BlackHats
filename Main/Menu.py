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
from Classes.SecretClasses.Rimuru import RimuruClass
import Test
from COBALT import COBALT
from time import sleep
from colorama import Fore, Back, Style, init
from Color import cText
from UI import display_battle_ui

 

COBALT = COBALT()
Classes = Classes()
Enemy = Enemy("a", 100, 1, 0)
Hacker = HackerClass()
Rimuru = RimuruClass()
SecurityAnalytic = SecurityAnalyticClass()
SocialEngineer = SocialEngineerClass()
Vocaloid = HatsuneMikuClass()
Player = Player.Player()
init(autoreset=True)

#pra but q n souber, cText é Colored Text (abreviei pq é games e seco filho, liso liso liso)
#isso tava aqui antes de eu colocar o cText em um arquivo diferente, fui moggado? games

print(Classes.ClassesAttacks())
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear() 
COBALT._Start() 

print(SecurityAnalytic.MostraAtaques())
print(Hacker.MostraAtaques())
print(SocialEngineer.MostraAtaques())
print(Vocaloid.MostraAtaques())
print(Rimuru.MostraAtaques())
clear()
Classes._Classes() 
ClassesOptions = {
    "SecurityAnalytic": SecurityAnalytic,
    "Hacker": Hacker,
    "Social Engineer": SocialEngineer
} 

while True:
    while True:
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

            case "HACKER" | "1":
                PlayerClass = Hacker
                break

            case "SOCIAL ENGINEER" | "3":
                PlayerClass = SocialEngineer
                break

            case "HATSUNE MIKU" | "CV01":
                PlayerClass = Vocaloid
                break
            case "RIMURU" | "SLIME":
                PlayerClass = Rimuru
                break
                

            case _:
                clear()
                print("Invalid class. Please choose again.")
                continue

    cText("▶  Enter your name >>","green")            
    Player.Name = input(" ")
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
cText(f">> Your class is: {Player.Class.RaceName()}","green")
sleep(2)
clear()
#print(Player.Name)
print(f"Available attacks: {Player.Class.MostraAtaques()}")
print(f"Integrity: {integrity_bar(Player.Class.Integrity, PlayerClass.Integrity)}")

# ---- teste ataques ----

def Damage(D, Defense) :
    return D * (1 - Defense / 100)
#print("Available attacks:", list(Player.Class.Attacks.keys()))
clear()
display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys())

while True :
    cText("▶  Choose an exploit >>","green")
    Attack = input("")
    
    if Attack not in Player.Class.Attacks:
        clear()
        print("Invalid attack, please choose a valid attack.")
        sleep(1.5)
        clear()
        display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys())
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

        case "Desintegration":
            clear()
            cText("I summon the DeepWeb slimes", "red")
            sleep(2)
            for i in range(100):
                final_damage = Damage(80, Player.Class.Defense)
                Player.Integrity -= final_damage
                clear()
                display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys())
    
                sleep(0.03)
                
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
    clear()
    display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys())
    
    if Player.Integrity <= 0:
        sleep(2)
        clear()
        cText(f"\n         [!]Error 404[!] \n < -- You have been hacked. -- >\n", "red")
        sleep(2)
        clear()
        break

    