import os
import sys
import getpass
from time import sleep

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from Game.ItemsLib.Items.TestItem import TestItemClass
from Game.ItemsLib.Items.TestItem2 import TestItem2Class
from Game.Classes.SecurityAnalyticClass import SecurityAnalyticClass
from Game.Main.UI import enemy_life, display_battle_ui
from Game.Classes.HackerClass import HackerClass
from Game.Classes.SocialEngineerClass import SocialEngineerClass
from Game.Classes.ReverseEngineerClass import ReverseEngineerClass 
from Game.Classes.Classes import Classes 
from Game.Classes.SecurityBypasser import SecurityBypasserClass
from Game.Classes.HardwareSpecialistClass import HardwareSpecialistClass
from Game.Classes.SecretClasses.Hatsune import HatsuneMikuClass
from Game.Classes.SecretClasses.CorruptedHatsune import CorruptedHatsuneMikuClass
from Game.Classes.SecretClasses.Rimuru import RimuruClass
import Game.Main.Player as PlayerModule
from Game.ItemsLib.Chests.NPC_Chest import open_chest
import Game.Main.Player as PlayerStats
from Game.Main.Player import integrity_bar, defense_bar
from Game.Main.Enemy import Enemy
from colorama import Fore, Back, Style, init
from Game.Main.Color import cText

init(autoreset=True)

from Game.Attacks.SpecialAttacks import (DecompilerAttack, AlgorithmCloneAttack, ProtectionBypassAttack, InternalAccessAttack, BaitingAttack, FirewallAttack, SecurityPatchAttack, DesintegrationAttack, MikuMikuBeamAttack, NegativeSpaceAttack, GiveDamageAttack, PneumoultramicroscopicsilicovolcanoconioticAttack, WorldIsMineAttack, TellYourWorldAttack, SystemOverrideAttack)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def user():
    return getpass.getuser()

def funcaoextremamentegrandenaqualseupropositodevidaehjustamenteprintaronomedoplayerpelomotivomaisinexistentedouniversovirgulaelaexisteapenasparaissopontofinalfmaiusculoFoiquandojmaiusculoJairofinalmentepercebeuvirgulaninguemligapraelebrutasobranadaprobetinhakkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk():                                                                                                                                                                                                                                                    
    return print(f"Player name: sla o nome dele, nem chegou nessa parte do script ainda, relaxa ai, {user()}")

def Damage(D, Defense):
    return D * (1 - Defense / 100)

class DarkHatsGame:
    def __init__(self):
        self.ClassesMenu = Classes()
        self.Hacker = HackerClass()
        self.Rimuru = RimuruClass()
        self.SecurityAnalytic = SecurityAnalyticClass()
        self.SecurityBypasser = SecurityBypasserClass()
        self.HardwareSpecialist = HardwareSpecialistClass()
        self.SocialEngineer = SocialEngineerClass()
        self.Vocaloid = HatsuneMikuClass()
        self.ReverseEngineer = ReverseEngineerClass()
        self.CorruptedHatsuneMiku = CorruptedHatsuneMikuClass()
        self.Player = PlayerModule.Player()
        
        self.attack_functions = {
            "Decompiler": DecompilerAttack,
            "Algorithm Clone": AlgorithmCloneAttack,
            "Protection Bypass": ProtectionBypassAttack,
            "Internal Access": InternalAccessAttack,
            "Miku Miku Beam": MikuMikuBeamAttack,
            "Tell Your World": TellYourWorldAttack,
            "World Is Mine": WorldIsMineAttack,
            "Baiting": BaitingAttack,
            "Firewall": FirewallAttack,
            "Security Patch": SecurityPatchAttack,
            "Pneumoultramicroscopicsilicovolcanoconiotic": PneumoultramicroscopicsilicovolcanoconioticAttack,
            "Desintegration": DesintegrationAttack,
            "Negative Space": NegativeSpaceAttack,
            "System Override": SystemOverrideAttack
        }

    def start(self):
        clear()

        self.ClassesMenu._Classes() 
        ClassPage = 1

        while True:
            while True:
                if self.Player.Class == self.CorruptedHatsuneMiku:
                    cText("▶  Choose your class >>", "red")
                else:
                    cText("▶  Choose your class >>", "green")
                
                PlayerClassInput = str(input("").strip().upper())

                match PlayerClassInput:
                    case "EXIT":
                        print("\n        Initializing exit sequence...")     
                        sleep(2)
                        print("            Exiting darkhats.flat...")
                        sleep(1)
                        clear()
                        return 

                    case "SECURITY ANALYTIC" | "2":
                        PlayerClass = self.SecurityAnalytic
                        break
                    case "REVERSE ENGINEER" | "4":
                        PlayerClass = self.ReverseEngineer
                        break
                    case "HACKER" | "1":
                        PlayerClass = self.Hacker
                        break
                    case "SOCIAL ENGINEER" | "3":
                        PlayerClass = self.SocialEngineer
                        break
                    case "HARDWARE SPECIALIST" | "5":
                        PlayerClass = self.HardwareSpecialist
                        break
                    case "SECURITY BYPASSER" | "6":
                        PlayerClass = self.SecurityBypasser
                        break
                    case "HATSUNE MIKU" | "CV01":
                        PlayerClass = self.Vocaloid
                        break
                    case "RIMURU" | "SLIME":
                        PlayerClass = self.Rimuru
                        break
                        
                    case "SECRET" | "666":
                        clear()
                        cText("⚠  ERROR 666: Secret Activated", "red")
                        sleep(2)
                        cText("Yes, there are secret classes", "red")
                        sleep(1.5)
                        
                        while True:
                            clear()
                            cText("Wanna a hint? (Y/N)", "cyan")
                            hint = str(input("").strip().upper())
                            match hint:
                                case "YES" | "Y":
                                    clear()
                                    cText("https://pastebin.com/2snJpKM9", "cyan")
                                    sleep(5)
                                    clear()
                                    self.ClassesMenu._Classes() 
                                    break
                                case "NO" | "N":
                                    clear()
                                    self.ClassesMenu._Classes() 
                                    break
                                case _:
                                    clear()
                                    cText("⚠  ERROR 04: Response not found", "red")
                                    sleep(1)
                                    continue
                    
                    case "NEXT PAGE" | "NEXT" | "PAGE":  
                        clear()
                        if ClassPage == 1:
                            self.ClassesMenu._Classes2() 
                            ClassPage = 2
                        elif ClassPage == 2:
                            self.ClassesMenu._Classes3() 
                            ClassPage = 3
                        elif ClassPage == 3:
                            self.ClassesMenu._Classes() 
                            ClassPage = 1

                    case "PREVIOUS PAGE" | "PREVIOUS" | "BACK":
                        clear()
                        if ClassPage == 1:
                            self.ClassesMenu._Classes3() 
                            ClassPage = 3
                        elif ClassPage == 2:
                            self.ClassesMenu._Classes() 
                            ClassPage = 1
                        elif ClassPage == 3:
                            self.ClassesMenu._Classes2() 
                            ClassPage = 2

                    case _:
                        clear()
                        if ClassPage == 1: self.ClassesMenu._Classes() 
                        elif ClassPage == 2: self.ClassesMenu._Classes2() 
                        elif ClassPage == 3: self.ClassesMenu._Classes3() 
                        cText("⚠  ERROR 04: Class not found", "red")
                        continue

            cText("▶  Enter your name >>", "green")            
            self.Player.Name = input("")
            if self.Player.Name == "Return":
                print("Returning to class selection...")
                clear()
                continue
            else:
                break

        self.Player.Class = PlayerClass    
        self.Player.Integrity = self.Player.Class.Integrity
        self.Player.Defense = self.Player.Class.Defense
        self.Player.Regen = self.Player.Class.Regen
        
        clear()
        cText(f">> Welcome {self.Player.Name}!", "green")
        sleep(2)
        cText(f">> Your class is: {self.Player.Class.raceName}", "green")
        sleep(2)
        clear()

        enemy_attacks = {
            "Shadow Strike": 20,
            "Inferno Blast": 60,
            "Phantom Slash": 70,
            "Chaos Roar": 100
        }
        current_enemy = Enemy(name="filth", max_health=500, defense=15, regen=0, attacks=enemy_attacks)
        active_cooldowns = {}

        enemy_life(current_enemy, integrity_bar)
        display_battle_ui(self.Player.Integrity, self.Player.Class.Integrity, self.Player.Defense, self.Player.Class.Attacks.keys(), self.Player.Class.ui_color)
        
        while True:
            while True:
                if type(self.Player.Class) == type(self.CorruptedHatsuneMiku):
                    cText("▶  Choose an exploit >>", "red")
                else:
                    cText("▶  Choose an exploit >>", "green")
                    
                Attack = input("")    
                
                if Attack == "Reverse" and getattr(self.Player.Class, 'Decompiled', False):
                    clear()
                    enemy_life(current_enemy, integrity_bar)
                    display_battle_ui(self.Player.Integrity, self.Player.Class.Integrity, self.Player.Defense, self.Player.Class.Attacks.keys(), self.Player.Class.ui_color)
                    cText(" Reversing the decompilation...", "warn")
                    sleep(2)
                    cText(" Decompilation reversed! Your original stats and attacks were restored!", "positive")
                    sleep(2)
                    self.Player.Class.Decompiled = False
                    self.Player.Class.Attacks = self.Player.Class.OriginalAttacks
                    self.Player.Class.Defense = self.Player.Class.DefenseBackup
                    self.Player.Class.Integrity = self.Player.Class.IntegrityBackup
                    clear()
                
                if Attack not in self.Player.Class.Attacks:
                    clear()
                    enemy_life(current_enemy, integrity_bar)
                    display_battle_ui(self.Player.Integrity, self.Player.Class.Integrity, self.Player.Defense, self.Player.Class.Attacks.keys(), self.Player.Class.ui_color)
                    cText("⚠  ERROR 04: Exploit not found", "red")
                    continue

                if Attack in active_cooldowns and active_cooldowns[Attack] > 0:
                    clear()
                    enemy_life(current_enemy, integrity_bar)
                    display_battle_ui(self.Player.Integrity, self.Player.Class.Integrity, self.Player.Defense, self.Player.Class.Attacks.keys(), self.Player.Class.ui_color)
                    cText(f"⚠  ACCESS DENIED: '{Attack}' is cooling down! ({active_cooldowns[Attack]} turns left)", "yellow")
                    continue
                
                base_damage, damage_per_level = self.Player.Class.Attacks[Attack]
                Attack_Info = base_damage + (damage_per_level * (self.Player.Level - 1))
                
                context = (self.Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, self.Player.Class)

                if Attack in self.attack_functions:
                    self.attack_functions[Attack](*context)

                if Attack == "Give Damage":
                    self.Player.Integrity -= Attack_Info

                if hasattr(current_enemy, "SkipTurn") and current_enemy.SkipTurn == True:
                    cText(">> Enemy turn skipped!", "yellow")
                    current_enemy.SkipTurn = False
                    sleep(2)
                    clear()
                    enemy_life(current_enemy, integrity_bar)
                    display_battle_ui(self.Player.Integrity, self.Player.Class.Integrity, self.Player.Defense, self.Player.Class.Attacks.keys(), self.Player.Class.ui_color)
                    continue
                else:
                    clear()
                    enemy_life(current_enemy, integrity_bar)
                    display_battle_ui(self.Player.Integrity, self.Player.Class.Integrity, self.Player.Defense, self.Player.Class.Attacks.keys(), self.Player.Class.ui_color)
                    final_damage = Damage(Attack_Info, current_enemy.Defense)
                    current_enemy.Health -= final_damage
                    cText(f" >> You executed [{Attack}]! {current_enemy.Name} took {final_damage:.1f} damage!", "positive")

                if hasattr(self.Player.Class, 'Cooldowns') and Attack in self.Player.Class.Cooldowns:
                    active_cooldowns[Attack] = self.Player.Class.Cooldowns[Attack]

                if current_enemy.Health <= 0:
                    sleep(1.5)                                          
                    clear()
                    cText(f"\n   [>> NODE COMPROMISED <<]\n < -- {current_enemy.Name} Defeated! -- >\n", "green")
                    sleep(4)
                    clear()
                    self.Player.Level += 1
                    current_enemy.Health += current_enemy.MaxHealth * 0.5
                    import Game.Main.Player as PlayerStats
                    PlayerStats.record_task_completed()
                    
                    if self.Player.Class.Items != {"testItem", "testItem2"}:
                        chest_opened = open_chest(self.Player)
                        if chest_opened:
                            PlayerStats.record_chest_opened()
                        
                    Integrity_boost = sum(item.Integrity for item in getattr(self.Player.Class, 'Items', []))
                    Defense_boost = sum(item.Defense for item in getattr(self.Player.Class, 'Items', []))
                    self.Player.Defense += Defense_boost
                    self.Player.Integrity += Integrity_boost
                    
                    clear()
                    enemy_life(current_enemy, integrity_bar)
                    display_battle_ui(self.Player.Integrity, self.Player.Class.Integrity, self.Player.Defense, self.Player.Class.Attacks.keys(), self.Player.Class.ui_color)
                    sleep(3)
                    cText(f" ur level is {self.Player.Level}, how u managed to do that? (this message will change)", "warn")
                    sleep(3)
                    return 

                sleep(1.5)
                break 

            enemy_attack_name, enemy_attack_dmg = current_enemy.random_attack()
            enemy_final_damage = Damage(enemy_attack_dmg, self.Player.Defense)
            self.Player.Integrity -= enemy_final_damage
            
            cText(f" >> {current_enemy.Name} retaliates with [{enemy_attack_name}]! You took {enemy_final_damage:.1f} damage!", "error")
            sleep(2.5)

            if self.Player.Integrity <= 0:
                clear()
                cText(f"\n        [!]Error 404[!] \n < -- You have been hacked. -- >\n", "red")
                sleep(2)
                enemy_life(current_enemy, integrity_bar)
                display_battle_ui(self.Player.Integrity, self.Player.Class.Integrity, self.Player.Defense, self.Player.Class.Attacks.keys(), self.Player.Class.ui_color)
                sleep(3)
                clear()
                return

            for skill in active_cooldowns:
                if active_cooldowns[skill] > 0:
                    active_cooldowns[skill] -= 1

            if self.Player.Regen > 0:
                self.Player.Integrity += self.Player.Regen
                if self.Player.Integrity >= self.Player.Class.Integrity: 
                    self.Player.Integrity = self.Player.Class.Integrity
                self.Player.Regen = 0

            if self.Player.Defense >= 100:
                self.Player.Defense = 99
                
            clear() 
            enemy_life(current_enemy, integrity_bar)
            display_battle_ui(self.Player.Integrity, self.Player.Class.Integrity, self.Player.Defense, self.Player.Class.Attacks.keys(), self.Player.Class.ui_color)