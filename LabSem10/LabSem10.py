from typing import List


def factN_rec(x: int, n: int = 1) -> int:
    assert x >= 0 and n > 0

    if 0 <= x and x < n:
        return 1

    return x * factN_rec(x - n, n)


def factN_iter(x: int, n: int = 1) -> int:
    assert x >= 0 and n > 0

    result: int = 1

    if 0 <= x and x < n:
        return result

    for i in range(x, 1, -n):
        result *= i

    return result


def fusc_rec(n: int) -> int:
    assert n >= 0

    if n in [0, 1]:
        return n
    if n % 2 == 0:
        return fusc_rec(n / 2)

    return fusc_rec((n - 1) / 2) + fusc_rec(
        (n + 1) / 2  # (n - 1) / 2 + 1 = (n + 1) / 2
    )


def potencia_rec(n: int, m: int) -> int:
    assert m >= 0

    if m == 0:
        return 1

    if m % 2 == 0:
        return potencia_rec(n * n, m // 2)

    if m % 2 == 1:
        return n * potencia_rec(n, m - 1)


def potencia_iter(n: int, m: int) -> int:
    assert m >= 0

    result = 1

    if m == 0:
        return result

    for _ in range(m):
        result *= n

    return result


def mcd_rec(n: int, m: int) -> int:
    assert n > 0 and m > 0, "Introduzca solo enteros positivos"

    if n == m:
        return n

    if n > m:
        return mcd_rec(n - m, m)

    return mcd_rec(n, m - n)


def mcd_iter(n: int, m: int) -> int:
    assert n > 0 and m > 0, "Introduzca solo enteros positivos"

    while n != m:
        if n > m:
            n -= m
        else:
            m -= n

    return n


def combinatorio_rec(n: int, k: int) -> int:
    assert n >= 0 and k >= 0, "Solo numeros naturales incluido el 0"

    if k == 0:
        return 1

    if k > n:
        return 0

    return combinatorio_rec(n - 1, k - 1) + combinatorio_rec(n - 1, k)


def stirling_rec(n: int, k: int) -> int:
    assert n >= 0 and k >= 0, "Solo numeros naturales incluido el 0"

    if k == 1 or k == n:
        return 1
    if k > n or (n > 0 and k == 0):
        return 0
    if k == n - 1:
        return combinatorio_rec(n, 2)
    if k == 2 and n > 0:
        return 2 ** (n - 1) - 1

    return stirling_rec(n - 1, k - 1) + k * stirling_rec(n - 1, k)


def ackerman_rec(m: int, n: int) -> int:
    assert m >= 0 and n >= 0, "Solo numeros naturales incluido el 0"

    if m == 0:
        return n + 1

    if n == 0:
        return ackerman_rec(m - 1, 1)

    return ackerman_rec(m - 1, ackerman_rec(m, n - 1))


def bs_rec(A: List[int], left: int, right: int, x: int) -> int:
    """
    Realiza una búsqueda binaria recursiva en una lista "ordenada"

    Args:
        A: La lista ordenada en la que se busca.
        left: El índice inicial de la búsqueda.
        right: El índice final de la búsqueda.
        x: El valor que se desea encontrar en la lista.

    Returns:
        El índice del elemento encontrado en la lista, o -1 si no se encuentra.
    """
    assert 0 <= left and right < len(A)

    if len(A) == 0 or left > right:
        return -1

    middle = (left + right) // 2

    if left <= right and A[middle] == x:
        return middle

    if left <= right and A[middle] > x:
        return bs_rec(A, left, middle - 1, x)

    if left <= right and A[middle] < x:
        return bs_rec(A, middle + 1, right, x)
