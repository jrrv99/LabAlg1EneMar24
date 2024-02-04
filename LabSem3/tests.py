import unittest

from LabSem3 import (
    buscar,
    es_primo,
    promedio,
    son_amigos,
    suma_maximo,
    es_simetrica,
    esta_ordenado,
    es_palindromo,
    sum_divs_props,
    suma_cuadrado_impares,
)


class TestLabSem3(unittest.TestCase):

    def test_es_primo(self):
        self.assertFalse(es_primo(1))
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(13))
        self.assertFalse(es_primo(20))
        self.assertTrue(es_primo(23))

    def test_suma_cuadrado_impares(self):
        self.assertEqual(suma_cuadrado_impares(1), 0)
        self.assertEqual(suma_cuadrado_impares(5), 1 + 3**2)
        self.assertEqual(suma_cuadrado_impares(10), 1 + 3**2 + 5**2 + 7**2 + 9**2)

    def test_sum_divs_props(self):
        self.assertEqual(sum_divs_props(220), 284)
        self.assertEqual(sum_divs_props(284), 220)
        self.assertEqual(sum_divs_props(1), 0)
        self.assertEqual(sum_divs_props(17), 1)
        self.assertEqual(sum_divs_props(12), 16)

    def test_son_amigos(self):
        self.assertTrue(son_amigos(220, 284))
        self.assertTrue(son_amigos(284, 220))
        self.assertFalse(son_amigos(220, 221))
        self.assertFalse(son_amigos(284, 283))

    def test_esta_ordenado(self):
        self.assertTrue(esta_ordenado([1, 2, 3, 4, 5]))
        self.assertFalse(esta_ordenado([1, 3, 2, 4, 5]))
        self.assertTrue(esta_ordenado([1]))
        self.assertTrue(esta_ordenado([]))

    def test_buscar(self):
        self.assertEqual(buscar([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(buscar([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(buscar([], 3), -1)

    def test_promedio(self):
        self.assertEqual(promedio([1, 2, 3, 4, 5]), 3)
        self.assertEqual(promedio([5]), 5)
        self.assertEqual(promedio([]), 0)

    def test_es_palindromo(self):
        self.assertTrue(es_palindromo("radar"))
        self.assertTrue(es_palindromo("madam"))
        self.assertFalse(es_palindromo("hello"))
        self.assertTrue(es_palindromo("a"))
        self.assertTrue(es_palindromo(""))

    def test_suma_maximo(self):
        matriz = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(suma_maximo(matriz), 3 + 6 + 9)

        matriz1 = [
            [1, 2, 3],
            [2, 4, 5],
            [3, 5, 6]
        ]
        self.assertEqual(suma_maximo(matriz1), 3 + 5 +  6)

    def test_es_simetrica(self):
        matriz1 = [
            [1, 2, 3],
            [2, 4, 5],
            [3, 5, 6]
        ]
        self.assertTrue(es_simetrica(matriz1))

        matriz2 = [
            [1, 2, 3],
            [2, 4, 2],
            [3, 2, 1]
        ]
        self.assertTrue(es_simetrica(matriz2))

        matriz3 = [
            [1, 2],
            [3, 4]
        ]
        self.assertFalse(es_simetrica(matriz3))


if __name__ == '__main__':
    unittest.main()