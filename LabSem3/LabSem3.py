from typing import List


def es_primo(num: int) -> bool:
    if num <= 1: return False

    for number in range(2, num): # [2, num)
        if num % number == 0: return False
    
    return True   


def suma_cuadrado_impares(num: int) -> int:
    sum: int = 0

    for number in range(1, num):
        if number % 2 != 0: sum += number**2

    return sum


def sum_divs_props(num: int) -> int:
    """
    Calculates the sum of proper divisors for a given number.

    Args:
        num (int): The number for which to calculate the sum of proper divisors.

    Returns:
        int: The sum of proper divisors for the given number.
    
    Example:
    ```python
    sum_divs_props(220)
    284
    sum_divs_props(284)
    220
    ```
    """
    sum: int = 0

    for i in range(1, num):
        if num % i == 0: sum += i
    
    return sum


def son_amigos(n: int, m: int) -> bool:
    return sum_divs_props(n) == m and sum_divs_props(m) == n


def esta_ordenado(numbers: List[float]) -> bool:
    for i in range(len(numbers) - 1):
        if (numbers[i] > numbers[i + 1]): return False

    return True

NOT_FOUND_RETURN_VALUE: int = -1

def buscar(numbers: List[float], num_to_find: float) -> int:
    for index in range(len(numbers)):
        if numbers[index] == num_to_find: return index

    return NOT_FOUND_RETURN_VALUE


EMPTY_LIST_RETURN_VALUE: float = 0.0

def promedio(numbers: List[float]) -> float:
    if len(numbers) == 0: return EMPTY_LIST_RETURN_VALUE

    sum: float = 0.0

    for index in range(len(numbers)): sum += numbers[index]
    
    return sum / len(numbers)


def es_palindromo(word: str) -> bool:
    for index in range(len(word) // 2):
        if word[index] != word[len(word) - (index + 1)]: return False

    return True


def suma_maximo(matriz: List[List[int]]) -> int:
    sum: int = 0
    rowMax: int

    for row in range(len(matriz)):
        if len(matriz[row]) < 0: continue
        
        rowMax = matriz[row][0]

        for column in range(1, len(matriz[row])):
            if rowMax < matriz[row][column]: rowMax = matriz[row][column]

        sum += rowMax

    return sum


def es_simetrica(matriz: List[List[int]]) -> bool:
    for row in  range(len(matriz)):
        for column in  range(len(matriz)):
            if row == column: continue
            if matriz[row][column] != matriz[column][row]: return False

    return True
