import os
from Classes.SecurityAnalyticClass import SecurityAnalyticClass
from Classes.HackerClass import HackerClass
from Classes.SocialEngineerClass import SocialEngineerClass
from Classes.Classes import Classes 
import Player
from Enemy import Enemy
import sys
Classes = Classes()
from COBALT import COBALT
Enemy = Enemy("a", 100, 1, 0)
Hacker = HackerClass()
SecurityAnalytic = SecurityAnalyticClass()
SocialEngineer = SocialEngineerClass()
Player = Player.Player()
from time import sleep
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
COBALT = COBALT()
COBALT.Start()
print(Classes.ClassesAttacks())



print(SecurityAnalytic.MostraAtaques())
print(Hacker.MostraAtaques())
print(SocialEngineer.MostraAtaques())
clear()
print(Classes.Classes())
ClassesOptions = {
    "SecurityAnalytic": SecurityAnalytic,
    "Hacker": Hacker,
    "Social Engineer": SocialEngineer
}

while True:
    while True:
        PlayerClass = input("Choose your class: ")
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

            case "Security Analytic" | "2":
                PlayerClass = SecurityAnalytic
                break

            case "Hacker" | "1":
                PlayerClass = Hacker
                break

            case "Social Engineer" | "3":
                PlayerClass = SocialEngineer
                break

            case "Evangelion":
                clear()
                print("You have chosen the Evangelion. This class is currently unavailable. (You are not worthy of this class, smh.)")
                sleep(3)
                clear()
                continue

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

# ---- teste ataques ----

def Damage(D, Defense) :
    return D * (1 - Defense / 100)
#print("Available attacks:", list(Player.Class.Attacks.keys()))

while True :
    Attack = input("Choose an attack: ")
    
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

        case "Baiting":
            Player.Class.Defense += Attack_Info[0]
            Player.Class.Regen += Attack_Info[1]
            clear()
            print(f"Defense increased to {Player.Class.Defense}%.")
            print(f"Regen increased to {Player.Class.Regen}.")

        case "Firewall":
            Player.Class.Defense += Attack_Info
            clear()
            print(f"Defense increased to {Player.Class.Defense}%.")

        case "Security Patch":
            Player.Class.Regen += Attack_Info 
            clear()
            print(f"Regen increased to {Player.Class.Regen}.")

        case "Pneumoultramicroscopicsilicovolcanoconiotic":
            print("U just got ball cancer, gng how u managed to do that is beyond me ngl")
            sleep(3)
            final_damage = Damage(100000000, Player.Class.Defense)
            Player.Class.Integrity -= final_damage
            clear()
            print(f"Integrity left after the attack '{Attack}': {Player.Class.Integrity:.1f}")
            sleep(3)
            clear()

        case _:
            final_damage = Damage(Attack_Info, Player.Class.Defense)
            Player.Class.Integrity -= final_damage
            clear()
            print(f"Available attacks: {Player.Class.MostraAtaques()}")
            print(f"Integrity left after the attack '{Attack}': {Player.Class.Integrity:.1f}")

    if Player.Class.Regen > 0:
        Player.Class.Integrity += Player.Class.Regen
        print(f"Integrity regenerated to {Player.Class.Integrity}.")
        Player.Class.Regen = 0
        
    if Player.Class.Integrity <= 0:
        sleep(2)
        clear()
        print("\n           Error 404 \n < -- You have been hacked. -- >\n")
        sleep(2)
        clear()
        break

    