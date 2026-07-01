from colorama import Fore
class SecurityAnalyticClass:

    def __init__(self):
        self.raceName = "Security Analytic"
        self.tier = 3
        self.attack_power = 30
        self.Integrity = 200
        self.Defense = 20
        self.Regen = 0
        self.ui_color = Fore.GREEN
        self.Attacks = {
            "Firewall": (30, 3),
            "Security Patch": (28, 3),
            "Weakness View": (26, 4),
            "Punch": (32, 2),
            "God's Hand": (45, 5),
            "Pneumoultramicroscopicsilicovolcanoconiotic": 'ball cancer'
        }

        self.Cooldowns = {
            "Firewall": 8,
            "Security Patch": 3,
            "Weakness View": 3,
            "God's Hand": 999999
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

class SecurityAnalytic(SecurityAnalyticClass):
    """Compatibility wrapper for the battle-balance tests and runtime usage."""
    pass