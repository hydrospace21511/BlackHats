import os
from time import sleep
from Classes.SecretClasses.Hatsune import HatsuneMikuClass
from Classes.SecretClasses.CorruptedHatsune import CorruptedHatsuneMikuClass
CorruptedHatsuneMiku = CorruptedHatsuneMikuClass()
import getpass
def user():
    return getpass.getuser()                                                                                                                                                                                                                                                    # ignora isso, é a maldade q quebra a quarta parede po

from colorama import init
import random
init(autoreset=True)
from Color import cText
from UI import display_battle_ui
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
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