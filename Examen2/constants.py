from typing import Set, List

from world_types import MenuType, CoordType
import actions, messages

MAIN_MENU: MenuType = [
    (actions.PRINT_WORLD, messages.MENU_PRINT_WORLD_OPTION),
    (actions.ADD_CITY, messages.MENU_ADD_CITY_OPTION),
    (actions.ADD_RIVER, messages.MENU_ADD_RIVER_OPTION),
    (actions.ADD_MOUNTAIN, messages.MENU_ADD_MOUNTAIN_OPTION),
    (actions.FLATTEN_AREA, messages.MENU_FLATTEN_OPTION),
    (actions.DELETE_AREA, messages.MENU_DELETE_ZONE_OPTION),
    (actions.RESIZE_AREA, messages.MENU_REDIMENSIONAR_OPTION),
    (actions.UNDO, messages.MENU_UNDO_OPTION),
    (actions.EXIT, messages.MENU_EXIT_OPTION),
]

MOVE_DOWN: CoordType = (1, 0)  # Vertical
MOVE_RIGHT: CoordType = (0, 1)  # Horizontal
MOVE_RIGHT_UP: CoordType = (-1, 1)  # Diagonal
MOVE_RIGHT_DOWN: CoordType = (1, 1)  # Diagonal inversa

RIVER_DIRECTIONS: List[CoordType] = [
    MOVE_DOWN,
    MOVE_RIGHT,
    MOVE_RIGHT_DOWN,
    MOVE_RIGHT_UP,
]

RIVER_MENU: MenuType = [
    (1, messages.RIVER_MENU_VERTICAL),
    (2, messages.RIVER_MENU_HORIZONTAL),
    (3, messages.RIVER_MENU_DIAGONAL),
    (4, messages.RIVER_MENU_DIAGONAL_INVERSA),
]

RIVER_MENU_ALLOWED_OPTIONS: Set[str] = set(
    [str(i + 1) for i in range(len(RIVER_DIRECTIONS))]
)

DEFAULT_RIVER_WIDTH: int = 3
