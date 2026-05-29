from colorama import Fore, Style

def integrity_bar(current_integrity, max_integrity):
    percent = max(0, min(1, current_integrity / max_integrity))
    
    num_full = int(percent * 15)
    num_empty = 15 - num_full
    
    bar = Fore.GREEN + '|' * num_full + Fore.RED + '·' * num_empty + Style.RESET_ALL
    return f"[{bar}] {percent*100:.0f}%"

def defense_bar(current_defense):
    max_val = 100
    visual_defense = 100 if current_defense == 99 else current_defense
    percent = max(0, min(1, visual_defense / max_val))
    
    num_full = int(percent * 15)
    num_empty = 15 - num_full
    
    bar1 = Fore.CYAN + '|' * num_full + Fore.BLUE + '·' * num_empty + Style.RESET_ALL
    return f"[{bar1}] {percent*100:.0f}%"

class Player :
    def __init__(self):
        self.Name = ""
        self.Class = ""
        self.Level = 1
        self.Integrity = 0
        self.Defense = 0
        self.Regen = 0
        self.ui_color = Fore.GREEN


    # def Name(self) :
    #     return self.Name
      
    # def Class (self):
    #     return self.Class
    
    # def Level (self):
    #     return self.Level
    
