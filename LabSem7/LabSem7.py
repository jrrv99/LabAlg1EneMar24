from typing import List

SetType = List[int]


def es_conjunto(lista: SetType) -> bool:
    items = []
    for item in lista:
        if item not in items:
            items.append(item)

    return len(lista) == len(items)


def union(set_1: SetType, set_2: SetType, swap: bool = False) -> SetType:
    assert es_conjunto(set_1) and es_conjunto(set_2)

    result: List[int] = set_1 + [number for number in set_2 if number not in set_1]

    if swap:
        set_1.clear()
        set_1.extend(result)

    return result


def interseccion(set_1: SetType, set_2: SetType, swap: bool = False) -> SetType:
    assert es_conjunto(set_1) and es_conjunto(set_2)

    result: List[int] = [number for number in set_1 if number in set_2]

    if swap:
        set_1.clear()
        set_1.extend(result)

    return result


def diferencia(set_1: SetType, set_2: SetType, swap: bool = False) -> SetType:
    assert es_conjunto(set_1) and es_conjunto(set_2)

    result: List[int] = [number for number in set_1 if number not in set_2]

    if swap:
        set_1.clear()
        set_1.extend(result)

    return result


def producto(set_1: SetType, set_2: SetType, swap: bool = False) -> SetType:
    assert es_conjunto(set_1) and es_conjunto(set_2)
    result: List[int] = []

    if len(set_2) == 0 or len(set_2) == 0:
        return result

    for a in set_1:
        for b in set_2:
            if (a * b) not in result:
                result.append(a * b)

    if swap:
        set_1.clear()
        set_1.extend(result)

    return result


def conjunto_de_sumas(set_1: SetType, swap: bool = False) -> SetType:
    assert es_conjunto(set_1)

    powerset: List[List[int]] = [[]]
    result: List[int] = []

    for i in set_1:
        powerset += [j + [i] for j in powerset]

    result = [sum(subset) for subset in powerset]

    if swap:
        set_1.clear()
        set_1.extend(result)

    return result
