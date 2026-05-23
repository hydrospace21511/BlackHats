from colorama import Fore, Style

def display_battle_ui(player_integrity, max_integrity, player_defense, available_attacks, ui_color):

    C_BORDER = ui_color
    #gosto da strategia ne? E PQ VC TA LENDO ISSO TUDO? EU N SOU ESQUIZOFRENICO DE ESCREVER MAS PQ VC TA LENDO?
    C_CORRUPTED = Fore.RED  #setei pra hatsune corrompida, mas posso usar pra outras classes futuramente
    C_ALERT  = ui_color  
    C_TEXT   = Fore.WHITE                
    C_DATA   = Fore.CYAN                  
    RESET    = Style.RESET_ALL

    l1_spaces = " " * 33 #l1 = linha 1 (ta centralizando titulo)
    title = f"{C_ALERT}COBALT MAINFRAME v1.0.4{RESET}{l1_spaces}{Style.DIM}SYSTEM NODE OVERVIEW{RESET}"


    # vida
    hp_percent = max(0, min(1, player_integrity / max_integrity))
    hp_full = int(hp_percent * 15)
    hp_empty = 15 - hp_full
    hp_bar_str = Fore.GREEN + '|' * hp_full + Fore.RED + '·' * hp_empty + RESET
    
    #porcentagem da defesa 
    def_visual = 100 if player_defense == 99 else player_defense
    def_percent = max(0, min(1, def_visual / 100))
    def_full = int(def_percent * 15)
    def_empty = 15 - def_full
    def_bar_str = Fore.CYAN + '|' * def_full + Fore.BLUE + '·' * def_empty + RESET

    #seta na ui
    hp_part = f"{C_TEXT}INTEGRITY:{RESET} [{hp_bar_str}] {C_DATA}{hp_percent*100:>3.0f}%{RESET}"
    def_part = f"{C_TEXT} DEFENSE:{RESET} [{def_bar_str}] {C_DATA}{player_defense:>3.0f}%{RESET}"
    line_status = f"{hp_part}     {C_BORDER}│{RESET}     {def_part}"

    attacks = ", ".join(available_attacks)
    prefix = "ACTIVE EXPLOITS: " # 17 caracteres
    
    attack_lines = []
    first_line_limit = 59
    
    if len(attacks) <= first_line_limit:

        pattacks = attacks.ljust(59)
        full_line = f"{Style.DIM}{prefix}{RESET}{C_DATA}{pattacks}{RESET}"
        attack_lines.append(full_line)

    else:
        part1 = attacks[:first_line_limit]
        full_line1 = f"{Style.DIM}{prefix}{RESET}{C_DATA}{part1}{RESET}"
        attack_lines.append(full_line1)
        text = attacks[first_line_limit:]
        
        while len(text) > 0:
            part_next = text[:76]
            text = text[76:]
            part_next1 = part_next.ljust(76)
            full_line_next = f"{C_DATA}{part_next1}{RESET}"
            attack_lines.append(full_line_next)

    l4_spaces = " " * 51
    line_prompt = f"{C_ALERT}>> INITIALIZE PROTOCOL...{RESET}{l4_spaces}" #ultima parte da ui (vou trocar pra outras versoes de classes)
    #printa ui + seta as cor das borda

    print(C_BORDER + "╔" + "═" * 78 + "╗" + RESET)
    print(f"{C_BORDER}║ {RESET}{title}{C_BORDER} ║{RESET}")
    print(C_BORDER + "╠" + "═" * 78 + "╣" + RESET)
    print(f"{C_BORDER}║ {RESET}{line_status}{C_BORDER} ║{RESET}")
    print(C_BORDER + "╠" + "═" * 78 + "╣" + RESET)
    
    for attack_line in attack_lines:
        print(f"{C_BORDER}║ {RESET}{attack_line}{C_BORDER} ║{RESET}")
        
    print(C_BORDER + "╠" + "═" * 78 + "╣" + RESET)
    print(f"{C_BORDER}║ {RESET}{line_prompt}{C_BORDER} ║{RESET}")
    print(C_BORDER + "╚" + "═" * 78 + "╝" + RESET)