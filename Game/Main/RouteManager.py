import json
import os
import random
from pathlib import Path


class EndingManager:

    def evaluate(self, route_history):
        history = [str(item).upper().strip() for item in (route_history or [])]
        
        if len(history) >= 5:
            last_5 = history[-5:]
            
            if all(item == "BAD" for item in last_5):
                return "ENDING_BAD"
            if all(item == "GOOD" for item in last_5):
                return "ENDING_GOOD"
            if all(item == "TRUE" for item in last_5):
                return "ENDING_TRUE"
            
            return "ENDING_NORMAL"
        return ""

class RouteManager:

    BAD_ROUTE = [
        "Pioneer_Credit_Union",
        "Apex_Investments_DB",
        "Cayman_Offshore_Net",
        "MacroGrid_Tech_Host",
        "Global_Reserve_Node",
    ]

    GOOD_ROUTE = [
        "FakeWin_Registry",
        "DebtHounds_Inc",
        "ShadowBet_Servers",
        "LPD_Evidence_Archive",
        "ACSD_Public_Comms",
    ]

    TRUE_ROUTE = [
        "CityCare_Pharmacy_Log",
        "Aegis_Health_Insurance",
        "Metro_Hospital_Arch",
        "Blackwood_Psych_Ward",
        "Dept_of_Vital_Stats",
    ]

    ROUTES = {
        "BAD": BAD_ROUTE,
        "GOOD": GOOD_ROUTE,
        "TRUE": TRUE_ROUTE,
    }

    def __init__(self, seed=7):
        self.seed = seed
        self.progress_path = Path(__file__).with_name("DataStore.json")
        self.legacy_progress_path = Path(__file__).with_name("route_progress.json")

    def get_choices_for_level(self, level=None):
        level = max(1, min(5, int(level or 1)))
        index = level - 1

        choices = [
            {"route": "BAD", "mission": self.BAD_ROUTE[index], "display_position": 0, "level": level},
            {"route": "GOOD", "mission": self.GOOD_ROUTE[index], "display_position": 1, "level": level},
            {"route": "TRUE", "mission": self.TRUE_ROUTE[index], "display_position": 2, "level": level},
        ]

        rng = random.Random(self.seed + level)
        display_order = list(range(3))
        rng.shuffle(display_order)
        for choice, position in zip(choices, display_order):
            choice['display_position'] = position
        return choices

    def save_progress(self, badges, route_history, ending=None, mission_history=None, level=None, inventory=None, tasks=None, chests=None):
        route_history = list(route_history or [])
        ending = ending or EndingManager().evaluate(route_history)
        badges = dict(badges or {})

        completed_tasks = len(route_history)
        badges['Normal Ending'] = bool(completed_tasks >= 5 and ending == 'ENDING_NORMAL')
        badges['Good Ending'] = bool(completed_tasks >= 5 and ending == 'ENDING_GOOD')
        badges['Bad Ending'] = bool(completed_tasks >= 5 and ending == 'ENDING_BAD')
        badges['Mr.Robot'] = bool(completed_tasks >= 5 and ending == 'ENDING_TRUE')

        payload = {
            "level": int(level) if level is not None else max(1, min(5, completed_tasks + 1)),
            "badges": badges,
            "route_history": route_history,
            "mission_history": list(mission_history or []),
            "inventory": list(inventory or []),
            "tasks": int(tasks) if tasks is not None else 0,
            "chests": int(chests) if chests is not None else 0,
            "ending": ending,
            "seed": self.seed,
        }
        self.progress_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        return payload

    def load_progress(self, badges):
        payload = None

        if self.progress_path.exists():
            try:
                payload = json.loads(self.progress_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                payload = None

        if payload is None and self.legacy_progress_path.exists():
            try:
                payload = json.loads(self.legacy_progress_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                payload = None

        if payload is None:
            payload = {"level": 1, "route_history": [], "mission_history": [], "ending": "", "badges": badges or {}}

        route_history = [str(item).upper().strip() for item in payload.get("route_history", [])]
        ending = payload.get("ending") or EndingManager().evaluate(route_history)
        badges_payload = dict(payload.get("badges", badges or {}))

        completed_tasks = len(route_history)
        badges_payload['Normal Ending'] = bool(completed_tasks >= 5 and ending == 'ENDING_NORMAL')
        badges_payload['Good Ending'] = bool(completed_tasks >= 5 and ending == 'ENDING_GOOD')
        badges_payload['Bad Ending'] = bool(completed_tasks >= 5 and ending == 'ENDING_BAD')
        badges_payload['Mr.Robot'] = bool(completed_tasks >= 5 and ending == 'ENDING_TRUE')

        tasks = int(payload.get('tasks', 0))
        chests = int(payload.get('chests', 0))

        import Game.Main.Player as PlayerStats
        PlayerStats.set_lifetime_stats(tasks, chests)

        return {
            "level": int(payload.get("level", max(1, min(5, len(route_history) + 1)))),
            "route_history": route_history,
            "mission_history": list(payload.get("mission_history", [])),
            "inventory": list(payload.get("inventory", [])),
            "tasks": tasks,
            "chests": chests,
            "ending": ending,
            "badges": badges_payload,
        }
