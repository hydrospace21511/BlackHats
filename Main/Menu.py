import os
from Classes.SecurityAnalyticClass import SecurityAnalyticClass
from Classes.HackerClass import HackerClass
from Classes.SocialEngineerClass import SocialEngineerClass
from Classes.Classes import Classes 
from Classes.SecretClasses.Hatsune import HatsuneMikuClass
import Player
from Enemy import Enemy
import sys
from COBALT import COBALT
from time import sleep
from colorama import Fore, Back, Style, init

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
def cText(message, type="info"):
    match type:
        case "red":
            print(f"{Fore.RED}{message}")
        case "yellow":
            print(f"{Fore.YELLOW}{message}")
        case "green":
            print(f"{Fore.GREEN}{message}")
        case "blue":
            print(f"{Fore.BLUE}{message}")
        case "cyan":
            print(f"{Fore.CYAN}{message}")
        case "black":
            print(f"{Fore.BLACK}{message}")
        case "error":
            print(f"{Fore.RED}[!] {message}")
        case "warn":
            print(f"{Fore.YELLOW}[!]{message}")
        case "positive":
            print(f"{Fore.GREEN}[✓]{message}")

print(Classes.ClassesAttacks())
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
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

            case "Hatsune Miku" | "CV01":
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

        case "Miku Miku Beam":
            i = 0
            PlayerClass.Defense = 0
            while i < 100:
                clear()
                if i < 30:
                    cText(f"Miku Miku Beam is charging... {i}%", "red")
                elif i < 60:
                    cText(f"Miku Miku Beam is charging... {i}%", "yellow")
                elif i <= 100:
                    cText(f"Miku Miku Beam is charging... {i}%", "green")
                sleep(0.03)
                i += 1
            if i >= 100:
                clear()
                print("Miku Miku Beam is fully charged!")
                sleep(1)
                clear()
                x = 0
                while x <= 100:
                    clear()
                    final_damage = Damage(Attack_Info, Player.Class.Defense)
                    print(cText(f"-{final_damage} life! ({x}%)", "red"))
                    Player.Class.Integrity -= final_damage
                    print(f"Life left: {Player.Class.MostraVida():.1f}")
                    sleep(0.03)
                    x += 1

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
        print(f"\n           Error 404 \n < -- You have been hacked. -- >\n")
        sleep(2)
        clear()
        break

    