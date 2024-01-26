import math

RADIUS_INPUT_MESSAGE: str = "Indique el radio del círculo: \n"
POINT_X_INPUT_MESSAGE: str = "Indique la coordenada x del punto: \n"
POINT_Y_INPUT_MESSAGE: str = "Indique la coordenada y del punto: \n"
NEGATIVE_RADIUS_ERROR_MESSAGE: str = "El radio del círculo debe ser no negativo."


def distance_from_origin(x: float, y: float) -> float:
	return math.sqrt(x**2 + y**2)


def main() -> None:
	radius: float = float(input(RADIUS_INPUT_MESSAGE))
	point_x: float = float(input(POINT_X_INPUT_MESSAGE))
	point_y: float = float(input(POINT_Y_INPUT_MESSAGE))

	if radius < 0:
		print(NEGATIVE_RADIUS_ERROR_MESSAGE)
		return
	
	print(distance_from_origin(point_x, point_y) <= radius)

if __name__ == "__main__":
	main()