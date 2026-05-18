from colorama import Fore, Style

def display_battle_ui(player_integrity, max_integrity, player_defense, available_attacks):
    """Displays a wide, low-profile hacker HUD to save vertical space"""
    
    C_BORDER = Fore.GREEN        # Verde CRT fosco para as bordas
    C_ALERT  = Fore.GREEN    # Verde brilhante para comandos
    C_TEXT   = Fore.WHITE                    # Texto
    C_DATA   = Fore.CYAN                     # Dados/Valores
    RESET    = Style.RESET_ALL

    hp_percent = max(0, min(1, player_integrity / max_integrity))
    hp_full = int(hp_percent * 15)
    hp_empty = 15 - hp_full
    hp_bar_str = Fore.GREEN + '|' * hp_full + Fore.RED + '·' * hp_empty + RESET
    hp_part = f"{C_TEXT}INTEGRITY:{RESET} [{hp_bar_str}] {C_DATA}{hp_percent*100:>3.0f}%{RESET}"

    def_visual = 100 if player_defense == 99 else player_defense
    def_percent = max(0, min(1, def_visual / 100))
    def_full = int(def_percent * 15)
    def_empty = 15 - def_full
    def_bar_str = Fore.CYAN + '|' * def_full + Fore.BLUE + '·' * def_empty + RESET
    def_part = f"{C_TEXT}FIREWALL:{RESET} [{def_bar_str}] {C_DATA}{player_defense:>3.0f}%{RESET}"

    status_line = f"{hp_part}   {C_BORDER}│{RESET}   {def_part}"

    all_attacks = ", ".join(available_attacks)

    print(C_BORDER + "╔" + "═" * 78 + "╗" + RESET)

    print(f"{C_BORDER}║ {C_ALERT}COBALT MAINFRAME v1.0.4{RESET} {'':<22} {Style.DIM}SYSTEM NODE OVERVIEW{RESET} {C_BORDER}║")
    print(C_BORDER + "╠" + "═" * 78 + "╣" + RESET)

    print(f"{C_BORDER}║ {status_line:<106} {C_BORDER}║")
    print(C_BORDER + "╠" + "═" * 78 + "╣" + RESET)

    print(f"{C_BORDER}║ {Style.DIM}ACTIVE EXPLOITS:{RESET} {C_DATA}{all_attacks:<60}{RESET} {C_BORDER}║")
    print(C_BORDER + "╠" + "═" * 78 + "╣" + RESET)

    print(f"{C_BORDER}║ {C_ALERT}>> INITIALIZE PROTOCOL...{'':<51}{RESET} {C_BORDER}║")
    
    print(C_BORDER + "╚" + "═" * 78 + "╝" + RESET)