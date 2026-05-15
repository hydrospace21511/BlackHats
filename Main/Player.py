from colorama import Fore, Style

def integrity_bar(current_integrity, max_integrity):
    percent = max(0, min(1, current_integrity / max_integrity))
    
    num_full = int(percent * 15)
    num_empty = 15 - num_full
    
    bar = Fore.GREEN + '|' * num_full + Fore.RED + '·' * num_empty + Style.RESET_ALL
    return f"[{bar}] {percent*100:.0f}%"

def defense_bar(current_defense):
    max_defense = 99
    percent = max(0, min(0.99, current_defense / max_defense)) # Trava em 0.99
    
    num_full = int(percent * 15)
    num_empty = 15 - num_full
    
    bar = Fore.BLUE + '|' * num_full + Fore.WHITE + '·' * num_empty + Style.RESET_ALL
    return f"[{bar}] {percent*100:.0f}%"

class Player :
    def __init__(self):
        self.Name = ""
        self.Class = None
        self.Level = 1
        self.Integrity = 0
        self.Defense = 0
        self.Regen = 0


    def Name(self) :
        return self.Name
      
    def Class (self):
        return self.Class
    
    def Level (self):
        return self.Level
    
