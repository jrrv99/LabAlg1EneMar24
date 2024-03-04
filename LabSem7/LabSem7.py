from typing import List

SetType = List[int]

def es_conjunto(lista: SetType) -> bool:
    items = []
    for item in lista:
        if item not in items:
            items.append(item)

    return len(lista) == len(items)
