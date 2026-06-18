from colorama import Fore, Back, Style, init
class LambdaClass:
     
    def __init__(self):
        self.raceName = "Lambda"
        self.Integrity = 450
        self.Defense = 40
        self.Regen = 0
        self.ui_color = Fore.YELLOW        
        self.Attacks = {
            "Delta Slash":(200, 50),
            "Atom Partition": (300, 100),
            "Mega Blast": (100, 100),
        }
        self.active_cooldowns = {
            "Delta Slash": 3,
            "Atom Partition": 4,
            "Mega Blast": 3
        }
        self.AttackPower=50
