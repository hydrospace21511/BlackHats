from colorama import Fore, Back, Style, init
class HackerClass:
     
    def __init__(self):
        self.raceName = "Hacker"
        self.Integrity = 85
        self.Defense = 15
        self.Regen = 0
        self.Attacks = {
            "SQL Injection": 40,
            "Cross-Site Scripting": 30,
            "Buffer Overflow": 50,
            "Denial of Service": 60,
        #    "God's Wrath": Regen + 100000000,
        "Pneumoultramicroscopicsilicovolcanoconiotic": 'ball cancer'
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

    #calculadora de dano (com a defesa)(tenho medo da conta q faz)
    def Damage(self, D, Defense) :
       # print("Available attacks:", list(self.Attacks.keys()))
        return D * (1 - Defense / 100)

    def Firewall(self):
        return 1
    
    def MostraAtaques(self):
        return list(self.Attacks.keys())