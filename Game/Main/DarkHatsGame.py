import os
import sys
import getpass
from time import sleep
from rich.console import Console, Group
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.live import Live
from rich.spinner import Spinner
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeRemainingColumn

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from Game.Main.COBALT import COBALT_FS
from Game.ItemsLib.Items.TestItem import TestItemClass
from Game.ItemsLib.Items.TestItem2 import TestItem2Class
from Game.Classes.SecurityAnalyticClass import SecurityAnalyticClass
from Game.Main.UI import enemy_life, display_battle_ui
from Game.Classes.HackerClass import HackerClass
from Game.Classes.SocialEngineerClass import SocialEngineerClass
from Game.Classes.ReverseEngineerClass import ReverseEngineerClass
from Game.Classes.SecurityBypasser import SecurityBypasserClass
from Game.Classes.HardwareSpecialistClass import HardwareSpecialistClass
from Game.Classes.SecretClasses.Hatsune import HatsuneMikuClass
from Game.Classes.SecretClasses.CorruptedHatsune import CorruptedHatsuneMikuClass
from Game.Classes.SecretClasses.Rimuru import RimuruClass
from Game.Classes.LambdaClass import LambdaClass
import Game.Main.Player as PlayerModule
from Game.ItemsLib.Chests.NPC_Chest import open_chest
import Game.Main.Player as PlayerStats
from Game.Main.Player import integrity_bar, defense_bar
from Game.Main.Enemy import Enemy
from Game.Main.RouteManager import RouteManager
from colorama import Fore, Back, Style, init
from Game.Main.Color import cText
from Game.Classes.ClassesMenu import classes_menu

init(autoreset=True)

from Game.Attacks.SpecialAttacks import (
    DecompilerAttack, AlgorithmCloneAttack, ProtectionBypassAttack,
    InternalAccessAttack, BaitingAttack, FirewallAttack, SecurityPatchAttack,
    DesintegrationAttack, MikuMikuBeamAttack, NegativeSpaceAttack,
    GiveDamageAttack, PneumoultramicroscopicsilicovolcanoconioticAttack,
    WorldIsMineAttack, TellYourWorldAttack, SystemOverrideAttack
)

true_level = 0


def get_key():
    if os.name == 'nt':
        import msvcrt
        key = msvcrt.getch()
        if key == b'\xe0':
            special = msvcrt.getch()
            if special == b'H': return 'UP'
            if special == b'P': return 'DOWN'
            if special == b'K': return 'LEFT'
            if special == b'M': return 'RIGHT'
        elif key in (b'\r', b'\n'):
            return 'ENTER'
        elif key == b' ':
            return 'SPACE'
        return None
    else:
        import tty, termios, sys
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            if ch == '\x1b':
                ch2 = sys.stdin.read(1)
                if ch2 == '[':
                    ch3 = sys.stdin.read(1)
                    if ch3 == 'A': return 'UP'
                    if ch3 == 'B': return 'DOWN'
                    if ch3 == 'C': return 'RIGHT'
                    if ch3 == 'D': return 'LEFT'
            elif ch in ('\r', '\n'):
                return 'ENTER'
            elif ch == ' ':
                return 'SPACE'
            return None
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def user():
    return getpass.getuser()

def Damage(D, Defense):
    return D * (1 - Defense / 100)


def apply_item_buffs(player, player_class):
    base_integrity = int(getattr(player_class, 'Integrity', 0))
    base_defense = int(getattr(player_class, 'Defense', 0))
    base_regen = int(getattr(player_class, 'Regen', 0))
    base_attack_power = int(getattr(player_class, 'attack_power', 0))

    total_defense = base_defense
    total_regen = base_regen
    total_attack_power = base_attack_power

    items = getattr(player_class, 'Items', None)
    if items in (None, 'None'):
        items = set()

    total_integrity_bonus = 0
    for item in items or []:
        total_integrity_bonus += int(getattr(item, 'Integrity', 0))
        total_defense += int(getattr(item, 'Defense', 0))
        total_regen += int(getattr(item, 'Regen', 0))
        total_attack_power += int(getattr(item, 'AttackPower', 0))

    previous_max = int(getattr(player, 'max_integrity', base_integrity))
    max_integrity = base_integrity + total_integrity_bonus

    current_integrity = int(getattr(player, 'Integrity', max_integrity))
    if current_integrity <= 0:
        current_integrity = max_integrity
    elif previous_max > 0 and max_integrity > 0:
        ratio = current_integrity / previous_max if previous_max > 0 else 1.0
        current_integrity = int(max_integrity * ratio)
    current_integrity = max(0, min(current_integrity, max_integrity))

    player.Integrity = current_integrity
    player.Defense = total_defense
    player.Regen = total_regen
    player.attack_power = total_attack_power

    player_class.Integrity = max_integrity
    player_class.Defense = base_defense
    player_class.Regen = base_regen
    player_class.attack_power = base_attack_power
    player_class.max_integrity = max_integrity
    return player, player_class


LEVEL_UP_DATA = {

    2: {
        "title":    "ATUALIZAÇÃO v2.0 — NOVOS ARQUIVOS DETECTADOS",
        "new_docs": ["Diário.txt", "Morgan.txt"],
        "hint":     "Você pode vê-los na aba 'Documentos' do sistema.",
        "badges":   [],
    },

    3: {
        "title":    "ATUALIZAÇÃO v3.0 — NOVOS ARQUIVOS DETECTADOS",
        "new_docs": ["Relato.txt", "Morgan2.txt"],
        "hint":     "Você recebeu algumas notícias em 'Documentos'.",
        "badges":   [],
    },
    4: {
        "title":    "ATUALIZAÇÃO v4.0 — ARQUIVO CORROMPIDO RECUPERADO",
        "new_docs": ["Lembranças.txt", "A Raiz.txt"],
        "hint":     "Um fragmento antigo ressurgiu em 'Documentos'.",
        "badges":   [],
    },
    5: {
        "title":    "ATUALIZAÇÃO v5.0 — PROCESSO DESCONHECIDO DETECTADO",
        "new_docs": ["NULL.txt"],
        "hint":     "Algo escreveu em 'Documentos'. Não foi você.",
        "badges":   [],
    },
    6: {
        "title":    "ERROR v6.0 — PARTIÇÃO FINAL MONTADA",
        "new_docs": ["SHEOL.txt"],
        "hint":     "O último registro está em 'Documentos'.",
        "badges":   ["DarkHats"],
    },
}


def _compute_effective_badges(raw_badges: dict, tasks: int, chests: int) -> dict:
    effective = dict(raw_badges or {})
    effective.setdefault("Social Engineer", False)
    effective.setdefault("Hardware Specialist", False)
    effective.setdefault("Security Bypass", False)
    effective.setdefault("Reverse Engineer", False)
    effective.setdefault("Security Analytic", False)
    effective.setdefault("Mr.Robot", False)
    effective.setdefault("Normal Ending", False)
    effective.setdefault("Good Ending", False)
    effective.setdefault("Bad Ending", False)
    effective.setdefault("???", False)
    effective.setdefault("DarkHats", False)

    effective["Social Engineer"] = effective["Social Engineer"] or (tasks >= 2)
    effective["Security Bypass"] = effective["Security Bypass"] or (tasks >= 1)
    effective["Security Analytic"] = effective["Security Analytic"] or (tasks >= 3)
    effective["Reverse Engineer"] = effective["Reverse Engineer"] or (tasks >= 5)
    effective["Hardware Specialist"] = effective["Hardware Specialist"] or (chests >= 3)
    effective["???"] = effective["???"] or (tasks >= 6)
    effective["DarkHats"] = effective["DarkHats"] or (tasks >= 6 and chests >= 5)
    return effective


def _show_level_up(player_level: int, old_state: dict, new_state: dict):
    data = LEVEL_UP_DATA.get(player_level)
    old_badges = _compute_effective_badges(old_state.get("badges", {}), old_state.get("tasks", 0), old_state.get("chests", 0))
    new_badges = _compute_effective_badges(new_state.get("badges", {}), new_state.get("tasks", 0), new_state.get("chests", 0))

    clear()
    cText(f"A versão do seu sistema ({player_level - 1}.0) está atualmente desatualizada.", "error")
    sleep(1.5)
    cText(f"Gostaria de atualizar a versão do seu sistema para {player_level}.0?", "green")
    sleep(1)
    input(f"\n  {Fore.LIGHTBLACK_EX}[ Pressione ENTER para continuar ]{Style.RESET_ALL}")
    clear()

    with Progress(
        TextColumn("[bold green]COBALT OS"),
        BarColumn(bar_width=40, complete_style="green", finished_style="bright_green"),
        TextColumn("[green]{task.percentage:>3.0f}%"),
        TimeRemainingColumn(),
    ) as progress:
        task = progress.add_task("Atualizando...", total=100)
        while not progress.finished:
            progress.advance(task, 1)
            sleep(0.04)

    sleep(1)
    clear()
    cText(f" Sistema atualizado com sucesso. Versão {player_level}.0 instalada.", "positive")
    sleep(1.5)
    input(f"\n  {Fore.LIGHTBLACK_EX}[ Pressione ENTER para ver as novidades ]{Style.RESET_ALL}")

    if data is None:
        clear()
        cText("Update concluído.", "green")
        input(f"\n  {Fore.LIGHTBLACK_EX}[ Pressione ENTER para sair ]{Style.RESET_ALL}")
        return

    clear()

    cText(f"[ {data['title']} ]", "cyan")
    sleep(0.8)
    print()

    new_docs = data.get("new_docs", [])
    if new_docs:
        count = len(new_docs)
        cText(f"  {count} novo(s) arquivo(s) inserido(s):", "green")
        sleep(0.5)
        for doc in new_docs:
            sleep(0.6)
            cText(f"    ▸  {doc}", "white")
        sleep(0.4)
        print()
        cText(f"  {data['hint']}", "warn")

    unlocked_badges = [
        i for i, unlocked in new_badges.items()
        if unlocked and not old_badges.get(i, False)
        and i not in ("Normal Ending", "Good Ending", "Bad Ending", "???")
    ]
    if unlocked_badges:
        sleep(1)
        print()
        cText("  [ CONQUISTAS DESBLOQUEADAS ]", "yellow")
        for i in unlocked_badges:
            sleep(0.5)
            cText(f"    🏅  {i}", "yellow")

    print()
    input(f"\n  {Fore.LIGHTBLACK_EX}[ Pressione ENTER para sair ]{Style.RESET_ALL}")


class DarkHatsGame:
    def __init__(self):
        self.Hacker               = HackerClass()
        self.Rimuru               = RimuruClass()
        self.SecurityAnalytic     = SecurityAnalyticClass()
        self.SecurityBypasser     = SecurityBypasserClass()
        self.HardwareSpecialist   = HardwareSpecialistClass()
        self.SocialEngineer       = SocialEngineerClass()
        self.Vocaloid             = HatsuneMikuClass()
        self.Lambda               = LambdaClass()
        self.ReverseEngineer      = ReverseEngineerClass()
        self.CorruptedHatsuneMiku = CorruptedHatsuneMikuClass()
        self.Player               = PlayerModule.Player()
        self.custom_boss_config = None

        self.attack_functions = {
            "Decompiler":                               DecompilerAttack,
            "Algorithm Clone":                          AlgorithmCloneAttack,
            "Protection Bypass":                        ProtectionBypassAttack,
            "Internal Access":                          InternalAccessAttack,
            "Miku Miku Beam":                           MikuMikuBeamAttack,
            "Tell Your World":                          TellYourWorldAttack,
            "World Is Mine":                            WorldIsMineAttack,
            "Baiting":                                  BaitingAttack,
            "Firewall":                                 FirewallAttack,
            "Security Patch":                           SecurityPatchAttack,
            "Pneumoultramicroscopicsilicovolcanoconiotic": PneumoultramicroscopicsilicovolcanoconioticAttack,
            "Desintegration":                           DesintegrationAttack,
            "Negative Space":                           NegativeSpaceAttack,
            "System Override":                          SystemOverrideAttack,
        }

    def set_custom_boss(self, name=None, max_health=None, defense=0, regen=0, attacks=None, phase=1):
        self.custom_boss_config = {
            "name": name or "CUSTOM BOSS",
            "max_health": int(max_health) if max_health is not None else 500,
            "defense": int(defense),
            "regen": int(regen),
            "attacks": dict(attacks or {}),
            "phase": int(phase),
        }
        return self

    def clear_custom_boss(self):
        self.custom_boss_config = None
        return self

    def _build_current_enemy(self, route_choice, player_level, mission_name=None):
        if self.custom_boss_config:
            boss_cfg = self.custom_boss_config
            enemy = Enemy(
                name=boss_cfg["name"],
                max_health=boss_cfg["max_health"],
                defense=boss_cfg["defense"],
                regen=boss_cfg["regen"],
                attacks=boss_cfg["attacks"] or {"SYSTEM COLLAPSE": 50},
            )
            enemy.route = str(route_choice).upper().strip()
            enemy.phase = max(1, int(boss_cfg.get("phase", 1)))
            enemy.max_hp = enemy.MaxHealth
            enemy.Health = enemy.MaxHealth
            return enemy

        current_enemy = Enemy.create_phase_enemy(route_choice, player_level, mission_name=mission_name)
        current_enemy.set_phase(max(1, (player_level // 2) + 1))
        current_enemy.Health = current_enemy.MaxHealth
        return current_enemy

    def start(self):
        clear()
        badges = RouteManager().load_progress({}, update_stats=False).get("badges", {})
        chosen = classes_menu(badges=badges)

        if chosen is None or chosen == "EXIT":
            return

        class_map = {
            "HACKER":               self.Hacker,
            "SECURITY ANALYTIC":    self.SecurityAnalytic,
            "SOCIAL ENGINEER":      self.SocialEngineer,
            "REVERSE ENGINEER":     self.ReverseEngineer,
            "HARDWARE SPECIALIST":  self.HardwareSpecialist,
            "SECURITY BYPASSER":    self.SecurityBypasser,
            "HATSUNE MIKU":         self.Vocaloid,
            "LAMBDA":               self.Lambda,
        }
        PlayerClass = class_map.get(chosen)
        if not PlayerClass:
            return

        cText("▶  Digite seu nome >>", "green")
        self.Player.Name = input("")
        if self.Player.Name == "Return":
            clear()
            return

        self.Player.Class     = PlayerClass

        if not hasattr(self.Player.Class, 'Items') or self.Player.Class.Items in (None, 'None'):
            self.Player.Class.Items = set()

        saved_progress  = RouteManager().load_progress({})
        inventory_names = saved_progress.get('inventory', [])
        if inventory_names:
            for item_name in inventory_names:
                item = open_chest.__globals__['get_item_by_name'](item_name)
                if item is not None:
                    self.Player.Class.Items.add(item)

        apply_item_buffs(self.Player, self.Player.Class)

        clear()
        cText(f">> Welcome {self.Player.Name}!", "green")
        sleep(2)
        cText(f">> Your class is: {self.Player.Class.raceName}", "green")
        sleep(2)
        clear()

        route_choice   = getattr(self, 'route_choice', 'BAD')
        mission_name   = getattr(self, 'mission_name', None)
        current_enemy  = self._build_current_enemy(route_choice, self.Player.Level, mission_name=mission_name)
        active_cooldowns = {}

        while True:
            actual_selection = 0

            while True:
                attack_list   = list(self.Player.Class.Attacks.keys())
                total_attacks = len(attack_list)

                while True:
                    clear()
                    enemy_life(current_enemy)
                    display_battle_ui(
                        player_integrity=self.Player.Integrity,
                        max_integrity=getattr(self.Player.Class, 'max_integrity', self.Player.Class.Integrity),
                        player_defense=self.Player.Defense,
                        available_attacks=attack_list,
                        ui_color=self.Player.Class.ui_color,
                        player_name=self.Player.Name,
                        class_name=PlayerClass.raceName,
                        selected_index=actual_selection
                    )
                    tecla = get_key()
                    if tecla == 'DOWN':
                        actual_selection = (actual_selection + 2) % total_attacks
                    elif tecla == 'UP':
                        actual_selection = (actual_selection - 2) % total_attacks
                    elif tecla == 'RIGHT':
                        actual_selection = (actual_selection + 1) % total_attacks
                    elif tecla == 'LEFT':
                        actual_selection = (actual_selection - 1) % total_attacks
                    elif tecla in ('ENTER', 'SPACE'):
                        Attack = attack_list[actual_selection]
                        break

                clear()
                enemy_life(current_enemy)
                display_battle_ui(
                    self.Player.Integrity, getattr(self.Player.Class, 'max_integrity', self.Player.Class.Integrity),
                    self.Player.Defense, self.Player.Class.Attacks.keys(),
                    self.Player.Class.ui_color,
                    player_name=self.Player.Name, class_name=PlayerClass.raceName,
                    selected_index=actual_selection
                )
                cText(f"\n>> EXECUTANDO PROTOCOLO: {Attack.upper()}...", "green")
                sleep(1)

                if Attack == "Reverse" and getattr(self.Player.Class, 'Decompiled', False):
                    clear()
                    enemy_life(current_enemy)
                    display_battle_ui(
                        self.Player.Integrity, getattr(self.Player.Class, 'max_integrity', self.Player.Class.Integrity),
                        self.Player.Defense, self.Player.Class.Attacks.keys(),
                        self.Player.Class.ui_color,
                        player_name=self.Player.Name, class_name=PlayerClass.raceName,
                        selected_index=actual_selection
                    )
                    cText(" Invertendo a descompilação...", "warn")
                    sleep(2)
                    cText(" Descompilação invertida! Seus status e ataques originais foram restaurados!", "positive")
                    sleep(2)
                    self.Player.Class.Decompiled = False
                    self.Player.Class.Attacks    = self.Player.Class.OriginalAttacks
                    self.Player.Class.Defense    = self.Player.Class.DefenseBackup
                    self.Player.Class.Integrity  = self.Player.Class.IntegrityBackup
                    clear()

                if Attack not in self.Player.Class.Attacks:
                    clear()
                    enemy_life(current_enemy)
                    display_battle_ui(
                        self.Player.Integrity, getattr(self.Player.Class, 'max_integrity', self.Player.Class.Integrity),
                        self.Player.Defense, self.Player.Class.Attacks.keys(),
                        self.Player.Class.ui_color,
                        player_name=self.Player.Name, class_name=PlayerClass.raceName,
                        selected_index=actual_selection
                    )
                    cText("⚠  ERRO 04: Exploit não encontrado", "red")
                    sleep(2)
                    continue

                if Attack in active_cooldowns and active_cooldowns[Attack] > 0:
                    clear()
                    enemy_life(current_enemy)
                    display_battle_ui(
                        self.Player.Integrity, getattr(self.Player.Class, 'max_integrity', self.Player.Class.Integrity),
                        self.Player.Defense, self.Player.Class.Attacks.keys(),
                        self.Player.Class.ui_color,
                        player_name=self.Player.Name, class_name=PlayerClass.raceName,
                        selected_index=actual_selection
                    )
                    cText(f"⚠  ACCESSO NEGADO: '{Attack}' está em cooldown! ({active_cooldowns[Attack]} turnos restantes)", "yellow")
                    sleep(2.5)
                    continue

                raw_attack = self.Player.Class.Attacks[Attack]
                if isinstance(raw_attack, tuple):
                    base_damage, damage_per_level = raw_attack
                else:
                    base_damage      = raw_attack
                    damage_per_level = 0

                base_damage      = float(base_damage)
                class_power      = getattr(self.Player.Class, 'attack_power', 0)
                level_multiplier = 1.0 + (self.Player.Level - 1) * 0.15
                Attack_Info      = base_damage * level_multiplier
                Attack_Info     += float(damage_per_level) * max(0, self.Player.Level - 1)
                Attack_Info     += class_power * 0.15

                context = (
                    self.Player, current_enemy, Attack_Info,
                    display_battle_ui, integrity_bar, defense_bar,
                    Damage, Attack, self.Player.Class
                )

                if Attack in self.attack_functions:
                    self.attack_functions[Attack](*context)

                if Attack == "Give Damage":
                    self.Player.Integrity -= Attack_Info

                if hasattr(current_enemy, "SkipTurn") and current_enemy.SkipTurn:
                    cText(">> Turno do inimigo skippado!", "yellow")
                    current_enemy.SkipTurn = False
                    sleep(2)
                    clear()
                    enemy_life(current_enemy)
                    display_battle_ui(
                        self.Player.Integrity, getattr(self.Player.Class, 'max_integrity', self.Player.Class.Integrity),
                        self.Player.Defense, self.Player.Class.Attacks.keys(),
                        self.Player.Class.ui_color,
                        player_name=self.Player.Name, class_name=PlayerClass.raceName,
                        selected_index=actual_selection
                    )
                    continue
                else:
                    clear()
                    enemy_life(current_enemy)
                    display_battle_ui(
                        self.Player.Integrity, getattr(self.Player.Class, 'max_integrity', self.Player.Class.Integrity),
                        self.Player.Defense, self.Player.Class.Attacks.keys(),
                        self.Player.Class.ui_color,
                        player_name=self.Player.Name, class_name=PlayerClass.raceName,
                        selected_index=actual_selection
                    )
                    final_damage = Damage(Attack_Info, current_enemy.Defense)
                    current_enemy.Health -= final_damage
                    cText(f" >> Você executou [{Attack}]! {current_enemy.Name} levou {final_damage:.1f} de dano!", "positive")

                if hasattr(self.Player.Class, 'Cooldowns') and Attack in self.Player.Class.Cooldowns:
                    active_cooldowns[Attack] = self.Player.Class.Cooldowns[Attack]

                if current_enemy.Health <= 0:
                    sleep(1.5)
                    clear()
                    cText(f"\n   [>> NODE COMPROMETIDO <<]\n < -- {current_enemy.Name} hackeado! -- >\n", "green")
                    sleep(4)
                    clear()

                    current_enemy.Health += current_enemy.MaxHealth * 0.5
                    import Game.Main.Player as PlayerStats
                    PlayerStats.record_task_completed()

                    if not getattr(self.Player.Class, 'Items', None):
                        self.Player.Class.Items = set()

                    chest_opened = open_chest(self.Player)
                    if chest_opened:
                        PlayerStats.record_chest_opened()

                    saved_progress  = RouteManager().load_progress({}, update_stats=False)
                    inventory_names = list(saved_progress.get('inventory', []))
                    if chest_opened and hasattr(chest_opened, 'itemName'):
                        inventory_names.append(chest_opened.itemName)
                    inventory_names = list(dict.fromkeys(inventory_names))

                    route_history = list(saved_progress.get('route_history', []))
                    mission_history = list(saved_progress.get('mission_history', []))

                    if route_choice and route_choice not in ("None", ""):
                        route_history.append(route_choice)
                    if mission_name:
                        mission_history.append(mission_name)

                    if mission_name == "DarkHats":
                        next_level = 6
                    else:
                        next_level = min(5, len(route_history) + 1)

                    RouteManager().save_progress(
                        saved_progress.get('badges', {}),
                        route_history,
                        None,
                        mission_history,
                        level=next_level,
                        inventory=inventory_names,
                        tasks=PlayerStats.get_lifetime_tasks(),
                        chests=PlayerStats.get_lifetime_chests()
                    )

                    item_set        = set(getattr(self.Player.Class, 'Items', []))
                    Integrity_boost = sum(getattr(item, 'Integrity', 0) for item in item_set)
                    Defense_boost   = sum(getattr(item, 'Defense',   0) for item in item_set)
                    self.Player.Defense   += Defense_boost
                    self.Player.Integrity += Integrity_boost

                    saved_now   = RouteManager().load_progress({}, update_stats=False)
                    badges_now  = saved_now.get('badges', {})
                    tasks_now   = int(saved_now.get('tasks', 0))
                    chests_now  = int(saved_now.get('chests', 0))
                    previous_state = {
                        'badges': saved_progress.get('badges', {}),
                        'tasks': int(saved_progress.get('tasks', 0)),
                        'chests': int(saved_progress.get('chests', 0)),
                    }
                    new_state = {
                        'badges': badges_now,
                        'tasks': tasks_now,
                        'chests': chests_now,
                    }
                    level_now   = int(saved_now.get('level', self.Player.Level))

                    _show_level_up(level_now, previous_state, new_state)

                    return

                sleep(1.5)
                break

            enemy_attack_name, enemy_attack_dmg = current_enemy.random_attack()
            enemy_final_damage = Damage(enemy_attack_dmg, self.Player.Defense)
            self.Player.Integrity -= enemy_final_damage
            cText(f" >> {current_enemy.Name} executou [{enemy_attack_name}]! Você levou {enemy_final_damage:.1f} de dano!", "error")
            sleep(2.5)

            if self.Player.Integrity <= 0:
                clear()
                cText(f"\n        [!]Erro 404[!] \n < -- Você foi hackeado -- >\n", "red")
                sleep(2)
                sleep(3)
                clear()
                return

            for skill in active_cooldowns:
                if active_cooldowns[skill] > 0:
                    active_cooldowns[skill] -= 1

            if self.Player.Regen > 0:
                self.Player.Integrity += self.Player.Regen
                if self.Player.Integrity >= self.Player.Class.Integrity:
                    self.Player.Integrity = self.Player.Class.Integrity
                self.Player.Regen = 0

            if self.Player.Defense >= 100:
                self.Player.Defense = 99

            clear()
            enemy_life(current_enemy)
            display_battle_ui(
                self.Player.Integrity, getattr(self.Player.Class, 'max_integrity', self.Player.Class.Integrity),
                self.Player.Defense, self.Player.Class.Attacks.keys(),
                self.Player.Class.ui_color,
                player_name=self.Player.Name, class_name=PlayerClass.raceName,
                selected_index=actual_selection
            )