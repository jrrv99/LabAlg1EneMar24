from typing import List, Tuple
import unittest

from LabSem7 import (
    es_conjunto,
    union,
    interseccion,
    diferencia,
    producto,
    conjunto_de_sumas,
)


class TestPrintMenu(unittest.TestCase):
    def tests_es_conjunto(self):
        test_cases = [([0, 7], True), ([], True), ([0, 0], False)]

        for value, expected_output in test_cases:
            self.assertEqual(es_conjunto(value), expected_output)

    def tests_union(self):
        test_cases = [([[0], [1], False], [0, 1]), ([[0], [2], True], [0, 2])]

        for (a, b, swap), expected_output in test_cases:
            if not swap:
                self.assertEqual(union(a, b, swap), expected_output)
                continue

            result = union(a, b, swap)
            self.assertEqual(result, expected_output)
            self.assertEqual(a, result)

        assertion_test_cases = [
            ([1, 1], [2, 1]),
            ([1, 2], [2, 2]),
            ([1, 1], [2, 2]),
            ([1, 1], [2, 1], True),
            ([1, 0], [2, 2], True),
            ([1, 1], [2, 2], True),
        ]
        for args in assertion_test_cases:
            with self.assertRaises(AssertionError):
                union(*args)

    def tests_interseccion(self):
        test_cases = [
            ([[0, 1, 2], [1, 3], False], [1]),
            ([[0, 1, 2], [2, 4], True], [2]),
        ]

        for (a, b, swap), expected_output in test_cases:
            if not swap:
                self.assertEqual(interseccion(a, b, swap), expected_output)
                continue

            result = interseccion(a, b, swap)
            self.assertEqual(result, expected_output)
            self.assertEqual(a, result)

        assertion_test_cases = [
            ([1, 1], [2, 1]),
            ([1, 2], [2, 2]),
            ([1, 1], [2, 2]),
            ([1, 1], [2, 1], True),
            ([1, 2], [2, 2], True),
            ([1, 1], [2, 2], True),
        ]
        for args in assertion_test_cases:
            with self.assertRaises(AssertionError):
                interseccion(*args)

    def tests_diferencia(self):
        test_cases = [
            ([[0, 1, 2], [1, 3], False], [0, 2]),
            ([[0, 1, 2], [], False], [0, 1, 2]),
            ([[], [0, 1, 2], False], []),
            ([[0, 1, 2], [2, 4], True], [0, 1]),
        ]

        for (a, b, swap), expected_output in test_cases:
            if not swap:
                self.assertEqual(diferencia(a, b, swap), expected_output)
                continue

            result = diferencia(a, b, swap)
            self.assertEqual(result, expected_output)
            self.assertEqual(a, result)

        assertion_test_cases = [
            ([1, 1], [2, 1]),
            ([1, 2], [2, 2]),
            ([1, 1], [2, 2]),
            ([1, 1], [2, 1], True),
            ([1, 2], [2, 2], True),
            ([1, 1], [2, 2], True),
        ]
        for args in assertion_test_cases:
            with self.assertRaises(AssertionError):
                diferencia(*args)

    def tests_producto(self):
        test_cases = [
            ([[0, 1], [2], False], [0, 2]),
            ([[0, 1], [2, 4], False], [0, 2, 4]),
            ([[], [2, 4], False], []),
            ([[0, 1], [], False], []),
            ([[], [], False], []),
        ]

        for (a, b, swap), expected_output in test_cases:
            if not swap:
                self.assertEqual(producto(a, b, swap), expected_output)
                continue

            result = producto(a, b, swap)
            self.assertEqual(result, expected_output)
            self.assertEqual(a, result)

        assertion_test_cases = [
            ([1, 1], [2, 1]),
            ([1, 2], [2, 2]),
            ([1, 1], [2, 2]),
            ([1, 1], [2, 1], True),
            ([1, 2], [2, 2], True),
            ([1, 1], [2, 2], True),
        ]
        for args in assertion_test_cases:
            with self.assertRaises(AssertionError):
                producto(*args)

    def tests_conjunto_de_sumas(self):
        test_cases = [
            ([[1, 2], False], [0, 1, 2, 3]),
            ([[1, 3], False], [0, 1, 3, 4]),
            ([[], False], [0]),
        ]

        for (a, swap), expected_output in test_cases:
            if not swap:
                self.assertEqual(conjunto_de_sumas(a, swap), expected_output)
                continue

            result = conjunto_de_sumas(a, swap)
            self.assertEqual(result, expected_output)
            self.assertEqual(a, result)

        assertion_test_cases = [
            [[1, 1]],
            [[1, 1], True],
        ]
        for args in assertion_test_cases:
            with self.assertRaises(AssertionError):
                conjunto_de_sumas(*args)


if __name__ == "__main__":
    unittest.main()
