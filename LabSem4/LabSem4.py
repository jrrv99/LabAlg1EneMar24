from typing import List

NOT_FOUND_RETURN_VALUE: int = -1


def es_subcadena_index(substring: str, string: str) -> int:
	first_instance_index: int = NOT_FOUND_RETURN_VALUE

	if substring not in string: return NOT_FOUND_RETURN_VALUE
	if substring == string: return 0

	for index in range(len(string)):
		if string[index] != substring[0]:
			continue
		
		first_instance_index = index
		for letter_index in range(1, len(substring)):
			if string[index + letter_index] != substring[letter_index]:
				first_instance_index = NOT_FOUND_RETURN_VALUE
				break

		if first_instance_index != NOT_FOUND_RETURN_VALUE:
			return first_instance_index
	
	return NOT_FOUND_RETURN_VALUE


def es_subcadena(substring: str, string: str) -> int:
	found: bool = False

	if substring not in string: return NOT_FOUND_RETURN_VALUE
	if substring == string: return 0

	for index in range(len(string)):
		if string[index] != substring[0]:
			continue
		
		found = True

		for letter_index in range(1, len(substring)):
			if string[index + letter_index] != substring[letter_index]:
				found = False
				break

		if found:
			return index
	
	return NOT_FOUND_RETURN_VALUE


def contar_ocurrencias(substring: str, string: str) -> int:
	if substring not in string: return 0
	if substring == string: return 1

	lastIndex: int = NOT_FOUND_RETURN_VALUE
	occurrences: int = 0
	string_aux: str = string

	while len(string_aux) >= len(substring):
		lastIndex = es_subcadena(substring, string_aux)

		if lastIndex == -1: break

		string_aux = string_aux[lastIndex + 1:]
		occurrences += 1
	
	return occurrences


def comparar_fechas(date1: str, date2: str) -> bool:
	[day1, month1, year1] = [int(string_num) for string_num in date1.split("-")]
	[day2, month2, year2] = [int(string_num) for string_num in date2.split("-")]

	if year1 < year2: return False
	if year1 > year2: return True

	if month1 < month2: return False
	if month1 > month2: return True
	
	if day1 < day2: return False
	if day1 > day2: return True

	return False # date1 = date2


def ordenado(list_: List[float], asc: bool = True) -> bool:
	for i in range(len(list_) - 1):
		if asc:
			if list_[i] > list_[i + 1]: return False
		else:
			if list_[i] < list_[i + 1]: return False
	
	return True


def count_reps(list_: List[int], num: int) -> int:
	if num not in list_: return 0
	
	count: int = 0

	for elemento in list_:
		if elemento == num: count += 1

	return count


# TODO: check list types
def es_permutacion(list_: List[int], N: int) -> bool:
    sec: List[int] = [*range(N)]  # <0, 1, 2, ..., N-1>

    if len(list_) != N: return False
    if list_ == sec: return True

    for num in list_:
        if num not in sec or count_reps(list_, num) > 1: return False

    return True


def suma_maxima(list_: List[int]) -> int:
    max_sum: int = list_[0]

    curr_sum: int = 0

    for i in range(len(list_)):
        curr_sum += list_[i]

        if curr_sum > max_sum:
            max_sum = curr_sum

        if curr_sum < 0:
            curr_sum = 0

    return max_sum


def desviacion_estandar(list_: List[float]) -> float:
	prom_u: float = sum(list_) / len(list_)
	sum_: float = sum([(Si - prom_u)**2 for Si in list_])

	return (sum_ / len(list_))**(1/2)


def diferencia_matriz(matriz: List[List[float]], N: int) -> float:
	# TODO: verify N>M
	# ? this case is not mentioned, what should be returned, 0?
	if len(matriz) == 0: return 0

	sum_n: float = 0
	sum_m: float = 0

	for row in range(len(matriz)):
		if len(matriz[row]) == 0: continue

		for column in range(len(matriz[row])):
			if row < N and column < N: sum_n += matriz[row][column]
			else: sum_m += matriz[row][column]
	
	return sum_n - sum_m


def logaritmo(r: int, b: int = 2) -> int:
	p: int = 0

	while b**p <= r:
		p += 1

	return p -1


def cuadrado_magico(matriz: List[List[int]]) -> bool:
    sum_rows: int = sum(matriz[0])
    sum_main_d: int = sum(matriz[i][i] for i in range(len(matriz)))
    sum_sec_d: int = sum(matriz[i][len(matriz) - (i + 1)] for i in range(len(matriz)))

    for row in matriz:
        if sum(row) != sum_rows:
            return False

    for col in range(len(matriz[0])):
        sum_col = sum(row[col] for row in matriz)
        if sum_col != sum_rows:
            return False


    if sum_main_d != sum_rows:
        return False

    if sum_sec_d != sum_rows:
        return False

    return True