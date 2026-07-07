from Game.ItemsLib.Items.Diskette                import Diskette3Class
from Game.ItemsLib.Items.CaboDeRede              import CaboDeRedeClass
from Game.ItemsLib.Items.ManualRoot              import ManualRootClass
from Game.ItemsLib.Items.DVD                     import DVDClass
from Game.ItemsLib.Items.Pager                   import PagerModificadoClass
from Game.ItemsLib.Items.DiarioCriptografado     import DiarioCriptografadoClass
from Game.ItemsLib.Items.RAMOverclocada          import RAMOverclocadaClass
from Game.ItemsLib.Items.Modem56k                import Modem56kClass
from Game.ItemsLib.Items.BadgeACSd               import BadgeACSDClass
from Game.ItemsLib.Items.FotoDesbotada           import FotoDesbotadaClass
from Game.ItemsLib.Items.VectraOverclockadoDaEti import VectraClass

from Game.Main.Color import cText
import os
import random
from time import sleep

items = [
    Diskette3Class(),
    CaboDeRedeClass(),
    ManualRootClass(),
    DVDClass(),
    PagerModificadoClass(),
    DiarioCriptografadoClass(),
    RAMOverclocadaClass(),
    Modem56kClass(),
    BadgeACSDClass(),
    FotoDesbotadaClass(),
    VectraClass()
]

chest_art = r'''
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
'''

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_item_by_name(item_name):
    for item in items:
        if item.itemName.lower() == str(item_name).lower():
            return item
    return None


def open_chest(Player):
    random_item = random.choice(items)

    while True:
        cText(chest_art, "green")
        cText("Você encontrou um baú!", "green")
        cText("Dentro há algo que pode mudar seus stats.", "green")
        cText("Gostaria de abri-lo? (S/N)", "green")

        Response = input(">> ").upper().strip()

        match Response:
            case "S" | "SIM":
                clear()
                sleep(1.5)
                cText(f"Você abre o baú e encontra:", "green")
                sleep(0.5)
                cText(f"  [ {random_item.tier.upper()} ]  {random_item.itemName}", "green")
                sleep(0.5)
                cText(f"  {random_item.lore}", "green")
                sleep(0.5)
                cText(f"  +{random_item.Integrity} Integrity  |  +{random_item.Defense} Defense", "green")

                current_items = set(getattr(Player.Class, 'Items', set()))
                current_items.add(random_item)
                Player.Class.Items = current_items

                if hasattr(Player, 'Class') and Player.Class is not None:
                    import Game.Main.DarkHatsGame as darkhats_game_module
                    darkhats_game_module.apply_item_buffs(Player, Player.Class)

                sleep(3)
                return random_item

            case "N" | "NÃO":
                clear()
                sleep(1.5)
                cText("Você decide deixar o baú e seguir em frente.", "green")
                return None

            case _:
                clear()
                cText(chest_art, "green")
                cText("Resposta inválida. Por favor, digite S ou N.", "red")
                sleep(1.5)
                clear()
                continue