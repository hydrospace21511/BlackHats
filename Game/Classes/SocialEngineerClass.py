from colorama import Fore
class SocialEngineerClass:
    def __init__(self):
        self.raceName = "Social Engineer"
        self.tier = 6
        self.attack_power = 22
        self.Integrity = 50
        self.Defense = 45
        self.Regen = 0
        self.stun = 0
        self.ui_color = Fore.GREEN
        self.Attacks = {
            "Internal Access": (18, 2),
            "Phishing": (24, 3),
            "Pretexting": (30, 4),
            "Baiting": (20, 2),
            "Punch": (22, 1),
            "God's Hand": (35, 5),
        #   "God's Wrath": [Regen + 100000000, 1]
        }

        self.Cooldowns = {
            "Internal Access": 1,
            "Phishing": 3, 
            "Pretexting": 5,
            "Baiting": 1   
        }
    
    def RaceName(self):
        return self.raceName
    
    def MostraAtaques(self):
        return list(self.Attacks.keys())
    
    def Damage(self, D, Defense) :
        # print("Available attacks:", list(self.Attacks.keys()))
        return D * (1 - Defense / 100)
    