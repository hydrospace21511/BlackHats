from colorama import Fore, Back, Style, init

class HackerClass:

    def __init__(self):
        self.raceName = "Hacker"
        self.tier = 1
        self.attack_power = 20
        self.Integrity = 80
        self.Defense = 10
        self.Regen = 0
        self.ui_color = Fore.GREEN        
        self.Items = "None"
        self.Attacks = {
            "SQL Injection": (48, 4),
            "Cross-Site Scripting": (42, 4),
            "Buffer Overflow": (60, 5),
            "Denial of Service": (69, 6),
            "Debug": (10000, 0)
        }
        self.active_cooldowns = {
            "SQL Injection": 1,
            "Cross-Site Scripting": 3, 
            "Buffer Overflow": 5,
            "Denial of Service": 6   
        }

    def RaceName(self):
        return self.raceName
    
    def MostraVida(self):
        return self.Integrity
    
    def Damage(self, D, Defense):
        return D * (1 - Defense / 100)
    
    def Firewall(self):
        return 1
    
    def MostraAtaques(self):
        return list(self.Attacks.keys())