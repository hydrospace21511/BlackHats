import os
import sys
import getpass
from time import sleep
from rich.console import Console, Group
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.live import Live
from rich.spinner import Spinner
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeRemainingColumn



sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from Game.Main.COBALT import COBALT_FS
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
from Game.Classes.LambdaClass import LambdaClass
import Game.Main.Player as PlayerModule
from Game.ItemsLib.Chests.NPC_Chest import open_chest
import Game.Main.Player as PlayerStats
from Game.Main.Player import integrity_bar, defense_bar
from Game.Main.Enemy import Enemy
from Game.Main.RouteManager import RouteManager
from colorama import Fore, Back, Style, init
from Game.Main.Color import cText

init(autoreset=True)

from Game.Attacks.SpecialAttacks import (DecompilerAttack, AlgorithmCloneAttack, ProtectionBypassAttack, InternalAccessAttack, BaitingAttack, FirewallAttack, SecurityPatchAttack, DesintegrationAttack, MikuMikuBeamAttack, NegativeSpaceAttack, GiveDamageAttack, PneumoultramicroscopicsilicovolcanoconioticAttack, WorldIsMineAttack, TellYourWorldAttack, SystemOverrideAttack)

true_level = 0
def get_key():
    if os.name == 'nt':
        import msvcrt
        key = msvcrt.getch()
        if key == b'\xe0': 
            special = msvcrt.getch()
            if special == b'H': return 'UP'
            if special == b'P': return 'DOWN'
            if special == b'K': return 'LEFT' 
            if special == b'M': return 'RIGHT' 
        elif key in (b'\r', b'\n'):
            return 'ENTER'
        elif key == b' ':
            return 'SPACE'
        return None
    else:
        import tty, termios, sys
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            if ch == '\x1b': 
                ch2 = sys.stdin.read(1)
                if ch2 == '[':
                    ch3 = sys.stdin.read(1)
                    if ch3 == 'A': return 'UP'
                    if ch3 == 'B': return 'DOWN'
                    if ch3 == 'C': return 'RIGHT' 
                    if ch3 == 'D': return 'LEFT' 
            elif ch in ('\r', '\n'):
                return 'ENTER'
            elif ch == ' ':
                return 'SPACE'
            return None
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


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
        self.ClassesMenu          = Classes()
        self.Hacker               = HackerClass()
        self.Rimuru               = RimuruClass()
        self.SecurityAnalytic     = SecurityAnalyticClass()
        self.SecurityBypasser     = SecurityBypasserClass()
        self.HardwareSpecialist   = HardwareSpecialistClass()
        self.SocialEngineer       = SocialEngineerClass()
        self.Vocaloid             = HatsuneMikuClass()
        self.Lambda               = LambdaClass()
        self.ReverseEngineer      = ReverseEngineerClass()
        self.CorruptedHatsuneMiku = CorruptedHatsuneMikuClass()
        self.Player               = PlayerModule.Player()
        
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
       # print(f"[DEBUG COBALT] Your level is actually > : {self.Player.Level}")

        clear()

        self.ClassesMenu._Classes() 
        ClassPage = 1

        while True:
            while True:
                if self.Player.Class == self.CorruptedHatsuneMiku:
                    cText("▶  Digite sua classe >>", "red")
                else:
                    cText("▶  Digite sua classe >>", "green")
                
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
                    case "LAMBDA":
                        PlayerClass = self.Lambda
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
                        cText("⚠  ERRO 04: Classe não encontrada", "red")
                        continue

            cText("▶  Digite seu nome >>", "green")            
            self.Player.Name = input("")
            if self.Player.Name == "Return":
                print("Retornando para a seleção de classe...")
                clear()
                continue
            else:
                break

        self.Player.Class = PlayerClass
        self.Player.Integrity = self.Player.Class.Integrity
        self.Player.Defense = self.Player.Class.Defense
        self.Player.Regen = self.Player.Class.Regen

        if not hasattr(self.Player.Class, 'Items') or self.Player.Class.Items in (None, 'None'):
            self.Player.Class.Items = set()

        saved_progress = RouteManager().load_progress({})
        inventory_names = saved_progress.get('inventory', [])
        if inventory_names:
            for item_name in inventory_names:
                item = open_chest.__globals__['get_item_by_name'](item_name)
                if item is not None:
                    self.Player.Class.Items.add(item)
                    self.Player.Integrity += getattr(item, 'Integrity', 0)
                    self.Player.Defense += getattr(item, 'Defense', 0)
        
        clear()
        cText(f">> Welcome {self.Player.Name}!", "green")
        sleep(2)
        cText(f">> Your class is: {self.Player.Class.raceName}", "green")
        sleep(2)
        clear()

        route_choice = getattr(self, 'route_choice', 'BAD')
        mission_name = getattr(self, 'mission_name', None)
        current_enemy = Enemy.create_phase_enemy(route_choice, self.Player.Level, mission_name=mission_name)
        current_enemy.set_phase(max(1, (self.Player.Level // 2) + 1))
        current_enemy.MaxHealth += int(self.Player.Level * 15)
        current_enemy.Health = current_enemy.MaxHealth
        active_cooldowns = {}
   
        while True:
            actual_selection = 0 
            
            while True:

                attack_list = list(self.Player.Class.Attacks.keys())
                total_attacks = len(attack_list)
                
                while True:
                    clear()
                    enemy_life(current_enemy)

                    nome_classe = getattr(self.Player.Class, 'Name', "HACKER")
                    
                    display_battle_ui(
                        player_integrity=self.Player.Integrity, 
                        max_integrity=self.Player.Class.Integrity, 
                        player_defense=self.Player.Defense, 
                        available_attacks=attack_list, 
                        ui_color=self.Player.Class.ui_color,
                        player_name=self.Player.Name,
                        class_name=PlayerClass.raceName,
                        selected_index=actual_selection
                    )
                    
                    tecla = get_key()
                    
                    if tecla == 'DOWN':
                        actual_selection = (actual_selection + 2) % total_attacks
                    elif tecla == 'UP':
                        actual_selection = (actual_selection - 2) % total_attacks
                    elif tecla == 'RIGHT':
                        actual_selection = (actual_selection + 1) % total_attacks  
                    elif tecla == 'LEFT':
                        actual_selection = (actual_selection - 1) % total_attacks  
                    elif tecla in ('ENTER', 'SPACE'):
                        Attack = attack_list[actual_selection]
                        break

                clear()
                enemy_life(current_enemy)
                display_battle_ui(self.Player.Integrity, self.Player.Class.Integrity, self.Player.Defense, self.Player.Class.Attacks.keys(), self.Player.Class.ui_color, selected_index=actual_selection)
                cText(f"\n>> EXECUTANDO PROTOCOLO: {Attack.upper()}...", "green")
                sleep(1)

                if Attack == "Reverse" and getattr(self.Player.Class, 'Decompiled', False):
                    clear()
                    enemy_life(current_enemy)
                    display_battle_ui(self.Player.Integrity, self.Player.Class.Integrity, self.Player.Defense, self.Player.Class.Attacks.keys(), self.Player.Class.ui_color, selected_index=actual_selection)
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
                    enemy_life(current_enemy)
                    display_battle_ui(self.Player.Integrity, self.Player.Class.Integrity, self.Player.Defense, self.Player.Class.Attacks.keys(), self.Player.Class.ui_color, selected_index=actual_selection)
                    cText("⚠  ERRO 04: Exploit não encontrado", "red")
                    sleep(2) 
                    continue

                if Attack in active_cooldowns and active_cooldowns[Attack] > 0:
                    clear()
                    enemy_life(current_enemy)
                    display_battle_ui(self.Player.Integrity, self.Player.Class.Integrity, self.Player.Defense, self.Player.Class.Attacks.keys(), self.Player.Class.ui_color, selected_index=actual_selection)
                    cText(f"⚠  ACCESSO NEGADO: '{Attack}' está em cooldown! ({active_cooldowns[Attack]} turnos restantes)", "yellow")
                    sleep(2.5) 
                    continue
                
                raw_attack = self.Player.Class.Attacks[Attack]
                if isinstance(raw_attack, tuple):
                    base_damage, damage_per_level = raw_attack
                else:
                    base_damage = raw_attack
                    damage_per_level = 0

                base_damage = float(base_damage)
                class_power = getattr(self.Player.Class, 'attack_power', 0)
                level_multiplier = 1.0 + (self.Player.Level - 1) * 0.15
                Attack_Info = base_damage * level_multiplier
                Attack_Info += float(damage_per_level) * max(0, self.Player.Level - 1)
                Attack_Info += class_power * 0.15
                
                context = (self.Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, self.Player.Class)

                if Attack in self.attack_functions:
                    self.attack_functions[Attack](*context)

                if Attack == "Give Damage":
                    self.Player.Integrity -= Attack_Info

                if hasattr(current_enemy, "SkipTurn") and current_enemy.SkipTurn == True:
                    cText(">> Turno do inimigo skippado!", "yellow")
                    current_enemy.SkipTurn = False
                    sleep(2)
                    clear()
                    enemy_life(current_enemy)
                    display_battle_ui(self.Player.Integrity, self.Player.Class.Integrity, self.Player.Defense, self.Player.Class.Attacks.keys(), self.Player.Class.ui_color, selected_index=actual_selection)
                    continue
                else:
                    clear()
                    enemy_life(current_enemy)
                    display_battle_ui(self.Player.Integrity, self.Player.Class.Integrity, self.Player.Defense, self.Player.Class.Attacks.keys(), self.Player.Class.ui_color, selected_index=actual_selection)
                    final_damage = Damage(Attack_Info, current_enemy.Defense)
                    current_enemy.Health -= final_damage
                    cText(f" >> Você executou [{Attack}]! {current_enemy.Name} levou {final_damage:.1f} de dano!", "positive")

                if hasattr(self.Player.Class, 'Cooldowns') and Attack in self.Player.Class.Cooldowns:
                    active_cooldowns[Attack] = self.Player.Class.Cooldowns[Attack]

                if current_enemy.Health <= 0:
                    sleep(1.5)                                          
                    clear()
                    cText(f"\n   [>> NODE COMPROMETIDO <<]\n < -- {current_enemy.Name} hackeado! -- >\n", "green")
                    sleep(4)
                    clear()
                    
                    current_enemy.Health += current_enemy.MaxHealth * 0.5
                    import Game.Main.Player as PlayerStats
                    PlayerStats.record_task_completed()
                    
                    if not getattr(self.Player.Class, 'Items', None):
                        self.Player.Class.Items = set()

                    chest_opened = open_chest(self.Player)
                    if chest_opened:
                        PlayerStats.record_chest_opened()

                    saved_progress = RouteManager().load_progress({}, update_stats=False)
                    inventory_names = list(saved_progress.get('inventory', []))
                    if chest_opened and hasattr(chest_opened, 'itemName'):
                        inventory_names.append(chest_opened.itemName)
                    inventory_names = list(dict.fromkeys(inventory_names))
                    RouteManager().save_progress(
                        saved_progress.get('badges', {}),
                        saved_progress.get('route_history', []),
                        saved_progress.get('ending', 'ENDING_NORMAL'),
                        saved_progress.get('mission_history', []),
                        level=saved_progress.get('level', 1),
                        inventory=inventory_names,
                        tasks=PlayerStats.get_lifetime_tasks(),
                        chests=PlayerStats.get_lifetime_chests()
                    )

                    item_set = set(getattr(self.Player.Class, 'Items', []))
                    Integrity_boost = sum(getattr(item, 'Integrity', 0) for item in item_set)
                    Defense_boost = sum(getattr(item, 'Defense', 0) for item in item_set)
                    self.Player.Defense += Defense_boost
                    self.Player.Integrity += Integrity_boost
                    
                    clear()
                    #enemy_life(current_enemy)
                    # cText(f" ur level is {self.Player.Level}, how u managed to do that? (this message will change)", "warn")
                    cText(f"A versão do seu sistema (4) está atualmente desatualizada.", "error")
                    sleep(1.5)
                    cText(f"Gostaria de atualizar a versão do seu sistema para 5?", "green")
                    sleep(1)
                    input(f"\n  {Fore.LIGHTBLACK_EX}[ Pressione ENTER para continuar ]{Style.RESET_ALL}")
                    clear()

                    with Progress(
                        TextColumn("[bold green]COBALT OS"),
                        BarColumn(bar_width=40, complete_style="green", finished_style="bright_green"),
                        TextColumn("[green]{task.percentage:>3.0f}%"),
                        TimeRemainingColumn(),
                    ) as progress:
                        task = progress.add_task("Atualizando...", total=100)
                        while not progress.finished:
                            progress.advance(task, 1)
                            sleep(0.04)

                    sleep(1)
                    clear()
                    sleep(0.5)
                    cText(" Sistema atualizado com sucesso. Versão 5.0 instalada.", "positive")
                    sleep(1.5)
                    input(f"\n  {Fore.LIGHTBLACK_EX}[ Pressione ENTER para ver as novidades ]{Style.RESET_ALL}")
                                        
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
                cText(f"\n        [!]Erro 404[!] \n < -- Você foi hackeado -- >\n", "red")
                sleep(2)
                enemy_life(current_enemy)
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
            enemy_life(current_enemy)
            display_battle_ui(self.Player.Integrity, self.Player.Class.Integrity, self.Player.Defense, self.Player.Class.Attacks.keys(), self.Player.Class.ui_color)