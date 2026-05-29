from Game.Main.Player import Player
import random
from Game.Main.Player import integrity_bar
Player = Player()

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