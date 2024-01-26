import subprocess
from typing import List, Tuple
import argparse


def test_problem_1() -> float:
    """
    Casos de prueba para el problema 1 (VolumenAreaCubo.py).

    Retorna:
        Puntaje obtenido en el problema.
    """
    print(f"Running \033[1mVolumenAreaCubo.py\033[0m...")

    result: int = 0
    test_cases: List[Tuple[str, str]] = [
        ("1", "1.0 6.0"),
        ("-1", "El número debe ser no negativo.")
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
        ("1\n0\n0", "True"),
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
        ("2020", "True"),
        ("0", "El año debe estar en el rango [1900, 2200].")
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
        ("25", "True"),
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
        ("25\n42", "True"),
        ("0\n0", "Ambos números deben ser positivos."),
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
    functions = {
        "test_problem_1": test_problem_1, 
        "test_problem_2": test_problem_2,
        "test_problem_3": test_problem_3,
        "test_problem_4": test_problem_4,
        "test_problem_5": test_problem_5,
    }

    parser = argparse.ArgumentParser()
    parser.add_argument("--test",
                        choices=list(functions.keys()),
                        help="Función a ejecutar",
                        required=False)
    args = parser.parse_args()

    if args.test is not None:
        functions[args.test]()
    else:
        main()
