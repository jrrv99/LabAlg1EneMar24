FIRST_NUM_INPUT_MESSAGE: str = "Indique el primer número: \n"
SECOND_NUM_INPUT_MESSAGE: str = "Indique el segundo número: \n"
NEGATIVE_NUMS_ERROR_MESSAGE: str = "Ambos números deben ser positivos."


def gcd(num1: int, num2: int) -> int:
	while num1 != num2:
		if num1 > num2:
			num1 -= num2
		else:
			num2 -= num1

	return num1


def main() -> None:
	num1: int = int(input(FIRST_NUM_INPUT_MESSAGE))
	num2: int = int(input(SECOND_NUM_INPUT_MESSAGE))

	if num1 <= 0 or num2 <= 0:
		print(NEGATIVE_NUMS_ERROR_MESSAGE)
		return
	
	print(gcd(num1, num2) == 1)


if __name__ == "__main__":
	main()
