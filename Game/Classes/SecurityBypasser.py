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
        self.Items = "None"
        self.Attacks = {
            "Firewall Bypass":  (32, 4),
            "System Override":  (38, 5),
            "Backdoor Implant": (35, 5),
            "Stealth Access":   (44, 6),
            "Hack":            (22, 2),
        }
        self.Cooldowns = {
            "Firewall Bypass":  2,
            "System Override":  3,
            "Backdoor Implant": 2,
            "Stealth Access":   4,
        }