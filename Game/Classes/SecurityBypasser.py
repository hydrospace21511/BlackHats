from colorama import Fore, Back, Style, init
class SecurityBypasserClass:
     
    def __init__(self):
        self.raceName = "Security Bypasser"
        self.tier = 1
        self.attack_power = 24
        self.Integrity = 200
        self.Defense = -10
        self.Regen = 0
        self.ui_color = Fore.GREEN        
        self.Attacks = {
            "Firewall Bypass": (18, 4),
            "System Override": (22, 5),
            "Backdoor Implant": (20, 6),
            "Stealth Access": (28, 5),
            "Punch": (16, 3)
        }
        self.active_cooldowns = {
            "Firewall Bypass": 3,
            "System Override": 3,
            "Backdoor Implant": 3,
            "Stealth Access": 3
        }
