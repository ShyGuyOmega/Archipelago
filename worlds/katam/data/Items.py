import typing

from BaseClasses import Item, ItemClassification


class ItemData(typing.NamedTuple):
    code: int
    itemName: str
    classification: ItemClassification
    itemID: int


class KatAMItem(Item):
    game: str = "Kirby & The Amazing Mirror"


itemList: typing.List[ItemData] = [
    ItemData(99991001, "")
]