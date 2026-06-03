from Game.Main.Player import Player
import random
from Game.Main.Player import integrity_bar
Player = Player()
from Game.Main.Color import cText

class Enemy:
    def __init__(self, name, max_health, defense, regen, attacks):
        self.Name = name
        self.MaxHealth = max_health
        self.Health = max_health
        self.Defense = defense
        self.Regen = regen
        self.Attacks = attacks

    def random_attack(self):
        attack_name = random.choice(list(self.Attacks.keys()))
        attack_damage = self.Attacks[attack_name]
        return attack_name, attack_damage
    
    def enemy_life(self,current_enemy):
        cText(f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║ {cText("COBALT VIRUS v1.0.2", "red")}                                      {cText("VIRUS MODE OVERVIEW", "red")} ║
╠═══════════════════════════════════════╦══════════════════════════════════════╣
║ ANOMALY NAME: {print(current_enemy.Name)}                         ║      INTEGRITY: {integrity_bar(current_enemy.Health, current_enemy.MaxHealth)}                      ║
╚═══════════════════════════════════════╩══════════════════════════════════════╝
              
              """
              )