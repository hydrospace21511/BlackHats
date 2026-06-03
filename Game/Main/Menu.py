import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from Game.ItemsLib.Items.TestItem import TestItemClass
from Game.ItemsLib.Items.TestItem2 import TestItem2Class
from Game.Classes.SecurityAnalyticClass import SecurityAnalyticClass
from Game.Main.UI import enemy_life
from Game.Classes.HackerClass import HackerClass
#from Game.Main.Enemy import enemy_life
# from Game.Main.Enemy import random_attack ???
# random_attack()
from Game.Classes.SocialEngineerClass import SocialEngineerClass
from Game.Classes.ReverseEngineerClass import ReverseEngineerClass #mirlo esteve aqui btw
from Game.Classes.Classes import Classes 
from Game.Classes.SecurityBypasser import SecurityBypasserClass
from Game.Classes.HardwareSpecialistClass import HardwareSpecialistClass
from Game.Classes.SecretClasses.Hatsune import HatsuneMikuClass
from Game.Classes.SecretClasses.CorruptedHatsune import CorruptedHatsuneMikuClass
import Game.Main.Player as Player
from Game.ItemsLib.Chests.NPC_Chest import open_chest
from Game.Main.Player import integrity_bar
from Game.Main.Player import defense_bar
from Game.Main.Enemy import Enemy
import sys
from Game.Classes.SecretClasses.Rimuru import RimuruClass
#import Test #test inutil🤣
import getpass
import termios
import tty
from Game.Main.COBALT import COBALT
from time import sleep
from colorama import Fore, Back, Style, init
from Game.Main.Color import cText
from Game.Main.UI import display_battle_ui
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def UA():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                print ("up")

def LA():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\033[B':
                print ("down")

##### lista de erros q "criei": 04: Not found, 201: Not loaded, 302: Class so strong, 666: Secret Class
def user():
    return getpass.getuser()

def funcaoextremamentegrandenaqualseupropositodevidaehjustamenteprintaronomedoplayerpelomotivomaisinexistentedouniversovirgulaelaexisteapenasparaissopontofinalfmaiusculoFoiquandojmaiusculoJairofinalmentepercebeuvirgulaninguemligapraelebrutasobranadaprobetinhakkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk():                                                                                                                                                                                                                                                    # ignora isso, é a maldade q quebra a quarta parede po
    return print(f"Player name: sla o nome dele, nem chegou nessa parte do script ainda, relaxa ai, {user.ip()}")

COBALT = COBALT()
Classes = Classes()
Hacker = HackerClass()
Rimuru = RimuruClass()
SecurityAnalytic = SecurityAnalyticClass()
SecurityBypasser = SecurityBypasserClass()
HardwareSpecialist = HardwareSpecialistClass()
SocialEngineer = SocialEngineerClass()
Vocaloid = HatsuneMikuClass()
ReverseEngineer = ReverseEngineerClass()
CorruptedHatsuneMiku = CorruptedHatsuneMikuClass() #pq to falando sozinho?
Player = Player.Player()
TestItem = TestItemClass()
TestItem2 = TestItem2Class()
init(autoreset=True)
from Game.Attacks.SpecialAttacks import DecompilerAttack, AlgorithmCloneAttack, ProtectionBypassAttack, InternalAccessAttack, BaitingAttack, FirewallAttack, SecurityPatchAttack, DesintegrationAttack, MikuMikuBeamAttack, NegativeSpaceAttack, GiveDamageAttack, PneumoultramicroscopicsilicovolcanoconioticAttack, WorldIsMineAttack, TellYourWorldAttack, SystemOverrideAttack

attack_functions = {
    "Decompiler": DecompilerAttack,
    "Algorithm Clone": AlgorithmCloneAttack,
    "Protection Bypass": ProtectionBypassAttack,
    "Internal Access": InternalAccessAttack,
    "Miku Miku Beam": MikuMikuBeamAttack,
   # "MMB": MikuMikuBeamAttack,
    "Tell Your World": TellYourWorldAttack,
    "World Is Mine": WorldIsMineAttack,
    "Baiting": BaitingAttack,
    "Firewall": FirewallAttack,
    "Security Patch": SecurityPatchAttack,
    "Pneumoultramicroscopicsilicovolcanoconiotic": PneumoultramicroscopicsilicovolcanoconioticAttack,
    "Desintegration": DesintegrationAttack,
   # "Give Damage": GiveDamageAttack,
    "Negative Space": NegativeSpaceAttack,
    "System Override": SystemOverrideAttack
}

#pra but q n souber, cText é Colored Text (abreviei pq é games e seco filho, liso liso liso)
#isso tava aqui antes de eu colocar o cText em um arquivo diferente, fui moggado? games

print(Classes.ClassesAttacks())
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear() 

# while True:
    
#     menu_option = 1
#     if UA():
#         menu_option += 1 #ignora isso, é teste q vai vir pro jogo futuramente (de jeito mior)
#     elif LA():
#         menu_option -= 1
#     if menu_option < 1:
#         menu_option = 3
#         COBALT._Help_menu()
#     elif menu_option > 3:
#         menu_option = 1
#         COBALT._Exit_menu()
#     # match menu_option:
#     #     case 1|3:
#     #         COBALT._Start_menu() 
#     #         break
#     #     case 2|0:
#     #         COBALT._Help_menu() 
#     #         break

COBALT.start()
clear()
Classes._Classes() 
ClassesOptions = {
    "SecurityAnalytic": SecurityAnalytic,
    "Hacker": Hacker,
    "Social Engineer": SocialEngineer,
    "Reverse Engineer": ReverseEngineer,
    "SecurityBypasser": SecurityBypasser,
    "HardwareSpecialist": HardwareSpecialist
} 

ClassPage = 1

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
            
            case "SECURITY BYPASSER" | "6":
                PlayerClass = SecurityBypasser
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
                
            
            case "NEXT PAGE" | "NEXT" | "PAGE":  
                if ClassPage == 1:
                    clear()
                    Classes._Classes2() 
                    ClassPage = 2

                elif ClassPage == 2:
                    clear()
                    Classes._Classes3() 
                    ClassPage = 3

                elif ClassPage == 3:
                    clear()
                    Classes._Classes() 
                    ClassPage = 1

            case "PREVIOUS PAGE" | "PREVIOUS" | "BACK":
                if ClassPage == 1:
                    clear()
                    Classes._Classes3() 
                    ClassPage = 3

                elif ClassPage == 2:
                    clear()
                    Classes._Classes() 
                    ClassPage = 1

                elif ClassPage == 3:
                    clear()
                    Classes._Classes2() 
                    ClassPage = 2

            case _:
                clear()
                if ClassPage == 1:
                        Classes._Classes() 

                elif ClassPage == 2:            #EM MINHA DEFESA NAO FUI EU QUE FIZ, UMA IA ALEATORIA INVADIU MEU PC E FEZ ESSA OBRA SATANICA DE IF E ELSE PRA MUDAR DE PAGINA, EU JURO QUE NAO FUI EU, EU SO QUERIA COLOCAR UM PROXIMO E ANTERIOR SIMPLES, MAS A IA DISSE "NAO, VAMOS FAZER UM SISTEMA DE PAGINAÇÃO COMPLETO COM CONTADORES E TUDO" E EU FIQUEI COM PREGUIÇA DE DISCUTIR COM A IA PQ ELA É MEU AMIGO, ENTÃO PRONTO, O RESULTADO É ESSE AQUI, EU JURO QUE NAO FUI EU QUE FIZ ISSO
                        Classes._Classes2() 

                elif ClassPage == 3:
                        Classes._Classes3() 
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

current_enemy = Enemy(name="filth", max_health=500, defense=15, regen=0, attacks=enemy_attacks) #talvez em coloque em uma pasta separada como "Enemies" junto com os ataque pra dar uma otimizada e organizada
active_cooldowns = {}
#Protection
def Damage(D, Defense) :
    return D * (1 - Defense / 100)



#print("Available attacks:", list(Player.Class.Attacks.keys()))
clear()
# if PlayerClass == Vocaloid:
#     Player.Integrity -= 207 * 9

# if PlayerClass == Hacker: # vai ser mudado para o sistema de baú, é só p testar mesmo (pa ri e resenha)
#     cText(" To só debuggando mesmo, pode escolher o ataque tranquilo", "warn")
#     if Player.Class.Items == "None":
#         Player.Class.Items = {TestItem, TestItem2, TestItem2, TestItem2}
#     print("O mano, vc ta com os seguintes items: sla, de nada ai")
#     sleep(3)

enemy_life(current_enemy, integrity_bar)
display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
while True:
    while True :
        if type(Player.Class) == CorruptedHatsuneMikuClass:
            cText("▶  Choose an exploit >>","red")
        else:
            cText("▶  Choose an exploit >>","green")
        Attack = input("")    
        
        if Attack == "Reverse" and Player.Class.Decompiled == True:
            clear()
            enemy_life(current_enemy, integrity_bar)
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
            enemy_life(current_enemy, integrity_bar)
            display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
            cText("⚠  ERROR 04: Exploit not found", "red")
            continue

        if Attack in active_cooldowns and active_cooldowns[Attack] > 0:
                clear()
                enemy_life(current_enemy, integrity_bar)
                display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
                cText(f"⚠  ACCESS DENIED: '{Attack}' is cooling down! ({active_cooldowns[Attack]} turns left)", "yellow")
                continue
        
        base_damage, damage_per_level = Player.Class.Attacks[Attack]
        Attack_Info = base_damage + (damage_per_level * (Player.Level - 1))
        #Attack_Info = Player.Class.Attacks[Attack]
        context = Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, Player.Class

        if Attack in attack_functions:
            attack_functions[Attack](*context)

        if Attack == "Give Damage":
            Player.Integrity -= Attack_Info

        if hasattr(current_enemy, "SkipTurn") and current_enemy.SkipTurn == True:
            cText(">> Enemy turn skipped!", "yellow")
            current_enemy.SkipTurn = False
            sleep(2)
            clear()
            enemy_life(current_enemy, integrity_bar)
            display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
            continue

        else:
            clear()
            
            enemy_life(current_enemy, integrity_bar)
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
            sleep(4)
            clear()
            Player.Level += 1
            current_enemy.Health += current_enemy.MaxHealth * 0.5
            open_chest(Player)
            Integrity_boost = sum(item.Integrity for item in Player.Class.Items)
            Defense_boost = sum(item.Defense for item in Player.Class.Items)
            Player.Defense += Defense_boost
            Player.Integrity += Integrity_boost
            clear()
            enemy_life(current_enemy, integrity_bar)
            display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
            sleep(3)
            cText(f" ur level is {Player.Level}, how u managed to do that? (this message will change)", "warn")
            sleep(3)
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
            enemy_life(current_enemy, integrity_bar)
            display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
            clear()
            Player.Integrity += PlayerClass.Integrity
            current_enemy.Health += current_enemy.MaxHealth
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
        enemy_life(current_enemy, integrity_bar)
        display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)