
from typing import List, Tuple
from LabSem3 import (
    buscar,
    es_primo,
    promedio,
    son_amigos,
    suma_maximo,
    es_simetrica,
    esta_ordenado,
    es_palindromo,
    suma_cuadrado_impares,
)


def test_es_primo() -> float:
    """
    Casos de prueba para la función es_primo.

    ### Retorna:
        `float`: Puntaje obtenido en el problema.
    """
    print("-" * 50)
    print(f"Testing \033[1mes_primo\033[0m...")

    result: float = 0
    test_cases: List[Tuple[int, bool]] = [
        (5, True),
        (8, False),
    ]

    for test in test_cases:
        try:
            test_result: float = es_primo(test[0])

            if test_result == test[1]:
                print(f"\033[1;36m**\033[0m Caso de prueba correcto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}\n")
                result += 1
            else:
                print(f"\033[1;31m**\033[0m Caso de prueba incorrecto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}")
                print(f"Expected: {test[1]}\n")
        except:
            print(f"\033[1;31m**\033[0m Hubo un error en el caso de prueba:")
            print(f"Input: {test[0]}")
            print(f"Expected: {test[1]}\n")

    return result / len(test_cases)


def test_suma_cuadrado_impares() -> float:
    """
    Casos de prueba para la función suma_cuadrado_impares.

    ### Retorna:
        `float`: Puntaje obtenido en el problema.
    """
    print("-" * 50)
    print(f"\nTesting \033[1msuma_cuadrado_impares\033[0m...")

    result: float = 0
    test_cases: List[Tuple[int, int]] = [
        (4, 10),
        (7, 35),
    ]

    for test in test_cases:
        try:
            test_result: float = suma_cuadrado_impares(test[0])

            if test_result == test[1]:
                print(f"\033[1;36m**\033[0m Caso de prueba correcto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}\n")
                result += 1
            else:
                print(f"\033[1;31m**\033[0m Caso de prueba incorrecto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}")
                print(f"Expected: {test[1]}\n")
        except:
            print(f"\033[1;31m**\033[0m Hubo un error en el caso de prueba:")
            print(f"Input: {test[0]}")
            print(f"Expected: {test[1]}\n")

    return result / len(test_cases)


def test_son_amigos() -> float:
    """
    Casos de prueba para la función son_amigos.

    ### Retorna:
        `float`: Puntaje obtenido en el problema.
    """
    print("-" * 50)
    print(f"\nTesting \033[1mson_amigos\033[0m...")

    result: float = 0
    test_cases: List[Tuple[int, int, bool]] = [
        (16, 15, False),
        (220, 284, True),
    ]

    for test in test_cases:
        try:
            test_result: float = son_amigos(test[0], test[1])

            if test_result == test[2]:
                print(f"\033[1;36m**\033[0m Caso de prueba correcto:")
                print(f"Input: {test[0]}, {test[1]}")
                print(f"Output: {test_result}\n")
                result += 1
            else:
                print(f"\033[1;31m**\033[0m Caso de prueba incorrecto:")
                print(f"Input: {test[0]}, {test[1]}")
                print(f"Output: {test_result}")
                print(f"Expected: {test[2]}")
        except:
            print(f"\033[1;31m**\033[0m Hubo un error en el caso de prueba:")
            print(f"Input: {test[0]}, {test[1]}")
            print(f"Expected: {test[2]}")

    return result / len(test_cases)


def test_esta_ordenado() -> float:
    """
    Casos de prueba para la función esta_ordenado.

    ### Retorna:
        `float`: Puntaje obtenido en el problema.
    """
    print("-" * 50)
    print(f"\nTesting \033[1mesta_ordenado\033[0m...")

    result: float = 0
    test_cases: List[Tuple[List[float], bool]] = [
        ([0, 1, 2, 3, 4], True),
        ([4, 3, 2, 1, 0], False),
    ]

    for test in test_cases:
        try:
            test_result: float = esta_ordenado(test[0])

            if test_result == test[1]:
                print(f"\033[1;36m**\033[0m Caso de prueba correcto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}\n")
                result += 1
            else:
                print(f"\033[1;31m**\033[0m Caso de prueba incorrecto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}")
                print(f"Expected: {test[1]}\n")
        except:
            print(f"\033[1;31m**\033[0m Hubo un error en el caso de prueba:")
            print(f"Input: {test[0]}")
            print(f"Expected: {test[1]}\n")

    return result / len(test_cases)


def test_buscar() -> float:
    """
    Casos de prueba para la función buscar.

    ### Retorna:
        `float`: Puntaje obtenido en el problema.
    """
    print("-" * 50)
    print(f"\nTesting \033[1mbuscar\033[0m...")

    result: float = 0
    test_cases: List[Tuple[List[float], float, int]] = [
        ([1.0, 2.0, 3.0, 4.0], 3.0, 2),
        ([1.0, 2.0, 3.0, 4.0], 0.0, -1),
    ]

    for test in test_cases:
        try:
            test_result: float = buscar(test[0], test[1])

            if test_result == test[2]:
                print(f"\033[1;36m**\033[0m Caso de prueba correcto:")
                print(f"Input: {test[0]}, {test[1]}")
                print(f"Output: {test_result}\n")
                result += 1
            else:
                print(f"\033[1;31m**\033[0m Caso de prueba incorrecto:")
                print(f"Input: {test[0]}, {test[1]}")
                print(f"Output: {test_result}")
                print(f"Expected: {test[2]}")
        except:
            print(f"\033[1;31m**\033[0m Hubo un error en el caso de prueba:")
            print(f"Input: {test[0]}, {test[1]}")
            print(f"Expected: {test[2]}")

    return result / len(test_cases)


def test_promedio() -> float:
    """
    Casos de prueba para la función promedio.

    ### Retorna:
        `float`: Puntaje obtenido en el problema.
    """
    print("-" * 50)
    print(f"\nTesting \033[1mpromedio\033[0m...")

    result: float = 0
    test_cases: List[Tuple[List[float], float]] = [
        ([0.0, 1.0, 2.0, 3.0, 4.0, 5.0], 2.5),
        ([0.0, 5.0], 2.5),
    ]

    for test in test_cases:
        try:
            test_result: float = promedio(test[0])

            if test_result == test[1]:
                print(f"\033[1;36m**\033[0m Caso de prueba correcto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}\n")
                result += 1
            else:
                print(f"\033[1;31m**\033[0m Caso de prueba incorrecto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}")
                print(f"Expected: {test[1]}\n")
        except:
            print(f"\033[1;31m**\033[0m Hubo un error en el caso de prueba:")
            print(f"Input: {test[0]}")
            print(f"Expected: {test[1]}\n")

    return result / len(test_cases)


def test_es_palindromo() -> float:
    """
    Casos de prueba para la función es_palindromo.

    ### Retorna:
        `float`: Puntaje obtenido en el problema.
    """
    print("-" * 50)
    print(f"\nTesting \033[1mes_palindromo\033[0m...")

    result: float = 0
    test_cases: List[Tuple[str, bool]] = [
        ("aba", True),
        ("abc", False),
    ]

    for test in test_cases:
        try:
            test_result: float = es_palindromo(test[0])

            if test_result == test[1]:
                print(f"\033[1;36m**\033[0m Caso de prueba correcto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}\n")
                result += 1
            else:
                print(f"\033[1;31m**\033[0m Caso de prueba incorrecto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}")
                print(f"Expected: {test[1]}\n")
        except:
            print(f"\033[1;31m**\033[0m Hubo un error en el caso de prueba:")
            print(f"Input: {test[0]}")
            print(f"Expected: {test[1]}\n")

    return result / len(test_cases)


def test_suma_maximo() -> float:
    """
    Casos de prueba para la función suma_maximo.

    ### Retorna:
        `float`: Puntaje obtenido en el problema.
    """
    print("-" * 50)
    print(f"\nTesting \033[1msuma_maximo\033[0m...")

    result: float = 0
    test_cases: List[Tuple[List[List[int]], int]] = [
        (
            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]],
            18
        ),
    ]
    for test in test_cases:
        try:
            test_result: float = suma_maximo(test[0])

            if test_result == test[1]:
                print(f"\033[1;36m**\033[0m Caso de prueba correcto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}\n")
                result += 1
            else:
                print(f"\033[1;31m**\033[0m Caso de prueba incorrecto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}")
                print(f"Expected: {test[1]}\n")
        except:
            print(f"\033[1;31m**\033[0m Hubo un error en el caso de prueba:")
            print(f"Input: {test[0]}")
            print(f"Expected: {test[1]}\n")

    return result / len(test_cases)


def test_es_simetrica() -> float:
    """
    Casos de prueba para la función es_simetrica.

    ### Retorna:
        `float`: Puntaje obtenido en el problema.
    """
    print("-" * 50)
    print(f"\nTesting \033[1mes_simetrica\033[0m...")

    result: float = 0
    test_cases: List[Tuple[List[List[int]], bool]] = [
        (
            [[1, 0, 0],
             [0, 1, 0],
             [0, 0, 1]],
            True
        ),
        (
            [[1, 0, -1],
             [0, 1, 0],
             [0, 0, 1]],
            False
        ),
    ]

    for test in test_cases:
        try:
            test_result: float = es_simetrica(test[0])

            if test_result == test[1]:
                print(f"\033[1;36m**\033[0m Caso de prueba correcto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}\n")
                result += 1
            else:
                print(f"\033[1;31m**\033[0m Caso de prueba incorrecto:")
                print(f"Input: {test[0]}")
                print(f"Output: {test_result}")
                print(f"Expected: {test[1]}\n")
        except:
            print(f"\033[1;31m**\033[0m Hubo un error en el caso de prueba:")
            print(f"Input: {test[0]}")
            print(f"Expected: {test[1]}\n")

    return result / len(test_cases)


def main() -> None:
    """
    Función principal.
    """
    result: float = 0.0

    print("\033[1mCorriendo tests...\033[0m")
    result += test_es_primo()
    result += test_suma_cuadrado_impares()
    result += test_son_amigos()
    result += test_esta_ordenado()
    result += test_buscar()
    result += test_promedio()
    result += test_es_palindromo()
    result += test_suma_maximo()
    result += test_es_simetrica()

    print(f"---\n{result * 5 / 9}/5.0 Puntaje total.")


if __name__ == "__main__":
    main()