from typing import Union, List, Tuple

from world_types import (
    GroundType,
    CityType,
    WaterType,
    MountainType,
    EmptyType,
    WorldType,
    TileType,
    WorldDimentionsType,
)
import constants, messages, actions, colors

# World Objects
GROUND: GroundType = "\033[1;32mT\033[0m"
CITY: CityType = "\033[1mC\033[0m"
WATER: WaterType = "\033[1;36mA\033[0m"
MOUNTAIN: MountainType = "\033[1;31mM\033[0m"
EMPTY: EmptyType = "\033[40m \033[0m"


def log_error(message: str):
    print(f"{colors.RED}{message}\033[0m")


def world_constructor(width: int, heigth: int, element: TileType = GROUND) -> WorldType:
    return [[element for _ in range(width)] for _ in range(heigth)]


def get_world_dimentions() -> Union[None, List[int]]:
    world_width: int
    world_height: int
    try:
        world_width = int(input(messages.WORLD_WIDTH_INPUT))
        world_height = int(input(messages.WORLD_HEIGHT_INPUT))

        if world_width < 1 or world_height < 1:
            raise ValueError("WHATEVER")
    except ValueError:
        log_error(messages.ERROR_WORLD_DIMENTIONS)
        return None

    return [world_width, world_height]


def print_menu(menu: List[Tuple[int, str]]) -> None:
    for option, message in menu:
        print(f"{colors.GREEN}{option}.\033[0m {message}")


def get_menu_option() -> int:
    print(messages.MENU_OPTION_INPUT)
    print_menu(constants.MAIN_MENU)
    option = input()

    if option not in actions.ALLOWED_ACTIONS:
        return 0

    return int(option)


# ----------------------------------------------------------------------------
# ACTIONS
# ----------------------------------------------------------------------------
def print_world(world: WorldType) -> None:
    print("\n".join([" ".join(row) for row in world]))


def main() -> None:
    world: WorldType
    world_dimentions: WorldDimentionsType = None
    action: int = 0

    while world_dimentions == None:
        world_dimentions = get_world_dimentions()

    world = world_constructor(*world_dimentions)

    while action != actions.EXIT:
        action = get_menu_option()

        if action == actions.PRINT_WORLD:
            print_world(world)
        elif action == actions.ADD_CITY:
            print(actions.ADD_CITY)
        elif action == actions.ADD_RIVER:
            print(actions.ADD_RIVER)
        elif action == actions.ADD_MOUNTAIN:
            print(actions.ADD_MOUNTAIN)
        elif action == actions.FLATTEN_AREA:
            print(actions.FLATTEN_AREA)
        elif action == actions.DELETE_AREA:
            print(actions.DELETE_AREA)
        elif action == actions.RESIZE_AREA:
            print(actions.RESIZE_AREA)
        elif action == actions.UNDO:
            print(actions.UNDO)
        elif action == actions.EXIT:
            print(actions.EXIT)
        else:
            log_error(messages.ERROR_MENU_OPTION_INPUT)


if __name__ == "__main__":
    main()
