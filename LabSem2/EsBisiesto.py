MIN_YEAR_INPUT: int = 1900
MAX_YEAR_INPUT: int = 2200
YEAR_INPUT_MESSAGE: str = "Indique el año: \n"
YEAR_RANGE_ERROR_MESSAGE: str = f"El año debe estar en el rango [{MIN_YEAR_INPUT}, {MAX_YEAR_INPUT}]."


def main() -> None:
	year: int = int(input(YEAR_INPUT_MESSAGE))

	if MIN_YEAR_INPUT > year or year > MAX_YEAR_INPUT:
		print(YEAR_RANGE_ERROR_MESSAGE)
		return
	
	print(year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0))


if __name__ == "__main__":
	main()