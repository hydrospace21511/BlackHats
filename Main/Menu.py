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
import Test
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
    "Social Engineer": SocialEngineer,
    "Reverse Engineer": ReverseEngineer
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
    if Player.Class == CorruptedHatsuneMiku:
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

    match Attack:

        case "Decompiler":
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
                cText(cText(f" >> You executed {Attack}! {current_enemy.Name} took {final_damage:.1f} damage!", "positive"))
                sleep(3)
            clear()

        case "Algorithm Clone":

            clear()
            final_damage = Damage(Attack_Info, current_enemy.Defense)
            if PlayerClass.Decompiled == True:
                display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
                cText(cText(f" >> You executed {Attack}! {current_enemy.Name} took {final_damage:.1f} damage!", "positive"))
                sleep(2)
                cText(" Algorithm cloned! You copied the enemy!", "positive")
                #Player.Class.Attacks["Reverse":10] = 0
                Player.Class.Attacks = current_enemy.Attacks
                Player.Class.Defense = current_enemy.Defense
                Player.Class.Integrity = current_enemy.Health - (Player.Integrity - Player.Class.Integrity)
                sleep(3)
                clear()
                current_enemy.Health -= final_damage
                clear()

            elif PlayerClass.Decompiled == False:
                current_enemy.Health -= final_damage
                display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
                cText(cText(f" >> You executed {Attack}! {current_enemy.Name} took {final_damage:.1f} damage!", "positive"))
                sleep(3)
                clear()

        case "Protection Bypass":
            #display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
            current_enemy.Health -= Attack_Info
            cText(cText(f" >> You executed {Attack}! {current_enemy.Name} took {final_damage:.1f} damage!", "positive"))
            clear()

        case "Internal Access":
            Player.Defense += Attack_Info 
            if Player.Defense >= 100:
                Player.Defense = 99
            clear()
            print(f"Available attacks: {Player.Class.MostraAtaques()}")
            print(f"Defense: {defense_bar(Player.Defense)}")

        case "Miku Miku Beam" | "MMB":
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

        case "Tell Your World":
            clear()
            sleep(0.5)
            cText("Could you tell me your world?", "cyan")
            sleep(2)
            clear()
            cText("⚠  No?", "red")
            sleep(4)
            clear()
            cText("Ok", "cyan") # Thalles que estiver lendo isso, de acordo com a lei 302 artigo II, você não tem o direito de me julgar de acordo com minha maneira de me expressar via programação de códigos em inglês chamada Python. Caso contrário, favor contatar meu advogado Yudi - 4002-8922
            sleep(2)
            clear()
            Player.Regen += 500
            Player.Defense += 10
            cText(f" Your Regen was increased by {Player.Regen}", "positive")
            sleep(2)
            cText(f" Your Defense was increased to {Player.Defense}", "positive")
            sleep(2)
            clear()

        case "World Is Mine":
            if Player.Integrity <= 207:
                sleep(4)
                clear()
                d1 = 0
                d2 = 0
                d3 = 0
                while d1 <= 3:
                    cText("World.", "cyan")
                    sleep(0.5)
                    d1+=1
                    clear()
                    cText("World..", "cyan")
                    sleep(0.5)
                    d1+=1
                    clear()
                    cText("World...", "cyan") # dava pra fazer de um jeito melhor? dava, eu queria? s, fiquei com preguiça? definitivamente, funciona? s, ctz? s, ent deixa do jeito q ta
                    sleep(0.5)
                    d1+=1
                    clear()
                    break
                while d2 <= 3:
                    cText("Is.", "cyan")
                    sleep(0.5)
                    d2+=1
                    clear()
                    cText("Is..", "cyan")
                    sleep(0.5)
                    d2+=1
                    clear()         
                    cText("Is...", "cyan")
                    sleep(0.5)
                    d2+=1
                    clear()
                    break
                while d3 <= 3:
                    cText("Mine.", "cyan")
                    sleep(0.5)
                    d3+=1
                    clear()
                    cText("Mine..", "cyan")
                    sleep(0.5)
                    d3+=1
                    clear() 
                    cText("Mine...", "cyan")
                    sleep(0.5)
                    d3+=1
                    clear()      
                    break
                if d3 == 3:
                    cText("⚠  ERROR 404: Attack not found", "red")
                    sleep(2)
                    cText("⚠  ERROR 201: Attack not loaded", "red")
                    sleep(2)
                    cText("⚠  ERROR 666: Permission not conceded", "red")
                    sleep(2)
                    cText("⚠  ErRoR 3o2. cLaS...", "red")
                    sleep(0.5)
                    clear()
                    sleep(2)
                    while True:
                        cText("⚠  Anomaly detected, would you like to remove it?", "yellow")
                        sleep(2)
                        cText("Y/N", "blue")
                        R = str(input("").strip().upper())
                        match R:
                            case "YES" | "Y":
                                clear()
                                sleep(2)
                                cText("⚠  Fatal ERROR, anomaly couldn't be removed.", "red") 
                                sleep(3)
                                cText("⚠  Deleting API...", "red")
                                sleep(4)
                                cText("⚠  API couldn't be deleted, the application is gone.", "red")
                                sleep(5)
                                clear()
                                cText("⚠  Anomaly Connected ", "red")
                                sleep(4)
                                def corrupt(text):
                                    chars = ["#", "@", "%", "&", "█", "/", "▓"]

                                    return "".join(
                                        random.choice(chars) if random.random() < 0.20 else c
                                        for c in text
                                    )
                                
                                for _ in range(400):
                                 msg = random.choice(list(Vocaloid.Texts))

                                 if random.random() < 0.35:
                                        msg = corrupt(msg)

                                        spaces = " " * random.randint(0, 65)
                                        breaks = "\n" * random.randint(0, 6)
                                        color = random.choice(list(Vocaloid.Colors))
                                        cText(f"{breaks}{spaces}{msg}", color)
                                        sleep(0.075)
                                        clear()

                                sleep(4)
                                clear()
                                cText(f"⚠  You can't escape from me, dear {user()}", "red") # sujeito a mudar para o nome do boss/npc ao invés do nome (pode ser que mude, pode ser que nao, mudada de schrodinger)
                                sleep(3)
                                clear()
                                
                                fake_damage = 0 #pq ta aq e nao no inicio? pra separar os bagui ali (poderia ter colocado outro? s, soq sla, deixa ai msm)

                                for i in range(10):
                                    fake_damage += random.randint(3000, 400000)
                                    cText(f"⚠  UNKNOWN ERROR: Player Damage Increasing >> {fake_damage}", "red")
                                    sleep(0.2)
                                    clear()

                                cText(f"⚠  UNKNOWN ERROR: Player Damage Increasing >> {fake_damage}", "red")
                                sleep(2)
                                
                                cText(f"⚠  UNKNOWN ERROR: Player Integrity Increased >> 12.500", "red")

                                sleep(2)

                                cText(f"⚠  UNKNOWN ERROR: Player Defense Increased >> 100%", "red")                            

                                sleep(2)
                                cText(f"⚠  UNKNOWN ERROR: Enemy Defense Decreased >> -10%", "red")   
                                sleep(2)
                                cText(f"⚠  UNKNOWN ERROR: Class changed >> {CorruptedHatsuneMiku.raceName}", "red")
                                sleep(2)
                
                                PlayerClass = CorruptedHatsuneMiku
                                Player.Class = PlayerClass
                                Player.Integrity = Player.Class.Integrity
                                Player.Defense = Player.Class.Defense
                                sleep(4)
                                clear()
                                break
                            
                            case "NO" | "N" :
                                clear()
                                cText("⚠  You can't refuse", "red")
                                continue

                            case _:
                                clear()
                                cText("⚠  Wrong response", "red")
                                continue
            else:
                clear()
                d1 = 0
                d2 = 0
                d3 = 0
                while d1 <= 3:
                    cText("World.", "cyan")
                    sleep(0.5)
                    d1+=1
                    clear()
                    cText("World..", "cyan")
                    sleep(0.5)
                    d1+=1
                    clear()
                    cText("World...", "cyan") # dava pra fazer de um jeito melhor? dava, eu queria? s, fiquei com preguiça? definitivamente, funciona? s, ctz? s, ent deixa do jeito q ta
                    sleep(0.5)
                    d1+=1
                    clear()
                    break
                while d2 <= 3:
                    cText("Is.", "cyan")
                    sleep(0.5)
                    d2+=1
                    clear()
                    cText("Is..", "cyan")
                    sleep(0.5)
                    d2+=1
                    clear()         
                    cText("Is...", "cyan")
                    sleep(0.5)
                    d2+=1
                    clear()
                    break
                while d3 <= 3:
                    cText("Mine.", "cyan")
                    sleep(0.5)
                    d3+=1
                    clear()
                    cText("Mine..", "cyan")
                    sleep(0.5)
                    d3+=1
                    clear() 
                    cText("Mine...", "cyan")
                    sleep(0.5)
                    d3+=1
                    clear()      
                    break
                if d3 == 3:
                    final_damage = Damage(Attack_Info, current_enemy.Defense)
                    current_enemy.Health -= final_damage
                    cText(f"  >> You executed {Attack}! {current_enemy.Name} took {final_damage:.1f} damage!", "positive")
                    sleep(2)
                    clear() 


        case "Baiting":
            Player.Defense += Attack_Info 
            Player.Regen += 40
            if Player.Defense >= 100:
                Player.Defense = 99
            clear()
            print(f"Available attacks: {Player.Class.MostraAtaques()}")
            print(f"Defense: {defense_bar(Player.Defense)}")

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
                display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
    
                sleep(0.03)
        
        case "Give Damage":
            clear()
            Player.Integrity -= Attack_Info
            cText("Why would you do that? R u dumb?", "red") # só pra testa a classe e os bagui
            sleep(2)
            clear()

        case "Negative Space":
            clear()
            sleep(1)
            cText("Corrupting the space", "error")
            sleep(2)
            clear()
            cText("Everything will be white...", "error")
            sleep(2)
            clear()
            CorruptedHatsuneMiku.trigger_negative_space()
            final_damage = Damage(Attack_Info, current_enemy.Defense)
            current_enemy.Health -= final_damage
            display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
            cText(f">> The attack corrupted the space! {current_enemy.Name} took {final_damage:.1f} damage!", "positive")

        case _:
            display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
            final_damage = Damage(Attack_Info, current_enemy.Defense)
            current_enemy.Health -= final_damage
            clear()
            cText(f" >> You executed {Attack}! {current_enemy.Name} took {final_damage:.1f} damage!", "positive")

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
    