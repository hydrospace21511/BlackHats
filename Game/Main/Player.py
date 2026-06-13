from colorama import Fore, Style

_LIFETIME_TASKS = 0
_LIFETIME_CHESTS = 0


def reset_lifetime_stats():
    global _LIFETIME_TASKS, _LIFETIME_CHESTS
    _LIFETIME_TASKS = 0                 #por alguma razão tava dando erro quando colocado minusculo, as vezes era o vscodi resenhudo, mas agora ta funfando pelo menos (me lembrou da saga do DBeaver(MySql))
    _LIFETIME_CHESTS = 0


def record_task_completed(amount=1):
    global _LIFETIME_TASKS
    _LIFETIME_TASKS += amount


def record_chest_opened(amount=1):
    global _LIFETIME_CHESTS
    _LIFETIME_CHESTS += amount


def get_lifetime_tasks():
    return _LIFETIME_TASKS


def get_lifetime_chests():
    return _LIFETIME_CHESTS


def get_lifetime_stats():
    return {
        "tasks": _LIFETIME_TASKS,
        "chests": _LIFETIME_CHESTS,
    }

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
        self.Level = 1 #1
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
    
