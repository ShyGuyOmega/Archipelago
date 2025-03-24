import os
import settings
import typing
from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from .Options import KatAMOptions


class KatAMWebWorld(WebWorld):
    options_page = "https://archipelago.gg/tutorial/Kirby%20&%20The%20Amazing%20Mirror/setup/en"
    rich_text_options_doc = True
    theme = "jungle"
    bug_report_page = "https://github.com/ShyGuyOmega/KatAM-Archipelago/issues"
    tutorials = [
        Tutorial(
            tutorial_name="setup Guide",
            description="A guide to setting up the Kirby & The Amazing Mirror randomizer for Archipelago.",
            language="English",
            file_name="setup_en.md",
            link="setup/en",
            authors=["ShyGuyOmega"]
        )
    ]


class KatAMSettings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the KatAM US ROM"""

        copy_to = "Kirby & The Amazing Mirror (USA).gba"
        description = "KatAM ROM File"
        md5s = ["df5efe075b35859529ebf82a4d824458"]

    rom_file: RomFile = RomFile(RomFile.copy_to)
    rom_start: bool = True

class KatAMWorld(World):
    """
    Venture into the Mirror World with Kirby, split into four by Dark Meta Knight,
    in order to reassemble the Mirror Shards and save Dream Land.
    """

    game = "Kirby & The Amazing Mirror"
    web = KatAMWebWorld()
    options_dataclass = KatAMOptions
    options: KatAMOptions
    settings: typing.ClassVar[KatAMSettings]
