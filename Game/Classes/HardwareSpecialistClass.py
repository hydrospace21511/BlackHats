from colorama import Fore, Back, Style, init

class HardwareSpecialistClass:

    def __init__(self):
        self.raceName = "Hardware Specialist"
        self.tier = 2
        self.attack_power = 26
        self.Integrity = 150
        self.Defense = 30
        self.Regen = 0
        self.ui_color = Fore.GREEN
        self.Items = "None"
        self.Attacks = {
            "Overclock":            (30, 3),
            "Hardware Exploit":     (36, 4),
            "Firmware Corruption":  (33, 3),
            "Power Surge":          (40, 4),
            "Punch":                (18, 2),
        }
        self.Cooldowns = {
            "Overclock":           2,
            "Hardware Exploit":    3,
            "Firmware Corruption": 3,
            "Power Surge":         4,
        }

    def Damage(self, D, Defense):
        return D * (1 - Defense / 100)