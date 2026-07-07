from colorama import Fore

class ReverseEngineerClass:

    def __init__(self):
        self.raceName = "Reverse Engineer"
        self.tier = 4
        self.attack_power = 34
        self.Integrity = 250
        self.Defense = 35
        self.IntegrityBackup = self.Integrity
        self.DefenseBackup = self.Defense
        self.Regen = 0
        self.stun = 0
        self.ui_color = Fore.GREEN
        self.Decompiled = False
        self.Items = "None"

        self.Attacks = {
            "Decompiler":        (42, 4),
            "Protection Bypass": (50, 5),
            "Algorithm Clone":   (36, 4),
            "ROP Chain":         (44, 5),
            "Hack":             (30, 3),
        }

        self.OriginalAttacks = {
            "Decompiler":        (42, 5),
            "Protection Bypass": (50, 5),
            "Algorithm Clone":   (36, 4),
            "ROP Chain":         (44, 5),
            "Hack":             (30, 3),
        }

        self.Cooldowns = {
            "Decompiler":        3,
            "Protection Bypass": 5,
            "Algorithm Clone":   2,
            "ROP Chain":         3,
        }