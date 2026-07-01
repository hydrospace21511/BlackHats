import random

from Game.Main.Player import integrity_bar
from Game.Main.Color import cText


class Enemy:
    PHASE_DATA = {
        "BAD": [
            {"name": "Pioneer_Credit_Union", "hp": 180, "defense": 6, "regen": 0, "attacks": {"Shadow Strike": 12, "Static Jolt": 18, "Signal Glitch": 21}},
            {"name": "Apex_Investments_DB", "hp": 260, "defense": 10, "regen": 1, "attacks": {"Shadow Strike": 18, "Inferno Blast": 24, "Data Leak": 27}},
            {"name": "Cayman_Offshore_Net", "hp": 340, "defense": 14, "regen": 2, "attacks": {"Inferno Blast": 28, "Phantom Slash": 32, "Net Collapse": 35}},
            {"name": "MacroGrid_Tech_Host", "hp": 420, "defense": 18, "regen": 3, "attacks": {"Phantom Slash": 34, "Chaos Roar": 40, "Grid Surge": 43}},
            {"name": "Global_Reserve_Node", "hp": 520, "defense": 20, "regen": 4, "attacks": {"Chaos Roar": 42, "Null Pulse": 48, "Core Melt": 51}},
        ],
        "GOOD": [
            {"name": "FakeWin_Registry", "hp": 240, "defense": 8, "regen": 1, "attacks": {"Phishing Burst": 18, "Logic Bomb": 24, "Trust Hijack": 27}},
            {"name": "DebtHounds_Inc", "hp": 320, "defense": 12, "regen": 2, "attacks": {"Phishing Burst": 24, "Firewall Breach": 30, "Ledger Burn": 33}},
            {"name": "ShadowBet_Servers", "hp": 410, "defense": 16, "regen": 3, "attacks": {"Firewall Breach": 32, "Kernel Panic": 38, "Server Melt": 41}},
            {"name": "LPD_Evidence_Archive", "hp": 500, "defense": 18, "regen": 4, "attacks": {"Kernel Panic": 40, "Data Flood": 46, "Archive Breach": 49}},
            {"name": "ACSD_Public_Comms", "hp": 620, "defense": 22, "regen": 5, "attacks": {"Data Flood": 48, "Signal Jam": 54, "Channel Burn": 58}},
        ],
        "TRUE": [
            {"name": "CityCare_Pharmacy_Log", "hp": 320, "defense": 10, "regen": 2, "attacks": {"Fatal Script": 22, "Red Code": 28, "Biohazard Loop": 31}},
            {"name": "Aegis_Health_Insurance", "hp": 420, "defense": 14, "regen": 3, "attacks": {"Fatal Script": 30, "Biohack Pulse": 36, "Triage Collapse": 40}},
            {"name": "Metro_Hospital_Arch", "hp": 540, "defense": 18, "regen": 4, "attacks": {"Biohack Pulse": 38, "Overclock Burst": 44, "Careline Surge": 47}},
            {"name": "Blackwood_Psych_Ward", "hp": 680, "defense": 24, "regen": 5, "attacks": {"Overclock Burst": 46, "Mind Plague": 52, "Ward Collapse": 56}},
            {"name": "Dept_of_Vital_Stats", "hp": 840, "defense": 28, "regen": 6, "attacks": {"Mind Plague": 56, "Cobalt Storm": 64, "Vital Panic": 69}},
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
        multiplier = 1 + (self.phase - 1) * 0.2
        self.MaxHealth = int(self.MaxHealth * multiplier)
        self.Health = self.MaxHealth
        self.Defense = int(self.Defense + (self.phase - 1) * 2)
        self.max_hp = self.MaxHealth
        return self

    @classmethod
    def create_phase_enemy(cls, route_name, level, mission_name=None):
        route = str(route_name).upper().strip()
        phase_index = max(0, min(4, int(level) - 1))
        phase_data = cls.PHASE_DATA.get(route, cls.PHASE_DATA['BAD'])[phase_index]
        if mission_name:
            phase_data = dict(phase_data)
            phase_data['name'] = mission_name

        multiplier = 1 + (phase_index * 0.2)
        scaled_hp = int(phase_data['hp'] * multiplier)
        scaled_defense = int(phase_data['defense'] + (phase_index * 2))
        scaled_attacks = {k: int(v * multiplier) for k, v in phase_data['attacks'].items()}

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
    
    def enemy_life(self,current_enemy):
        cText(f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║ {cText("COBALT VIRUS v1.0.2", "red")}                                      {cText("VIRUS MODE OVERVIEW", "red")} ║
╠═══════════════════════════════════════╦══════════════════════════════════════╣
║ ANOMALY NAME: {print(current_enemy.Name)}                         ║      INTEGRITY: {integrity_bar(current_enemy.Health, current_enemy.MaxHealth)}                      ║
╚═══════════════════════════════════════╩══════════════════════════════════════╝
              
              """
              )