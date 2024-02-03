
import subprocess
from typing import List, Tuple


def test_problem_1() -> float:
    """
    Casos de prueba para el problema 1 (VolumenAreaCubo.py).

    Retorna:
        Puntaje obtenido en el problema.
    """
    print(f"Running \033[1mVolumenAreaCubo.py\033[0m...")

    result: int = 0
    test_cases: List[Tuple[str, str]] = [
        ("2", "8.0 24.0"),
        ("5", "125.0 150.0"),
        ("42.5", "76765.625 10837.5"),
        ("0", "0.0 0.0"),
        ("-0.00001", "El número debe ser no negativo.")
    ]

    for test in test_cases:
        process = subprocess.run(
            ["python3", "VolumenAreaCubo.py"],
            input=test[0],
            text=True,
            capture_output=True
        )

        output: str = process.stdout.split("\n")[-2].strip()
        test_result: bool = output == test[1]

        if test_result:
            print(
                f"\033[1;36m**\033[0m Caso de prueba correcto: {test[0]} -> {test[1]}")
            result += 1
        else:
            print(
                f"\033[1;31m**\033[0m Caso de prueba incorrecto: {test[0]} -> {test[1]}")
            print(f"Output: {output}")
            if process.stderr:
                print(f"Error: {process.stderr.strip()}")

    print(f"---\n{result}/{len(test_cases)} Casos de prueba correctos.\n")

    return result / len(test_cases)


def test_problem_2() -> float:
    """
    Casos de prueba para el problema 2 (DentroDelCirculo.py).

    Parámetros:
        script: Nombre del script a probar.

    Retorna:
        Puntaje obtenido en el problema.
    """
    print(f"Running \033[1mDentroDelCirculo.py\033[0m...")

    result: int = 0
    test_cases: List[Tuple[str, str]] = [
        ("2\n1\n1", "True"),
        ("5\n3\n4", "True"),
        ("5\n-3\n-4", "True"),
        ("5\n3\n4.00001", "False"),
        ("5\n5\n5", "False"),
        ("5\n-5\n-5", "False"),
        ("-1\n0\n0", "El radio del círculo debe ser no negativo."),
    ]

    for test in test_cases:
        process = subprocess.run(
            ["python3", "DentroDelCirculo.py"],
            input=test[0],
            text=True,
            capture_output=True
        )

        output: str = process.stdout.split("\n")[-2].strip()
        test_result: bool = output == test[1]

        if test_result:
            print(
                f"\033[1;36m**\033[0m Caso de prueba correcto: {test[0]} -> {test[1]}")
            result += 1
        else:
            print(
                f"\033[1;31m**\033[0m Caso de prueba incorrecto: {test[0]} -> {test[1]}")
            print(f"Output: {output}")
            if process.stderr:
                print(f"Error: {process.stderr.strip()}")

    print(f"---\n{result}/{len(test_cases)} Casos de prueba correctos.\n")

    return result / len(test_cases)


def test_problem_3() -> float:
    """
    Casos de prueba para el problema 3 (EsBisiesto.py).

    Parámetros:
        script: Nombre del script a probar.

    Retorna:
        Puntaje obtenido en el problema.
    """
    print(f"Running \033[1mEsBisiesto.py\033[0m...")

    result: int = 0
    test_cases: List[Tuple[str, str]] = [
        ("2016", "True"),
        ("2019", "False"),
        ("2000", "True"),
        ("1900", "False"),
        ("2200", "False"),
        ("1200", "El año debe estar en el rango [1900, 2200]."),
        ("1899", "El año debe estar en el rango [1900, 2200]."),
        ("2201", "El año debe estar en el rango [1900, 2200]."),
        ("2401", "El año debe estar en el rango [1900, 2200]."),
    ]

    for test in test_cases:
        process = subprocess.run(
            ["python3", "EsBisiesto.py"],
            input=test[0],
            text=True,
            capture_output=True
        )

        output: str = process.stdout.split("\n")[-2].strip()
        test_result: bool = output == test[1]

        if test_result:
            print(
                f"\033[1;36m**\033[0m Caso de prueba correcto: {test[0]} -> {test[1]}")
            result += 1
        else:
            print(
                f"\033[1;31m**\033[0m Caso de prueba incorrecto: {test[0]} -> {test[1]}")
            print(f"Output: {output}")
            if process.stderr:
                print(f"Error: {process.stderr.strip()}")

    print(f"---\n{result}/{len(test_cases)} Casos de prueba correctos.\n")

    return result / len(test_cases)


def test_problem_4() -> float:
    """
    Casos de prueba para el problema 4 (EsCuadradoPerfecto.py).

    Parámetros:
        script: Nombre del script a probar.

    Retorna:
        Puntaje obtenido en el problema.
    """
    print(f"Running \033[1mEsCuadradoPerfecto.py\033[0m...")

    result: int = 0
    test_cases: List[Tuple[str, str]] = [
        ("529", "True"),
        ("1", "True"),
        ("0", "True"),
        ("17", "False"),
        ("19", "False"),
        ("-1", "El número debe ser no negativo."),
    ]

    for test in test_cases:
        process = subprocess.run(
            ["python3", "EsCuadradoPerfecto.py"],
            input=test[0],
            text=True,
            capture_output=True
        )

        output: str = process.stdout.split("\n")[-2].strip()
        test_result: bool = output == test[1]

        if test_result:
            print(
                f"\033[1;36m**\033[0m Caso de prueba correcto: {test[0]} -> {test[1]}")
            result += 1
        else:
            print(
                f"\033[1;31m**\033[0m Caso de prueba incorrecto: {test[0]} -> {test[1]}")
            print(f"Output: {output}")
            if process.stderr:
                print(f"Error: {process.stderr.strip()}")

    print(f"---\n{result}/{len(test_cases)} Casos de prueba correctos.\n")

    return result / len(test_cases)


def test_problem_5() -> float:
    """
    Casos de prueba para el problema 5 (SonNumerosCoprimos.py).

    Parámetros:
        script: Nombre del script a probar.

    Retorna:
        Puntaje obtenido en el problema.
    """
    print(f"Running \033[1mSonNumerosCoprimos.py\033[0m...")

    result: int = 0
    test_cases: List[Tuple[str, str]] = [
        ("90\n77", "True"),
        ("1\n1", "True"),
        ("48\n180", "False"),
        ("3125\n4096", "True"),
        ("23625\n39468", "False"),
        ("0\n0", "Ambos números deben ser positivos."),
        ("5\n-1", "Ambos números deben ser positivos."),
        ("-1\n5", "Ambos números deben ser positivos.")
    ]

    for test in test_cases:
        process = subprocess.run(
            ["python3", "SonNumerosCoprimos.py"],
            input=test[0],
            text=True,
            capture_output=True
        )

        output: str = process.stdout.split("\n")[-2].strip()
        test_result: bool = output == test[1]

        if test_result:
            print(
                f"\033[1;36m**\033[0m Caso de prueba correcto: {test[0]} -> {test[1]}")
            result += 1
        else:
            print(
                f"\033[1;31m**\033[0m Caso de prueba incorrecto: {test[0]} -> {test[1]}")
            print(f"Output: {output}")
            if process.stderr:
                print(f"Error: {process.stderr.strip()}")

    print(f"---\n{result}/{len(test_cases)} Casos de prueba correctos.\n")

    return result / len(test_cases)


def main():
    """
    Función principal.
    """
    print("Corriendo tests...")

    result: float = 0.0
    result += test_problem_1()
    result += test_problem_2()
    result += test_problem_3()
    result += test_problem_4()
    result += test_problem_5()

    print(f"---\n{result}/5.0 Puntaje total.")


if __name__ == "__main__":
    main()