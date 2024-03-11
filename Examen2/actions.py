from typing import Set

PRINT_WORLD: int = 1
ADD_CITY: int = 2
ADD_RIVER: int = 3
ADD_MOUNTAIN: int = 4
FLATTEN_AREA: int = 5
DELETE_AREA: int = 6
RESIZE_AREA: int = 7
UNDO: int = 8
EXIT: int = 9

ALLOWED_ACTIONS: Set[str] = {
    str(PRINT_WORLD),
    str(ADD_CITY),
    str(ADD_RIVER),
    str(ADD_MOUNTAIN),
    str(FLATTEN_AREA),
    str(DELETE_AREA),
    str(RESIZE_AREA),
    str(UNDO),
    str(EXIT),
}

ALLOWED_UNDO_ACTIONS: Set[str] = {
    ADD_CITY,
    ADD_RIVER,
    ADD_MOUNTAIN,
    FLATTEN_AREA,
    DELETE_AREA,
}
