from typing import Set

from world_types import (
    GroundType,
    CityType,
    WaterType,
    MountainType,
    EmptyType,
    WorldType,
    TileType,
    WorldDimentionsType,
    MenuType,
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


def get_world_dimentions() -> WorldDimentionsType:
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


def print_menu(menu: MenuType) -> None:
    for option, message in menu:
        print(f"{colors.GREEN}{option}.\033[0m {message}")


def get_menu_option(
    menu_input_message: str, menu: MenuType, allowed_options: Set[str]
) -> int:
    print(menu_input_message)
    print_menu(menu)
    option = input()

    if option not in allowed_options:
        return 0

    return int(option)


# ----------------------------------------------------------------------------
# ACTIONS
# ----------------------------------------------------------------------------
def print_world(world: WorldType) -> None:
    print("\n".join([" ".join(row) for row in world]))


def add_city(
    world: WorldType, world_dimentions: WorldDimentionsType, element: TileType = CITY
) -> WorldType:
    WORLD_WIDTH, WORLD_HEIGHT = world_dimentions
    X: int
    Y: int
    L: int

    try:
        X = int(input(messages.COORD_X_INPUT))
        Y = int(input(messages.COORD_Y_INPUT))
        L = int(input(messages.CITY_L_INPUT))

        if (0 > X or X >= WORLD_WIDTH) or (0 > Y or Y >= WORLD_HEIGHT) or (L <= 0):
            raise ValueError("INPUTS_ERROR")
    except ValueError:
        log_error(messages.ERROR_CITY_INPUTS % (WORLD_WIDTH, WORLD_HEIGHT))
        return world

    LX: int = L if X + L < WORLD_WIDTH else WORLD_WIDTH
    LY: int = L if Y + L < WORLD_HEIGHT else WORLD_HEIGHT
    for row in range(X, LX):
        for col in range(Y, LY):
            world[row][col] = element

    return world


def add_river(
    world: WorldType, world_dimentions: WorldDimentionsType, element: TileType = WATER
) -> WorldType:
    WORLD_WIDTH, WORLD_HEIGHT = world_dimentions
    X: int
    Y: int
    D: int

    try:
        X = int(input(messages.COORD_X_INPUT))
        Y = int(input(messages.COORD_Y_INPUT))
        D = get_menu_option(
            messages.RIVER_MENU_MESSAGE,
            constants.RIVER_MENU,
            constants.RIVER_MENU_ALLOWED_OPTIONS,
        )

        if (0 > X or X >= WORLD_WIDTH) or (0 > Y or Y >= WORLD_HEIGHT) or (D == 0):
            raise ValueError("INPUTS_ERROR")
    except ValueError:
        log_error(messages.ERROR_RIVER_INPUTS % (WORLD_WIDTH, WORLD_HEIGHT))
        return world

    # TODO: Refactor this with constants.RIVER_DIRECTIONS
    if D == 1:  # Vertical
        for i in range(max(0, Y - 1), min(WORLD_HEIGHT, Y + 2)):
            if 0 <= X < WORLD_WIDTH:
                world[i][X] = WATER
    elif D == 2:  # Horizontal
        for j in range(max(0, X - 1), min(WORLD_WIDTH, X + 2)):
            if 0 <= Y < WORLD_HEIGHT:
                world[Y][j] = WATER
    elif D == 3:  # Diagonal
        for k in range(3):
            new_X = X - 1 + k
            new_Y = Y - 1 + k
            if 0 <= new_X < WORLD_WIDTH and 0 <= new_Y < WORLD_HEIGHT:
                world[new_Y][new_X] = WATER
    elif D == 4:  # Diagonal inversa
        for k in range(3):
            new_X = X + 1 - k
            new_Y = Y - 1 + k
            if 0 <= new_X < WORLD_WIDTH and 0 <= new_Y < WORLD_HEIGHT:
                world[new_Y][new_X] = WATER

    return world


def main() -> None:
    world: WorldType
    world_dimentions: WorldDimentionsType = None
    action: int = 0

    while world_dimentions == None:
        world_dimentions = get_world_dimentions()

    world = world_constructor(*world_dimentions)

    while action != actions.EXIT:
        action = get_menu_option(
            messages.MENU_OPTION_INPUT, constants.MAIN_MENU, actions.ALLOWED_ACTIONS
        )

        if action == actions.PRINT_WORLD:
            print_world(world)
        elif action == actions.ADD_CITY:
            world = add_city(world, world_dimentions)
        elif action == actions.ADD_RIVER:
            world = add_river(world, world_dimentions)
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
            print(messages.EXIT_MESSAGE)
        else:
            log_error(messages.ERROR_MENU_OPTION_INPUT)


if __name__ == "__main__":
    main()