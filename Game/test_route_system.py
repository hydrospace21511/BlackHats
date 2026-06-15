import unittest

from Game.Main.RouteManager import RouteManager, EndingManager


class RouteSystemTests(unittest.TestCase):
    def test_level_choices_include_one_mission_per_route(self):
        manager = RouteManager(seed=7)
        choices = manager.get_choices_for_level(1)

        self.assertEqual(len(choices), 3)
        self.assertEqual({item['route'] for item in choices}, {'BAD', 'GOOD', 'TRUE'})

    def test_full_progression_uses_fixed_mission_order(self):
        manager = RouteManager(seed=7)

        level_one = {item['route']: item['mission'] for item in manager.get_choices_for_level(1)}
        level_five = {item['route']: item['mission'] for item in manager.get_choices_for_level(5)}

        self.assertEqual(level_one['BAD'], 'Pioneer_Credit_Union')
        self.assertEqual(level_one['GOOD'], 'FakeWin_Registry')
        self.assertEqual(level_one['TRUE'], 'CityCare_Pharmacy_Log')

        self.assertEqual(level_five['BAD'], 'Global_Reserve_Node')
        self.assertEqual(level_five['GOOD'], 'ACSD_Public_Comms')
        self.assertEqual(level_five['TRUE'], 'Dept_of_Vital_Stats')

    def test_all_15_missions_are_reachable(self):
        manager = RouteManager(seed=7)
        all_missions = []

        for level in range(1, 6):
            all_missions.extend(item['mission'] for item in manager.get_choices_for_level(level))

        self.assertEqual(len(set(all_missions)), 15)

    def test_display_positions_are_shuffled_but_missions_are_fixed(self):
        manager = RouteManager(seed=11)
        choices = manager.get_choices_for_level(2)

        names = [item['mission'] for item in choices]
        self.assertEqual(sorted(names), sorted([
            'Apex_Investments_DB',
            'DebtHounds_Inc',
            'Aegis_Health_Insurance',
        ]))

    def test_ending_manager_returns_expected_results(self):
        ending = EndingManager()

        self.assertEqual(ending.evaluate(['BAD'] * 5), 'ENDING_BAD')
        self.assertEqual(ending.evaluate(['GOOD'] * 5), 'ENDING_GOOD')
        self.assertEqual(ending.evaluate(['TRUE'] * 5), 'ENDING_TRUE')
        self.assertEqual(ending.evaluate(['BAD', 'GOOD', 'BAD', 'TRUE', 'GOOD']), 'ENDING_NORMAL')

    def test_save_and_load_in_badges(self):
        manager = RouteManager(seed=3)
        badges = {}

        manager.save_progress(badges, ['BAD', 'GOOD', 'TRUE', 'BAD', 'GOOD'])
        loaded = manager.load_progress(badges)

        self.assertEqual(loaded['route_history'], ['BAD', 'GOOD', 'TRUE', 'BAD', 'GOOD'])
        self.assertEqual(loaded['ending'], 'ENDING_NORMAL')

    def test_save_and_load_inventory(self):
        manager = RouteManager(seed=3)

        payload = manager.save_progress({}, ['BAD'], inventory=['Test', 'Test2'], level=2)

        self.assertEqual(payload['inventory'], ['Test', 'Test2'])

        loaded = manager.load_progress({})
        self.assertEqual(loaded['inventory'], ['Test', 'Test2'])
        self.assertEqual(loaded['level'], 2)


if __name__ == '__main__':
    unittest.main()
