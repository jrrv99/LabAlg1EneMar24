INPUT_MESSAGE: str = "Indique el lado del cubo: \n"
ERROR_MESSAGE: str = "El número debe ser no negativo."


def cube_volume(side: float) -> float:
    return side * side * side


def cube_surface_area(side: float) -> float:
    return 6 * side * side


def main() -> None:
    side: float = float(input(INPUT_MESSAGE))

    if side < 0:
        print(ERROR_MESSAGE)
        return

    print(cube_volume(side), cube_surface_area(side))


if __name__ == "__main__":
    main()
