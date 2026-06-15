import unittest

from Game.Main.Enemy import Enemy
from Game.Main.Player import Player
from Game.Classes.SecurityAnalyticClass import SecurityAnalytic


class BattleBalanceTests(unittest.TestCase):
    def test_route_phase_enemy_uses_level_specific_stats(self):
        enemy = Enemy.create_phase_enemy('TRUE', 5)

        self.assertEqual(enemy.Name, 'Dept_of_Vital_Stats')
        self.assertGreater(enemy.Health, 300)
        self.assertGreater(len(enemy.Attacks), 2)

    def test_enemy_phase_scaling(self):
        enemy = Enemy('Test', 100, 10, 2)
        enemy.set_phase(1)
        self.assertGreater(enemy.max_hp, 0)

    def test_player_level_scales_damage(self):
        player = Player('Tester')
        player.Level = 5
        player.Integrity = 100
        player.Defense = 10
        base = SecurityAnalytic().attack_power
        scaled = player.scale_damage(base)

        self.assertGreater(scaled, base)

    def test_enemy_round_is_phase_based(self):
        enemy = Enemy('Boss', 40, 20, 2)
        enemy.set_phase(2)
        self.assertGreaterEqual(enemy.phase, 2)


if __name__ == '__main__':
    unittest.main()
