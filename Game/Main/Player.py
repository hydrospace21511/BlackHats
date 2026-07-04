from colorama import Fore, Style

_LIFETIME_TASKS = 0
_LIFETIME_CHESTS = 0
_LIFETIME_REBIRTHS = 0

def reset_lifetime_stats():
    global _LIFETIME_TASKS, _LIFETIME_CHESTS, _LIFETIME_REBIRTHS
    _LIFETIME_TASKS = 0                 #vai tomando, 20 anos de experiencia com mysql pra fazer isso, ta? e pq vc ta lendo meus codigo dnv? eu sou o unico q fala aqui, tamo safe
    _LIFETIME_CHESTS = 0
    _LIFETIME_REBIRTHS = 0


def record_task_completed(amount=1):
    global _LIFETIME_TASKS
    _LIFETIME_TASKS += amount


def record_chest_opened(amount=1):
    global _LIFETIME_CHESTS
    _LIFETIME_CHESTS += amount

def record_rebirthed(amount=1):
    global _LIFETIME_REBIRTHS
    _LIFETIME_REBIRTHS += amount

def get_lifetime_tasks():
    return _LIFETIME_TASKS


def get_lifetime_chests():
    return _LIFETIME_CHESTS


def get_lifetime_stats():
    return {
        "tasks": _LIFETIME_TASKS,
        "chests": _LIFETIME_CHESTS,
        "rebirths": _LIFETIME_REBIRTHS #affs veyr, tudo eu 
    }


def set_lifetime_stats(tasks=0, chests=0, rebirths=0):
    global _LIFETIME_TASKS, _LIFETIME_CHESTS, _LIFETIME_REBIRTHS
    _LIFETIME_TASKS = int(tasks)
    _LIFETIME_CHESTS = int(chests)
    _LIFETIME_REBIRTHS = int(rebirths)

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

class Player:
    def __init__(self, name=""):
        self.Name = name
        self.Class = ""
        self.Level = 0
        self.Integrity = 0
        self.Defense = 0
        self.Regen = 0
        self.ui_color = Fore.GREEN

    def scale_damage(self, base_damage):
        level_bonus = max(0, self.Level - 1) * 0.15
        return float(base_damage) * (1 + level_bonus)


    # def Name(self) :
    #     return self.Name
      
    # def Class (self):
    #     return self.Class
    
    # def Level (self):
    #     return self.Level
    
