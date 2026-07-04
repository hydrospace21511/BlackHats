    
    # match Attack:

    #     case "Decompiler":
    #         DecompilerAttack(*context)

    #     case "Algorithm Clone":
    #         AlgorithmCloneAttack(*context)
        
    #     case "Protection Bypass":
    #         ProtectionBypassAttack(*context)

    #     case "Internal Access":
    #         InternalAccessAttack(*context)

    #     case "Miku Miku Beam" | "MMB":
    #         MikuMikuBeamAttack(*context)

    #     case "Tell Your World":
    #         TellYourWorldAttack(*context)


    #     case "World Is Mine":
    #         WorldIsMineAttack(*context)


    #     case "Baiting":
    #         BaitingAttack(*context)

    #     case "Firewall":
    #         FirewallAttack(*context)

    #     case "Security Patch":
    #         SecurityPatchAttack(*context)

    #     case "Pneumoultramicroscopicsilicovolcanoconiotic":
    #         PneumoultramicroscopicsilicovolcanoconioticAttack(*context)

    #     case "Desintegration":
    #         DesintegrationAttack(*context)
        
    #     case "Give Damage":
    #         GiveDamageAttack(*context)

    #     case "Negative Space":
    #         NegativeSpaceAttack(*context)
        
    #     case _:
    #         display_battle_ui(Player.Integrity, Player.Class.Integrity, Player.Defense, Player.Class.Attacks.keys(), Player.Class.ui_color)
    #         final_damage = Damage(Attack_Info, current_enemy.Defense)
    #         current_enemy.Health -= final_damage
    #         clear()
    #         cText(f" >> You executed {Attack}! {current_enemy.Name} took {final_damage:.1f} damage!", "positive")