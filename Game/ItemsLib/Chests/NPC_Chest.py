from Game.ItemsLib.Items.TestItem import TestItemClass
from Game.ItemsLib.Items.TestItem2 import TestItem2Class
from Game.Main.Color import cText
import os
from time import sleep
TestItem = TestItemClass()
TestItem2 = TestItem2Class()
items = {TestItem, TestItem2}
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
import random


def open_chest(Player):
    random_item = random.choice(list(items))   
    while True:
        cText(r'''
                            ___.=""_;=.
                            ,-"_,=""     `"=._                  
                            "=._o`"-._        `"=._
                            `"=._o`"=._      _`"=._                     
                                    :=._o "=._."_.-="'"=._
                            __.--" , ; `"=._o." ,-"""-._ ".   
                        ._"  ,. .` ` `` ,  `"-._"-._   ". '
                        |o`"=._` , "` `; .". ,  "-._"-._; ;              
                        | ;`-.o`"=._; ." ` '`."\` . "-._ /
                        |o;    `"-.o`"=._``  '` " ,__.--o;  
                        | ;     (#) `-.o `"=.`_.--"_o.-; ;
                        |o;._    "      `".o|o_.--"    ;o;
                        "=._o--._        ; | ;        ; ;
                                "=._o--._   ;o|o;     _._;o;
                                    "=._o._; | ;_.--"o.--"
                                        "=.o|o_.--"
        ''', "green")
        cText("You found a chest! Inside, you find some items that buff or nerf your stats.", "green")
        cText("Would you like to open it?", "green")
        cText("Y/N", "green")
        Response = input(">> ").upper().strip()
        match Response:
            case "Y" | "YES":
                clear()
                sleep(2)
                cText(f"You open the chest and find the following item: {random_item.itemName}", "green")
                Player.Class.Items.add(random_item)
                sleep(3)
                return items
                
            case "N" | "NO":
                clear()
                sleep(2)
                cText("You decide to leave the chest alone and continue on your journey.", "green")
                return None
                
            case _:
                clear()                
                cText("Invalid response. Please enter Y or N.", "red")
                continue
