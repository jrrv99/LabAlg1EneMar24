import math


INPUT_MESSAGE = "Indique el número: \n"
NEGATIVE_NUMBER_ERROR_MESSAGE = "El número debe ser no negativo."


def main() -> None:
	number: int = int(input(INPUT_MESSAGE))

	if number < 0:
		print(NEGATIVE_NUMBER_ERROR_MESSAGE)
		return

	print(math.sqrt(number)**2 == number)


if __name__ == "__main__":
	main()
