from typing import List

def es_conjunto(lista: List[int]) -> bool:
    return len(lista) == len(set(lista))