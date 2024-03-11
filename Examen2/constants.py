import actions, messages

MAIN_MENU = [
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
