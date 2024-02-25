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
