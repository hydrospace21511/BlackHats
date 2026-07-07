import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.append(str(Path(__file__).resolve().parents[1]))

from Game.Main.COBALT import COBALT_FS
from Game.Main.DarkHatsGame import DarkHatsGame, apply_item_buffs
from Game.ItemsLib.Items.TestItem import TestItemClass


class CustomBossTests(unittest.TestCase):
    def test_custom_boss_config_overrides_enemy_creation(self):
        game = DarkHatsGame()
        game.set_custom_boss(
            name="Firewall King",
            max_health=777,
            defense=25,
            regen=3,
            attacks={"Rootkit": 40, "Ransomware": 50},
        )

        enemy = game._build_current_enemy(route_choice="BAD", player_level=5, mission_name=None)

        self.assertEqual(enemy.Name, "Firewall King")
        self.assertEqual(enemy.MaxHealth, 777)
        self.assertEqual(enemy.Health, 777)
        self.assertEqual(enemy.Defense, 25)
        self.assertEqual(enemy.Regen, 3)
        self.assertEqual(enemy.Attacks, {"Rootkit": 40, "Ransomware": 50})

    def test_completed_darkhats_entry_opens_discord_chan_boss(self):
        explorer = COBALT_FS()
        with patch.object(explorer, "_open_custom_boss") as mock_open:
            explorer.handle_action({"type": "INFO", "name": "[COMPLETO] DarkHats finalizado!"})

        mock_open.assert_called_once()
        kwargs = mock_open.call_args.kwargs
        self.assertEqual(kwargs["name"], "Discord-chan")
        self.assertEqual(kwargs["max_health"], 10000)
        self.assertEqual(kwargs["defense"], 0)
        self.assertEqual(kwargs["attacks"]["Ping Storm"], 220)

    def test_apply_item_buffs_gives_full_hp_when_player_current_hp_is_zero(self):
        game = DarkHatsGame()
        player = game.Player
        class_obj = type(
            "FakeClass",
            (),
            {"Integrity": 130, "Defense": 10, "Regen": 2, "attack_power": 0, "Items": set()},
        )()
        player.Class = class_obj
        player.Integrity = 0
        player.max_integrity = 0
        player.Defense = 10
        player.Regen = 2
        player.attack_power = 0
        class_obj.Items.add(TestItemClass())

        apply_item_buffs(player, class_obj)

        self.assertEqual(player.Integrity, 215)
        self.assertEqual(class_obj.max_integrity, 215)


if __name__ == "__main__":
    unittest.main()
