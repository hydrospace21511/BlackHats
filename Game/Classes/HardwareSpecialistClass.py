from colorama import Fore, Back, Style, init
class HardwareSpecialistClass:
     
    def __init__(self):
        self.raceName = "Hardware Specialist"
        self.tier = 5
        self.attack_power = 26
        self.Integrity = 200
        self.Defense = 40
        self.Regen = 0
        self.ui_color = Fore.GREEN        
        self.Attacks = {
            "Overclock": (30, 3),
            "Hardware Exploit": (36, 4),
            "Firmware Corruption": (33, 3),
            "Power Surge": (40, 4),
            "Punch": (26, 2)

        }
        self.active_cooldowns = {
            "Overclock": 2,
            "Hardware Exploit": 3,
            "Firmware Corruption": 3,
            "Power Surge": 4            
        }
