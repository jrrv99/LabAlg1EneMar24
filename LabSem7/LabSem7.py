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

    result = set_1 + [number for number in set_2 if number not in set_1]

    if swap:
        set_1.clear()
        set_1.extend(result)

    return result


def interseccion(set_1: SetType, set_2: SetType, swap: bool = False) -> SetType:
    assert es_conjunto(set_1) and es_conjunto(set_2)

    result = [number for number in set_1 if number in set_2]

    if swap:
        set_1.clear()
        set_1.extend(result)

    return result


def diferencia(set_1: SetType, set_2: SetType, swap: bool = False) -> SetType:
    assert es_conjunto(set_1) and es_conjunto(set_2)

    result = [number for number in set_1 if number not in set_2]

    if swap:
        set_1.clear()
        set_1.extend(result)

    return result
