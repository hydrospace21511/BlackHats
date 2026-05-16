from Player import integrity_bar, defense_bar

def display_battle_ui(player_integrity, max_integrity, player_defense, available_attacks):
    """Display the battle UI in a bordered box"""
    integrity_display = integrity_bar(player_integrity, max_integrity)
    defense_display = defense_bar(player_defense)
    
    border_top = "╔" + "═" * 75 + "╗"
    border_bottom = "╚" + "═" * 75 + "╝"
    border_side = "║"
    
    print(border_top)
    print(f"{border_side} {'BATTLE STATUS':^73} {border_side}")
    print(f"{border_side} {'-' * 73} {border_side}")
    print(f"{border_side} Life:     {integrity_display:<65} {border_side}")
    print(f"{border_side} Defense:  {defense_display:<65} {border_side}")
    print(f"{border_side} {'-' * 73} {border_side}")
    print(f"{border_side} {'AVAILABLE ATTACKS:':^73} {border_side}")
    
    # Wrap attacks list if too long
    attack_lines = []
    current_line = ""
    for attack in available_attacks:
        if len(current_line) + len(attack) + 2 > 71:
            attack_lines.append(current_line)
            current_line = attack
        else:
            if current_line:
                current_line += ", " + attack
            else:
                current_line = attack
    if current_line:
        attack_lines.append(current_line)
    
    for line in attack_lines:
        print(f"{border_side} {line:<73} {border_side}")
    
    print(f"{border_side} {'-' * 73} {border_side}")
    print(f"{border_side} {'CHOOSE YOUR ATTACK':<73} {border_side}")
    print(border_bottom)
