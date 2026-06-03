from colorama import Fore, Back, Style, init
class SecurityBypasserClass:
     
    def __init__(self):
        self.raceName = "Security Bypasser"
        self.Integrity = 200
        self.Defense = -10
        self.Regen = 0
        self.ui_color = Fore.GREEN        
        self.Attacks = {
            "Firewall Bypass": (20, 20),
            "System Override": (15, 10),
            "Backdoor Implant": ("regen", 10),
            "Stealth Access": (30, 30),
            "Punch": 40      
        }
        self.active_cooldowns = {
            "Firewall Bypass": 3,
            "System Override": 3,
            "Backdoor Implant": 3,
            "Stealth Access": 3
        }
