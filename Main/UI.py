from colorama import Fore, Style

def display_battle_ui(player_integrity, max_integrity, player_defense, available_attacks):
    
    C_BORDER = Fore.GREEN        
    C_ALERT  = Fore.GREEN + Style.BRIGHT   
    C_TEXT   = Fore.WHITE                
    C_DATA   = Fore.CYAN                  
    RESET    = Style.RESET_ALL

    l1_spaces = " " * 33
    line_title = f"{C_ALERT}COBALT MAINFRAME v1.0.4{RESET}{l1_spaces}{Style.DIM}SYSTEM NODE OVERVIEW{RESET}"

    hp_percent = max(0, min(1, player_integrity / max_integrity))
    hp_full = int(hp_percent * 15)
    hp_empty = 15 - hp_full
    hp_bar_str = Fore.GREEN + '|' * hp_full + Fore.RED + '·' * hp_empty + RESET
    
    def_visual = 100 if player_defense == 99 else player_defense
    def_percent = max(0, min(1, def_visual / 100))
    def_full = int(def_percent * 15)
    def_empty = 15 - def_full
    def_bar_str = Fore.CYAN + '|' * def_full + Fore.BLUE + '·' * def_empty + RESET

    hp_part = f"{C_TEXT}INTEGRITY:{RESET} [{hp_bar_str}] {C_DATA}{hp_percent*100:>3.0f}%{RESET}"
    def_part = f"{C_TEXT} DEFENSE:{RESET} [{def_bar_str}] {C_DATA}{player_defense:>3.0f}%{RESET}"
    line_status = f"{hp_part}     {C_BORDER}│{RESET}     {def_part}"

    all_attacks = ", ".join(available_attacks)
    prefix = "ACTIVE EXPLOITS: " # 17 caracteres
    
    formatted_attack_lines = []
    first_line_limit = 59
    
    if len(all_attacks) <= first_line_limit:

        padded_attacks = all_attacks.ljust(59)
        full_line = f"{Style.DIM}{prefix}{RESET}{C_DATA}{padded_attacks}{RESET}"
        formatted_attack_lines.append(full_line)

    else:
        part1 = all_attacks[:first_line_limit]
        full_line1 = f"{Style.DIM}{prefix}{RESET}{C_DATA}{part1}{RESET}"
        formatted_attack_lines.append(full_line1)
        remaining_text = all_attacks[first_line_limit:]
        
        while len(remaining_text) > 0:
            part_next = remaining_text[:76]
            remaining_text = remaining_text[76:]
            part_next_padded = part_next.ljust(76)
            full_line_next = f"{C_DATA}{part_next_padded}{RESET}"
            formatted_attack_lines.append(full_line_next)

    l4_spaces = " " * 51
    line_prompt = f"{C_ALERT}>> INITIALIZE PROTOCOL...{RESET}{l4_spaces}"

    print(C_BORDER + "╔" + "═" * 78 + "╗" + RESET)
    print(f"{C_BORDER}║ {RESET}{line_title}{C_BORDER} ║{RESET}")
    print(C_BORDER + "╠" + "═" * 78 + "╣" + RESET)
    print(f"{C_BORDER}║ {RESET}{line_status}{C_BORDER} ║{RESET}")
    print(C_BORDER + "╠" + "═" * 78 + "╣" + RESET)
    
    for attack_line in formatted_attack_lines:
        print(f"{C_BORDER}║ {RESET}{attack_line}{C_BORDER} ║{RESET}")
        
    print(C_BORDER + "╠" + "═" * 78 + "╣" + RESET)
    print(f"{C_BORDER}║ {RESET}{line_prompt}{C_BORDER} ║{RESET}")
    print(C_BORDER + "╚" + "═" * 78 + "╝" + RESET)