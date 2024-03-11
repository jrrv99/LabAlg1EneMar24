from typing import Literal, Union, List

GroundType = Literal["\033[1;32mT\033[0m"]
CityType = Literal["\033[1mC\033[0m"]
WaterType = Literal["\033[1;36mA\033[0m"]
MountainType = Literal["\033[1;31mM\033[0m"]
EmptyType = Literal["\033[40m \033[0m"]

TileType = Union[
    GroundType,
    CityType,
    WaterType,
    MountainType,
    EmptyType,
]

WorldType = List[List[TileType]]

WorldDimentionsType = Union[None, List[int]]
