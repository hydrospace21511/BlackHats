import random

from Game.Main.Player import integrity_bar
from Game.Main.Color import cText


class Enemy:
    PHASE_DATA = {
        "BAD": [
            {"name": "Pioneer_Credit_Union",  "hp": 180, "defense":  6, "regen": 0, "attacks": {"Shadow Strike": 12, "Static Jolt":   18, "Signal Glitch":  20}},
            {"name": "Apex_Investments_DB",   "hp": 260, "defense": 10, "regen": 1, "attacks": {"Shadow Strike": 16, "Inferno Blast":  22, "Data Leak":      25}},
            {"name": "Cayman_Offshore_Net",   "hp": 340, "defense": 14, "regen": 2, "attacks": {"Inferno Blast":  24, "Phantom Slash":  28, "Net Collapse":   32}},
            {"name": "MacroGrid_Tech_Host",   "hp": 420, "defense": 18, "regen": 3, "attacks": {"Phantom Slash":  30, "Chaos Roar":     36, "Grid Surge":     39}},
            {"name": "Global_Reserve_Node",   "hp": 500, "defense": 20, "regen": 4, "attacks": {"Chaos Roar":     38, "Null Pulse":     44, "Core Melt":      44}},
        ],
        "GOOD": [
            {"name": "FakeWin_Registry",      "hp": 240, "defense":  8, "regen": 1, "attacks": {"Phishing Burst": 16, "Logic Bomb":     22, "Trust Hijack":   25}},
            {"name": "DebtHounds_Inc",        "hp": 320, "defense": 12, "regen": 2, "attacks": {"Phishing Burst": 22, "Firewall Breach":28, "Ledger Burn":    31}},
            {"name": "ShadowBet_Servers",     "hp": 400, "defense": 16, "regen": 3, "attacks": {"Firewall Breach":28, "Kernel Panic":   34, "Server Melt":    37}},
            {"name": "LPD_Evidence_Archive",  "hp": 490, "defense": 18, "regen": 4, "attacks": {"Kernel Panic":   36, "Data Flood":     42, "Archive Breach":  45}},
            {"name": "ACSD_Public_Comms",     "hp": 590, "defense": 22, "regen": 5, "attacks": {"Data Flood":     44, "Signal Jam":     50, "Channel Burn":    52}},
        ],
        "TRUE": [
            {"name": "CityCare_Pharmacy_Log", "hp": 320, "defense": 10, "regen": 2, "attacks": {"Fatal Script":   20, "Red Code":       26, "Biohazard Loop":  29}},
            {"name": "Aegis_Health_Insurance","hp": 410, "defense": 14, "regen": 3, "attacks": {"Fatal Script":   26, "Biohack Pulse":  32, "Triage Collapse": 36}},
            {"name": "Metro_Hospital_Arch",   "hp": 520, "defense": 18, "regen": 4, "attacks": {"Biohack Pulse":  34, "Overclock Burst":40, "Careline Surge":  43}},
            {"name": "Clearview_Records",     "hp": 640, "defense": 24, "regen": 5, "attacks": {"Overclock Burst":42, "Mind Plague":    48, "Record Wipe":     50}},
            {"name": "Dept_of_Vital_Stats",   "hp": 780, "defense": 28, "regen": 6, "attacks": {"Mind Plague":    50, "Cobalt Storm":   58, "Vital Panic":     60}},
        ],
    }

    def __init__(self, name, max_health, defense, regen, attacks=None):
        self.Name = name
        self.MaxHealth = int(max_health)
        self.Health = int(max_health)
        self.Defense = int(defense)
        self.Regen = int(regen)
        self.Attacks = attacks or {}
        self.phase = 1
        self.max_hp = self.MaxHealth

    def set_phase(self, phase):
        self.phase = max(1, int(phase))
        self.Health = self.MaxHealth
        self.Defense = int(self.Defense + (self.phase - 1) * 2)
        self.max_hp = self.MaxHealth
        return self

    @classmethod
    def create_phase_enemy(cls, route_name, level, mission_name=None):
        if mission_name == "DarkHats":
            enemy = cls(
                name="MOM No.2",
                max_health=2000,
                defense=40,
                regen=0,
                attacks={
                    "SYSTEM COLLAPSE": 80,
                    "MEMORY WIPE":     60,
                    "ROOT ACCESS":     100,
                }
            )
            enemy.route = str(route_name).upper().strip()
            enemy.phase = 5
            enemy.max_hp = enemy.MaxHealth
            return enemy

        route = str(route_name).upper().strip()
        phase_index = max(0, min(4, int(level) - 1))
        phase_data = cls.PHASE_DATA.get(route, cls.PHASE_DATA['BAD'])[phase_index]
        if mission_name:
            phase_data = dict(phase_data)
            phase_data['name'] = mission_name

        scaled_hp = int(phase_data['hp'])
        scaled_defense = int(phase_data['defense'])
        scaled_attacks = dict(phase_data['attacks'])

        enemy = cls(
            name=phase_data['name'],
            max_health=scaled_hp,
            defense=scaled_defense,
            regen=phase_data['regen'] + phase_index,
            attacks=scaled_attacks,
        )
        enemy.route = route
        enemy.phase = phase_index + 1
        enemy.max_hp = enemy.MaxHealth
        return enemy

    def random_attack(self):
        if not self.Attacks:
            return "Strike", max(5, self.Defense)
        attack_name = random.choice(list(self.Attacks.keys()))
        attack_damage = self.Attacks[attack_name]
        return attack_name, attack_damage

    def enemy_life(self, current_enemy):
        cText(f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║ {cText("COBALT VIRUS v1.0.2", "red")}                                      {cText("VIRUS MODE OVERVIEW", "red")} ║
╠═══════════════════════════════════════╦══════════════════════════════════════╣
║ ANOMALY NAME: {print(current_enemy.Name)}                         ║      INTEGRITY: {integrity_bar(current_enemy.Health, current_enemy.MaxHealth)}                      ║
╚═══════════════════════════════════════╩══════════════════════════════════════╝
        """)