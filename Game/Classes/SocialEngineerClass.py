from colorama import Fore

class SocialEngineerClass:

    def __init__(self):
        self.raceName = "Social Engineer"
        self.tier = 5
        self.attack_power = 38
        self.Integrity = 300
        self.Defense = 40
        self.Regen = 5
        self.stun = 0
        self.ui_color = Fore.GREEN
        self.Items = "None"
        self.Attacks = {
            "Internal Access": (4, 2),
            "Phishing":        (24, 3),
            "Pretexting":      (30, 4),
            "Baiting":         (4, 2),
            "Hack":           (22, 1),
        #    "God's Hand":      (50, 5),
        }
        self.Cooldowns = {
            "Internal Access": 1,
            "Phishing":        3,
            "Pretexting":      5,
            "Baiting":         1,
        }

    def RaceName(self):
        return self.raceName

    def MostraAtaques(self):
        return list(self.Attacks.keys())

    def Damage(self, D, Defense):
        return D * (1 - Defense / 100)