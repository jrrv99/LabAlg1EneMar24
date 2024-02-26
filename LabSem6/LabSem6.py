from typing import List


def numero_de_kaprekar(num: int) -> bool:
    squared: int = num**2

    for i in range(1, len(str(squared))):
        left_part: int = squared // 10**i
        right_part: int = squared % 10**i

        if left_part + right_part == num:
            return True

    if squared == num:
        return True

    return False


def numero_de_kaprekar_str(num: int) -> bool:
    squared: int = num**2
    squared_str: str = str(squared)

    for i in range(1, len(squared_str)):
        left_part: int = int(squared_str[:i])
        right_part: int = int(squared_str[i:])

        if left_part + right_part == num:
            return True

    if squared == num:
        return True

    return False


def numero_feliz(num: int) -> bool:
    if num < 0:
        raise ValueError("El número debe ser no-negativo")

    already_squered_nums: List[int] = []

    while num != 1:
        already_squered_nums.append(num)

        num = sum([int(digit) ** 2 for digit in str(num)])

        if num in already_squered_nums:
            return False

    return True


def orderStringByUnicode(string: str) -> str:
    return "".join(sorted(list(string)))


def anagrama(string1: str, string2: str) -> bool:
    if string1 == string2:
        return False

    return orderStringByUnicode(string1) == orderStringByUnicode(string2)


def comprimir(string: str) -> str:
    if any(char.isdigit() for char in string):
        raise ValueError("El string no debe contener caracteres numéricos.")

    compressed_string = ""
    count = 1

    for i in range(len(string)):
        if i + 1 < len(string) and string[i] == string[i + 1]:
            count += 1
        else:
            compressed_string += f"{count}{string[i]}"
            count = 1

    return compressed_string
