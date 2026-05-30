import os
import sys
import pygame
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from time import sleep
from Game.Classes.SecretClasses.Hatsune import HatsuneMikuClass
from Game.Classes.SecretClasses.CorruptedHatsune import CorruptedHatsuneMikuClass
CorruptedHatsuneMiku = CorruptedHatsuneMikuClass()
#NegativeSpaceT = CorruptedHatsuneMikuClass.trigger_negative_space
pygame.mixer.init()
import getpass
from colorama import Fore, Back, Style
def user():
    return getpass.getuser()
                                                                                                                                                                                                                                                    # ignora isso, é a maldade q quebra a quarta parede po


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
    if Player.Class.Decompiled == False:
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
            for i in range(100):
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
            cText("Why would you do that? R u dumb?", "red") # só pra testa a classe e os bagui
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
            attack_archive = os.path.dirname(os.path.abspath(__file__))
            root_archive = os.path.dirname(attack_archive)
            MMB_sound = os.path.join(root_archive, "Sounds", "miku-miku-beam.mp3")
            i = 0
            time = 0.06
            pygame.mixer.music.load(MMB_sound)
            pygame.mixer.music.play()
            PlayerClass.Defense = 0
            #sleep(990)
            while i < 100:
                clear()
                if i < 55:
                    cText(f"Now it's time for the moment you've been waiting for!", "red")
                elif i < 71:
                    cText(f"One!", "red") # tentei usar case mas fiquei com preguiça, ent vai ficar assim mesmo (pq vc ta lendo isso, thalles?)
                elif i <= 84:
                    cText(f"Two!", "yellow")
                elif i <= 100:
                    cText(f"Three!", "green")
                sleep(time)
                i += 1
            if i >= 100:
                clear()
                cText(" Ready? Miku Miku Beam!", "positive")
                sleep(1.38)
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
            print("U just got ball cancer, gng how u managed to do that is beyond me ngl")
            sleep(3)
            final_damage = Damage(100000000, Player.Class.Defense)
            Player.Integrity -= final_damage
            clear()
            print(f"Integrity: {integrity_bar(Player.Integrity, Player.Class.Integrity)}")
            sleep(3)
            clear()

def ProtectionBypassAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
                #display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
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

def WorldIsMineAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
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
                                TempVocaloid = HatsuneMikuClass()
                                def corrupt(text):
                                    chars = ["#", "@", "%", "&", "█", "/", "▓"]

                                    return "".join(
                                        random.choice(chars) if random.random() < 0.20 else c
                                        for c in text
                                    )
                                
                                for _ in range(400):
                                 msg = random.choice(list(TempVocaloid.Texts))

                                 if random.random() < 0.35:
                                        msg = corrupt(msg)

                                        spaces = " " * random.randint(0, 65)
                                        breaks = "\n" * random.randint(0, 6)
                                        color = random.choice(list(TempVocaloid.Colors))
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

def SystemOverrideAttack(Player, current_enemy, Attack_Info, display_battle_ui, integrity_bar, defense_bar, Damage, Attack, PlayerClass):
    current_enemy.SkipTurn = True
    clear()
    final_damage = Damage(Attack_Info, current_enemy.Defense)
    current_enemy.Health -= final_damage

    cText(" System overridden! Enemy systems frozen!", "positive")
    sleep(2)
    clear()