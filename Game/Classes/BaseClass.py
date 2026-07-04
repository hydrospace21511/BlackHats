from colorama import Fore, Back, Style, init
class BaseClass:
     
    def __init__(self):
        self.raceName = ""
        self.Integrity = 85
        self.Defense = 15
        self.Regen = 0
        self.ui_color = Fore.GREEN        
        self.Attacks = {
        }
        self.active_cooldowns = {
        }
