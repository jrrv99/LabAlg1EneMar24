import unittest
from typing import List
import LabSem4

class TestLabSem4(unittest.TestCase):

    def test_es_subcadena(self):       
        self.assertEqual(LabSem4.es_subcadena("world", "Hello world!"), 6)
        self.assertEqual(LabSem4.es_subcadena("world?", "Hello world!"), -1)
        self.assertEqual(LabSem4.es_subcadena("world", "world Hello world!"), 0)
        self.assertEqual(LabSem4.es_subcadena("world", "Hello wworld orld!"), 7)
        self.assertEqual(LabSem4.es_subcadena("world", "world!"), 0)
    
    def test_contar_ocurrencias(self):
        self.assertEqual(LabSem4.contar_ocurrencias("world", "Hello world!"), 1)
        self.assertEqual(LabSem4.contar_ocurrencias("world?", "Hello world!"), 0)
        self.assertEqual(LabSem4.contar_ocurrencias("aa", "aaa"), 2)
    
    def test_comparar_fechas(self):
        self.assertEqual(LabSem4.comparar_fechas("05-05-2002", "01-01-2000"), True)
        self.assertEqual(LabSem4.comparar_fechas("05-05-1999", "01-01-2000"), False)
        self.assertEqual(LabSem4.comparar_fechas("01-01-2000", "01-01-2000"), False)

    def test_ordenado(self):
        self.assertEqual(LabSem4.ordenado([0, 1, 2, 3], True), True)
        self.assertEqual(LabSem4.ordenado([3, 2, 1, 0], True), False)
        self.assertEqual(LabSem4.ordenado([3, 2, 1, 0], False), True)
        self.assertEqual(LabSem4.ordenado([9, 3, 2, 1, 10], True), False)
        self.assertEqual(LabSem4.ordenado([9, 3, 2, 1, 10], False), False)
    
    def test_es_permutacion(self):
        self.assertEqual(LabSem4.es_permutacion([0, 1, 2, 3], 4), True)
        self.assertEqual(LabSem4.es_permutacion([1, 0, 2, 3], 4), True)
        self.assertEqual(LabSem4.es_permutacion([0, 0, 2, 3], 4), False)
        self.assertEqual(LabSem4.es_permutacion([1, 2, 3, 4], 4), False)
        self.assertEqual(LabSem4.es_permutacion([0, 1, 2, 3], 3), False)
    
    def test_suma_maxima(self):
        self.assertEqual(LabSem4.suma_maxima([4, -1, 4, -8, 5, 1]), 7)
        self.assertEqual(LabSem4.suma_maxima([-1, -8, 3, 2, -6, 4]), 5)
    
    def test_desviacion_estandar(self):
        self.assertEqual(LabSem4.desviacion_estandar([1, 1, 1, 1, 1, 1]), 0.0)
        self.assertEqual(LabSem4.desviacion_estandar([1, 1, 1, 2, 2, 2]), 0.5)

    def test_diferencia_matriz(self):
        matriz: List[List[float]] = [
            [1.0, 1.0, 2.0],
            [1.0, 1.0, 2.0],
            [2.0, 2.0, 2.0],
        ]

        self.assertEqual(LabSem4.diferencia_matriz(matriz, 2), -6.0)
        self.assertEqual(LabSem4.diferencia_matriz(matriz, 3), 14.0)
    
    def test_logaritmo(self):
        self.assertEqual(LabSem4.logaritmo(16), 4)
        self.assertEqual(LabSem4.logaritmo(18, 10), 1)
        self.assertEqual(LabSem4.logaritmo(1), 0)
        self.assertEqual(LabSem4.logaritmo(1, 5), 0)
        self.assertEqual(LabSem4.logaritmo(10, 10), 1)
        self.assertEqual(LabSem4.logaritmo(10, 3), 2)

    def test_cuadrado_magico(self):
        matriz1: List[List[int]] = [
            [2, 7, 6],
            [9, 5, 1],
            [4, 3, 8],
        ]
        matriz2 = [
            [2, 7, 1],
            [9, 5, 1],
            [4, 3, 8],
        ]

        self.assertEqual(LabSem4.cuadrado_magico(matriz1), True)
        self.assertEqual(LabSem4.cuadrado_magico(matriz2), False)


if __name__ == '__main__':
    unittest.main()
