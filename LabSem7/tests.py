from typing import List, Tuple
import unittest

from LabSem7 import es_conjunto, union


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


if __name__ == "__main__":
    unittest.main()
