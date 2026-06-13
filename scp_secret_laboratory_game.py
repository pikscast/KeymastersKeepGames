from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle, DefaultOnToggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


# Option Dataclass
@dataclass
class SCPSecretLaboratoryArchipelagoOptions:
    scp_secret_lab_play_as_scp: SCPSecretLaboratoryPlayasSCP
    scp_secret_lab_include_scp_3114: SCPSecretLaboratoryIncludeSCP3114
    scp_secret_lab_dr_brights: SCPSecretLaboratoryDrBrightsFacility

# Main Class
class SCPSecretLaboratoryeGame(Game):
    name = "SCP: Secret Laboratory"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = None

    is_adult_only_or_unrated = False

    options_cls = SCPSecretLaboratoryArchipelagoOptions

    # Optional Game Constraints
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    # Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Kill FACILITYROLE as INSURGENCYROLE",
                data={
                    "FACILITYROLE": (self.facility_roles, 1),
                    "INSURGENCYROLE": (self.insurgency_roles, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Kill INSURGENCYROLE as FACILITYROLE",
                data={
                    "INSURGENCYROLE": (self.insurgency_roles, 1),
                    "FACILITYROLE": (self.facility_roles, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Kill HUMANROLE as SCP-049-2",
                data={
                    "HUMANROLE": (self.human_roles, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Contain or support in containing SCPROLE",
                data={
                    "SCPROLE": (self.scp_roles, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Kill a player with WEAPON",
                data={
                    "WEAPON": (self.weapons, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Kill a player with SPECIALWEAPON",
                data={
                    "SPECIALWEAPON": (self.weapons_special, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Destroy a door in ZONE",
                data={
                    "ZONE": (self.zones, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Acquire KEYCARD keycard",
                data={
                    "KEYCARD": (self.keycards, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Acquire SCPITEM",
                data={
                    "SCPITEM": (self.scp_items, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Heal yourself with HEALINGITEM",
                data={
                    "HEALINGITEM": (self.healing_items, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win the game as TEAM",
                data={
                    "TEAM": (self.teams, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Escape as ESCAPEROLE",
                data={
                    "ESCAPEROLE": (self.escape_roles, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Initiate Warhead Detonation",
                data=dict(),
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
        ]
        
        if self.play_as_scp:
            objectives.append(
                GameObjectiveTemplate(
                    label="Win the game as SCPROLE",
                    data={
                        "SCPROLE": (self.scp_roles, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=1,
                ),
            )
            objectives.append(
                GameObjectiveTemplate(
                    label="Kill or assist in killing HUMANROLE as SCPROLE",
                    data={
                        "HUMANROLE": (self.human_roles, 1),
                        "SCPROLE": (self.scp_roles, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=3,
                ),
            )
            objectives.append(
                GameObjectiveTemplate(
                label="Win the game as an SCP",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
                ),
            )
            objectives.append(
                GameObjectiveTemplate(
                label="Turn off one of SCP-079's generators",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
                ),
            )
            
        if self.dr_brights:
            objectives.append(
                GameObjectiveTemplate(
                    label="Kill Serpent's Hand as HUMANROLE",
                    data={
                        "HUMANROLE": (self.human_roles, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
            )
            objectives.append(
                GameObjectiveTemplate(
                    label="Kill HUMANROLE as Serpent's Hand",
                    data={
                        "HUMANROLE": (self.human_roles, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
            )
            objectives.append(
                GameObjectiveTemplate(
                    label="Kill HUMANROLE as SCP-035",
                    data={
                        "HUMANROLE": (self.human_roles, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
            )
            objectives.append(
                GameObjectiveTemplate(
                    label="Kill SCP-035",
                    data=dict(),
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
            )
            objectives.append(
                GameObjectiveTemplate(
                    label="Win the game as Serpent's Hand",
                    data=dict(),
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=1,
                ),
            )

        return objectives

    @property
    def play_as_scp(self) -> bool:
        return bool(self.archipelago_options.scp_secret_lab_play_as_scp.value)

    @property
    def dr_brights(self) -> bool:
        return bool(self.archipelago_options.scp_secret_lab_dr_brights.value)
        
    @property
    def include_scp_3114(self) -> bool:
        return bool(self.archipelago_options.scp_secret_lab_include_scp_3114.value)

    # Datasets
    @staticmethod
    def facility_roles() -> List[str]:
        return [
            "Facility Guard",
            "MTF",
            "Scientist",
        ]
    
    @staticmethod
    def insurgency_roles() -> List[str]:
        return [
            "Chaos Insurgent",
            "Class-D",
        ]
    
    @staticmethod
    def human_roles() -> List[str]:
        return [
            "Facility Guard",
            "MTF",
            "Scientist",
            "Chaos Insurgent",
            "Class-D",
        ]
        
    @functools.cached_property
    def scp_roles_base(self) -> List[str]:
        return [
            "SCP-049",
            "SCP-049-2",
            "SCP-079",
            "SCP-096",
            "SCP-106",
            "SCP-173",
            "SCP-939",
        ]
        
    @functools.cached_property
    def scp_roles_3114(self) -> List[str]:
        return [
            "SCP-3114",
        ]
        
    def scp_roles(self) -> List[str]:
        scp_roles = self.scp_roles_base[:]
        if self.include_scp_3114:
            scp_roles.extend(self.scp_roles_3114)
        return scp_roles
    
    @staticmethod
    def weapons() -> List[str]:
        return [
            "COM-15",
            "COM-18",
            "Crossvec",
            "FR-MG-0",
            "FSP-9",
            "MTF-E11-SR",
            ".44 Revolver",
            "AK",
            "Logicer",
            "Shotgun",
            "High-Explosive Grenade",
        ]
        
    @staticmethod
    def weapons_special() -> List[str]:
        return [
            "3-X Particle Disruptor",
            "Jailbird",
            "Micro H.I.D.",
            "A7",
            "COM-45",
            "SCP-018",
            "SCP-127",
            "SCP-1509",
        ]
        
    @staticmethod
    def zones() -> List[str]:
        return [
            "Light Containment",
            "Heavy Containment",
            "Entrance",
        ]
        
    @staticmethod
    def keycards() -> List[str]:
        return [
            "Janitor",
            "Scientist",
            "Research Supervisor",
            "Containment Engineer",
            "Security Guard",
            "MTF Private",
            "MTF Operative",
            "MTF Captain",
            "Zone Manager",
            "Facility Manager",
            "O5",
            "Surface Access",
            "Chaos Insurgency",
        ]

    @staticmethod
    def scp_items() -> List[str]:
        return [
            "SCP-018",
            "SCP-127",
            "SCP-207",
            "Anti-Cola",
            "SCP-244",
            "SCP-268",
            "SCP-500",
            "SCP-1344",
            "SCP-1509",
            "SCP-1576",
            "SCP-1853",
            "SCP-2176",
        ]
        
    @staticmethod
    def healing_items() -> List[str]:
        return [
            "Adrenaline",
            "First Aid Kit",
            "Painkillers",
            "SCP-500",
        ]
        
    @staticmethod
    def teams() -> List[str]:
        return [
            "Foundation",
            "Insurgency",
        ]
        
    @staticmethod
    def escape_roles() -> List[str]:
        return [
            "Class-D",
            "Scientist",
            "Detained Class-D",
            "Detained Scientist",
        ]

# Archipelago Options
class SCPSecretLaboratoryPlayasSCP(DefaultOnToggle):
    """
    If true, enables objectives requiring playing as a SCP. 
    """

    display_name = "SCP: Secret Laboratory Play as SCP"

class SCPSecretLaboratoryIncludeSCP3114(Toggle):
    """
    If true, enables objectives related to SCP-3114. SCP-3114 is normally only available during the Halloween event, but custom servers can enable it year-round.
    """

    display_name = "SCP: Secret Laboratory Include SCP-3114"
    
class SCPSecretLaboratoryDrBrightsFacility(Toggle):
    """
    If true, enable objectives using custom content on the Dr. Bright’s Facility servers.
    """

    display_name = "SCP: Secret Laboratory Dr. Bright's Facility"