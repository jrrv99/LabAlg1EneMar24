from typing import List, Tuple
import unittest

import LabSem6


class TestPrintMenu(unittest.TestCase):
    def test_numero_de_kaprekar(self):
        kaprekar_nums: List[int] = [
            0,
            1,
            9,
            45,
            55,
            99,
            297,
            703,
            999,
            2223,
            2728,
            4879,
            4950,
            5050,
            5292,
            7272,
            7777,
            9999,
            17344,
            22222,
            38962,
            77778,
            82656,
            95121,
            99999,
            142857,
            148149,
            181819,
            187110,
            208495,
            318682,
            329967,
            351352,
            356643,
            390313,
            461539,
            466830,
            499500,
            500500,
            533170,
        ]

        self.assertFalse(LabSem6.numero_de_kaprekar(46))
        self.assertFalse(LabSem6.numero_de_kaprekar_str(46))

        for num in kaprekar_nums:
            self.assertTrue(LabSem6.numero_de_kaprekar(num), num)
            self.assertTrue(LabSem6.numero_de_kaprekar_str(num), num)


if __name__ == "__main__":
    unittest.main()
