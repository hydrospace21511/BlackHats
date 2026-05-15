from Player import Player
from Player import integrity_bar
Player = Player()

class Enemy:
    def __init__(self, name, health, defense, regen):
        self.NPCname = name
        self.NPChealth = health
        self.NPCDefense = defense
        self.NPCRegen = regen
        self.NPCAttacks = {
            "Stab": 30,
            "Virtual Strike": 50,
            "Cyber Blast": 60,
            "Protocol Overload": 70,
            "System Crash": 80
        }
            
    def give_damage(self, damage):
        final_damage = damage * (1 - Player.Integrity / 100)
        Player.Integrity -= final_damage
        print(f"{Player.Name} took {final_damage:.1f} damage. Integrity: {integrity_bar(Player.Integrity)}")
