from colorama import Fore, Back, Style, init
class HardwareSpecialistClass:
     
    def __init__(self):
        self.raceName = "Hardware Specialist"
        self.Integrity = 200
        self.Defense = 40
        self.Regen = 0
        self.ui_color = Fore.GREEN        
        self.Attacks = {
            "Overclock": 50,
            "Hardware Exploit": 70,
            "Firmware Corruption": 60,
            "Power Surge": 80,
            "Punch": 50

        }
        self.active_cooldowns = {
            "Overclock": 2,
            "Hardware Exploit": 3,
            "Firmware Corruption": 3,
            "Power Surge": 4            
        }
