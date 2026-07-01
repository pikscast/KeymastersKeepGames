from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import Toggle, DefaultOnToggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class CallOfDutyBlackOps6ArchipelagoOptions:
    call_of_duty_black_ops_6_enable_multiplayer: CallOfDutyBlackOps6EnableMultiplayer
    call_of_duty_black_ops_6_enable_zombies: CallOfDutyBlackOps6EnableZombies
    call_of_duty_black_ops_6_include_post_launch_weapons: CallOfDutyBlackOps6IncludePostLaunchWeapons
    call_of_duty_black_ops_6_include_party_games: CallOfDutyBlackOps6IncludePartyGames


class CallOfDutyBlackOps6Game(Game):
    name = "Call of Duty: Black Ops 6"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = CallOfDutyBlackOps6ArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives: List[GameObjectiveTemplate] = list()

        if self.enable_multiplayer:
            objectives += self.multiplayer_objectives()

        if self.enable_zombies:
            objectives += self.zombies_objectives()

        return objectives

    def multiplayer_objectives(self) -> List[GameObjectiveTemplate]:
        objectives: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Complete 3 matches of GAMEMODE",
                data={
                    "GAMEMODE": (self.gamemodes, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a match of GAMEMODE",
                data={
                    "GAMEMODE": (self.gamemodes, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Get 10 kills with WEAPON",
                data={
                    "WEAPON": (self.weapons, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Get 10 METHOD kills",
                data={
                    "METHOD": (self.methods_multiplayer, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Deploy SCORESTREAK",
                data={
                    "SCORESTREAK": (self.scorestreaks_easy, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Deploy SCORESTREAK",
                data={
                    "SCORESTREAK": (self.scorestreaks_hard, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Use FIELDUPGRADE 3 times",
                data={
                    "FIELDUPGRADE": (self.field_upgrades_multiplayer, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete a match on MAP",
                data={
                    "MAP": (self.maps_multiplayer, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Capture 5 Objectives",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Appear in Top 3",
                data=dict(),
                is_time_consuming=False,
                is_difficult=True,
                weight=1
            ),
        ]

        if self.include_post_launch_weapons:
            objectives.append(
                GameObjectiveTemplate(
                    label="Get 10 kills with DLCWEAPON",
                    data={
                        "DLCWEAPON": (self.dlc_weapons, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3,
                ),
            )

        if self.include_party_games:
            objectives.append(
                GameObjectiveTemplate(
                    label="Complete 3 matches of PARTYGAME",
                    data={
                        "PARTYGAME": (self.party_games, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
            )
            objectives.append(
                GameObjectiveTemplate(
                    label="Win a match of PARTYGAME",
                    data={
                        "PARTYGAME": (self.party_games, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
            )

        return objectives

    def zombies_objectives(self) -> List[GameObjectiveTemplate]:
        objectives: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Exfil on round ROUND on MAP",
                data={
                    "ROUND": (self.rounds, 1),
                    "MAP": (self.maps_zombies, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete 5 S.A.M. Tasks on MAP",
                data={
                    "MAP": (self.maps_zombies, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Reach round 20 on MAP while CHALLENGE",
                data={
                    "MAP": (self.maps_zombies, 1),
                    "CHALLENGE": (self.challenges, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Complete Main Quest on MAP",
                data={
                    "MAP": (self.maps_zombies, 1),
                },
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Trigger secret song on MAP",
                data={
                    "MAP": (self.maps_zombies, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Kill 200 zombies with WEAPON",
                data={
                    "WEAPON": (self.weapons, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Kill 200 zombies with WONDERWEAPON",
                data={
                    "WONDERWEAPON": (self.wonder_weapons, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Upgrade WEAPON to Legendary rarity",
                data={
                    "WEAPON": (self.weapons, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Use the Pack-A-Punch to upgrade WEAPON to Tier III",
                data={
                    "WEAPON": (self.weapons, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Get 100 METHOD kills on zombies",
                data={
                    "METHOD": (self.methods_zombies, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Use FIELDUPGRADE 5 times",
                data={
                    "FIELDUPGRADE": (self.field_upgrades_zombies, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Kill ELITEZOMBIE with WEAPON",
                data={
                    "ELITEZOMBIE": (self.elite_zombies, 1),
                    "WEAPON": (self.weapons, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
        ]

        if self.include_post_launch_weapons:
            objectives.append(
                GameObjectiveTemplate(
                    label="Kill 200 zombies with DLCWEAPON",
                    data={
                        "DLCWEAPON": (self.dlc_weapons, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3,
                ),
            )
            objectives.append(
                GameObjectiveTemplate(
                    label="Upgrade DLCWEAPON to Legendary rarity",
                    data={
                        "DLCWEAPON": (self.dlc_weapons, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3,
                ),
            )
            objectives.append(
                GameObjectiveTemplate(
                    label="Use the Pack-A-Punch to upgrade DLCWEAPON to Tier III",
                    data={
                        "DLCWEAPON": (self.dlc_weapons, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3,
                ),
            )
            objectives.append(
                GameObjectiveTemplate(
                    label="Kill ELITEZOMBIE with DLCWEAPON",
                    data={
                        "ELITEZOMBIE": (self.elite_zombies, 1),
                        "DLCWEAPON": (self.dlc_weapons, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3,
                ),
            )

        return objectives

    @property
    def enable_multiplayer(self) -> bool:
        return bool(self.archipelago_options.call_of_duty_black_ops_6_enable_multiplayer.value)

    @property
    def enable_zombies(self) -> bool:
        return bool(self.archipelago_options.call_of_duty_black_ops_6_enable_zombies.value)

    @property
    def include_post_launch_weapons(self) -> bool:
        return bool(self.archipelago_options.call_of_duty_black_ops_6_include_post_launch_weapons.value)

    @property
    def include_party_games(self) -> bool:
        return bool(self.archipelago_options.call_of_duty_black_ops_6_include_party_games.value)

    @staticmethod
    def gamemodes() -> List[str]:
        return [
            "Team Deathmatch",
            "Kill Order",
            "Domination",
            "Hardpoint",
            "Kill Confirmed",
            "Headquarters",
            "Search and Destroy",
            "Free-for-all",
            "Demolition",
            "Control",
        ]

    @staticmethod
    def party_games() -> List[str]:
        return [
            "Prop Hunt",
            "Infected",
            "Gun Game",
            "Sharpshooter",
            "One in the Chamber",
            "Gunfight",
        ]

    @staticmethod
    def weapons() -> List[str]:
        return [
            "AK-74",
            "AMES 85",
            "AS VAL",
            "Goblin MK2",
            "GPR 91",
            "Model L",
            "XM4",
            "C9",
            "Jackal PDW",
            "Kompakt 92",
            "KSV",
            "PP-919",
            "Tanto .22",
            "ASG-89",
            "Marine SP",
            "GPMG-7",
            "PU-21",
            "XMG",
            "AEK-973",
            "DM-10",
            "SWAT 5.56",
            "Tsarkov 7.62",
            "LR 7.62",
            "LW3A1 Frostline",
            "SVD",
            "9mm PM",
            "Grekhova",
            "GS45",
            "Stryder .22",
            "Cigma 2B",
            "HE-1",
            "Knife",
            "Baseball Bat",
        ]

    @staticmethod
    def dlc_weapons() -> List[str]:
        return [
            "AMR Mod 4",
            "Cleaver",
            "Krig C",
            "Maelstrom",
            "Power Drill",
            "Saug",
            "Sirin 9mm",
            "Bo Staff",
            "Cypher 091",
            "D1.3 Sector",
            "Feng 82",
            "Katanas",
            "Nunchaku",
            "PPSh-41",
            "Sai",
            "Skateboard",
            "TR2",
            "CR-56 AMAX",
            "HDR",
            "Kali Sticks",
            "Kilo 141",
            "Ladra",
            "Nail Gun",
            "Essex Model 07",
            "FFAR 1",
            "LC10",
            "Olympia",
            "Pickaxe",
            "ABR A1",
            "Boxing Gloves",
            "Gravemark .357 Revolver",
            "PML 5.56",
            "Chainsaw",
            "Dresden 9mm",
            "Merrick 556",
        ]

    @staticmethod
    def methods_multiplayer() -> List[str]:
        return [
            "critical",
            "melee",
            "equipment",
            "explosive",
            "objective",
            "Scorestreak",
        ]

    @staticmethod
    def methods_zombies() -> List[str]:
        return [
            "critical",
            "melee",
            "equipment",
            "explosive",
            "Scorestreak",
            "trap",
        ]

    @staticmethod
    def scorestreaks_easy() -> List[str]:
        return [
            "Scout Pulse",
            "RC-XD",
            "Combat Bow",
            "SAM Turret",
            "UAV",
            "Archangel Launcher",
            "Counter UAV"
            "Care Package",
            "LDBR",
            "Death Machine",
            "Napalm Strike"
            "Hand Cannon",
            "Sentry Turret",
            "Grim Reaper",
        ]

    @staticmethod
    def scorestreaks_hard() -> List[str]:
        return [
            "Hellstorm",
            "Interceptors",
            "Watchdog Helo",
            "Strategic Bomber",
            "War Machine",
            "A.G.R. Mk 1",
            "HARP",
            "Chopper Gunner",
            "Dreadnought"
        ]

    @staticmethod
    def field_upgrades_multiplayer() -> List[str]:
        return [
            "Assault Pack",
            "Spring Mine",
            "Trophy System",
            "Scrambler",
            "Signal Lure",
            "War Cry",
            "Tactical Insertion",
            "Acoustic Amp",
            "Morphine Injector",
            "Neurogas",
            "Sleeper Agent",
        ]

    @staticmethod
    def field_upgrades_zombies() -> List[str]:
        return [
            "Dark Flare",
            "Energy Mine",
            "Frenzied Guard",
            "Healing Aura",
            "Aether Shroud",
            "Mister Peeks",
            "Tesla Storm",
            "Frost Blast",
        ]

    @staticmethod
    def rounds() -> List[str]:
        return [
            "11",
            "16",
            "21",
            "26",
            "31",
        ]

    @staticmethod
    def maps_zombies() -> List[str]:
        return [
            "Liberty Falls",
            "Terminus",
            "Citadelle des Morts",
            "The Tomb",
            "Shattered Veil",
            "Reckoning",
        ]

    @staticmethod
    def challenges() -> List[str]:
        return [
            "using no GobbleGums",
            "not increasing a weapons' rarity",
            "not buying any perks",
            "not being downed",
            "using only melee",
            "not using the Pack-A-Punch",
            "not upgrading your armor",
            "not using equipment",
        ]

    @staticmethod
    def wonder_weapons() -> List[str]:
        return [
            "Ray Gun",
            "Ray Gun Mark II",
            "Thrustodyne M23",
            "Balmung",
            "Caliburn",
            "Durendal",
            "Solais",
            "Staff of Ice",
            "Wunderwaffe DG-2",
            "Gorgofex",
            "DRI-11 Beamsmasher",
        ]

    @staticmethod
    def elite_zombies() -> List[str]:
        return [
            "Mangler",
            "Doppelghast",
            "Shock Mimic",
            "Amalgam",
            "Abomination",
        ]
        
    @staticmethod
    def maps_multiplayer() -> List[str]:
        return [
            "Babylon",
            "Barrage",
            "Bounty",
            "Dealership",
            "Derelict",
            "Extraction",
            "Firing Range",
            "Fringe",
            "Fugitive",
            "Gravity",
            "Grind",
            "Hacienda",
            "Haven",
            "Hideout",
            "Jackpot",
            "Lowtown",
            "Nuketown",
            "Payback",
            "Protocol",
            "Red Card",
            "Rewind",
            "Rig",
            "Runway",
            "SCUD",
            "Shutdown",
            "Skyline",
            "Subsonic",
            "Vault",
            "Vorkuta",
            "WMD",
        ]

# Archipelago Options
class CallOfDutyBlackOps6EnableMultiplayer(DefaultOnToggle):
    """
    If true, enables Multiplayer objectives.
    """
    display_name = "Call of Duty: Black Ops 6 - Enable Multiplayer"


class CallOfDutyBlackOps6EnableZombies(DefaultOnToggle):
    """
    If true, enables Zombies objectives.
    """
    display_name = "Call of Duty: Black Ops 6 - Enable Zombies"


class CallOfDutyBlackOps6IncludePostLaunchWeapons(Toggle):
    """
    If true, enables objectives involving post-launch weapons.
    """
    display_name = "Call of Duty: Black Ops 6 - Include Post-Launch Weapons"


class CallOfDutyBlackOps6IncludePartyGames(DefaultOnToggle):
    """
    If true, enables objectives involving Party Game modes.
    """
    display_name = "Call of Duty: Black Ops 6 - Include Party Games"
