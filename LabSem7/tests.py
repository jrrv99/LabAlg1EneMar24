from typing import List, Tuple
import unittest

from LabSem7 import es_conjunto


class TestPrintMenu(unittest.TestCase):
    def tests_es_conjunto(self):
        test_cases = [([0, 7], True), ([], True), ([0, 0], False)]

        for value, expected_output in test_cases:
            self.assertEqual(es_conjunto(value), expected_output)


if __name__ == "__main__":
    unittest.main()
