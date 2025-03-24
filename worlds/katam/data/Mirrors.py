import typing

from BaseClasses import Entrance


class MirrorData(typing.NamedTuple):
	name: str
	givenID: int
	address: int
	type: int
	exits: str
	desc: str


mirrorList: typing.List[MirrorData] = [
	MirrorData(
		"hub_rbr2",
		1,
		88888888,
		1,
		"rbr2_rbr3",
		"First Mirror",
	),
	MirrorData(
		"hub_pep",
		1,
		0x88b4b74,
		1,
		"rbr2_rbr3",
		"First Mirror",
	),
	MirrorData(
		"rbr2_rbr3",
		2,
		88888889,
		1,
		"Exit From Rbr2",
	),
	MirrorData(

	)
]