from colorama import Fore
class ReverseEngineerClass:
    def __init__(self):
        self.raceName = "Reverse Engineer"
        self.Integrity = 500
        self.Defense = 45
        self.IntegrityBackup = self.Integrity
        self.DefenseBackup = self.Defense
        self.Regen = 0
        self.stun = 0
        self.ui_color = Fore.GREEN
        self.Decompiled = False
        
        self.Attacks = {
            "Decompiler": 60,
            "Protection Bypass": 100,
            "Algorithm Clone": 40,
            "ROP Chain": 80,
            "Punch": 50
        }

        self.OriginalAttacks = {
            "Decompiler": 60,
            "Protection Bypass": 100,
            "Algorithm Clone": 40,
            "ROP Chain": 80,
            "Punch": 50
        }

        self.Cooldowns = {
            "Decompiler": 3,
            "Protection Bypass": 5,
            "Algorithm Clone": 2,
            "ROP Chain": 3
        }
    