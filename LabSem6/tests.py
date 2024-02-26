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

    def test_numero_feliz(self):
        happy_nums = [
            1,
            7,
            10,
            13,
            19,
            23,
            28,
            31,
            32,
            44,
            49,
            68,
            70,
            79,
            82,
            86,
            91,
            94,
            97,
            100,
            103,
            109,
            129,
            130,
            133,
            139,
            167,
            176,
            188,
            190,
            192,
            193,
            203,
            208,
            219,
            226,
            230,
            236,
            239,
            262,
            263,
            280,
            291,
            293,
            301,
            302,
            310,
            313,
            319,
            320,
            326,
            329,
            331,
            338,
            356,
            362,
            365,
            367,
            368,
            376,
            379,
            383,
            386,
            391,
            392,
            397,
            404,
            409,
            440,
            446,
            464,
            469,
            478,
            487,
            490,
            496,
            536,
            556,
            563,
            565,
            566,
            608,
            617,
            622,
            623,
            632,
            635,
            637,
            638,
            644,
            649,
            653,
            655,
            656,
            665,
            671,
            673,
            680,
            683,
            694,
            700,
            709,
            716,
            736,
            739,
            748,
            761,
            763,
            784,
            790,
            793,
            802,
            806,
            818,
            820,
            833,
            836,
            847,
            860,
            863,
            874,
            881,
            888,
            899,
            901,
            904,
            907,
            910,
            912,
            913,
            921,
            923,
            931,
            932,
            937,
            940,
            946,
            964,
            970,
            973,
            989,
            998,
            1000,
        ]

        for num in range(1001):
            if num in happy_nums:
                self.assertTrue(LabSem6.numero_feliz(num), num)
            else:
                self.assertFalse(LabSem6.numero_feliz(num), num)

    def tests_anagrama(self):
        self.assertTrue(LabSem6.anagrama("amor", "roma"))
        self.assertFalse(LabSem6.anagrama("Toledo", "El todo"))
        self.assertFalse(LabSem6.anagrama("Hola", "Mundo"))
        self.assertFalse(LabSem6.anagrama("", "roma"))
        self.assertFalse(LabSem6.anagrama("amor", ""))
        self.assertFalse(LabSem6.anagrama("", ""))

    def test_comprimir(self):
        cases: List[Tuple[str, str]] = [
            ("aaaaabbbcccc", "5a3b4c"),
            ("ab", "1a1b"),
            ("", ""),
        ]

        for value, expected_result in cases:
            self.assertEqual(LabSem6.comprimir(value), expected_result)

    def test_puede_colocar_flores(self):
        test_cases: List[Tuple[List[List[int], int], bool]] = [
            ([[1, 0, 0, 0, 1], 1], True),
            ([[1, 0, 0, 0, 1], 0], True),
            ([[0, 0, 1, 0, 0], 2], True),
            ([[0, 1, 1, 1, 0], 0], True),
            ([[1, 0, 0, 0, 1], 2], False),
            ([[0, 1, 1, 1, 0], 2], False),  # checks list index out of range
            ([[0], 2], False),  # checks list index out of range
            ([[0], 1], True),  # checks list index out of range
            ([[1], 1], False),  # checks list index out of range
            ([[1], 0], True),  # checks list index out of range
        ]

        for case_args, expected_result in test_cases:
            self.assertEqual(
                LabSem6.puede_colocar_flores(*case_args),
                expected_result,
                f"{case_args} is not {expected_result}",
            )

        with self.assertRaises(ValueError):
            LabSem6.puede_colocar_flores([1, 0, 0, 0, 1], -1)
        with self.assertRaises(ValueError):
            LabSem6.puede_colocar_flores([2, 0, 0, 0, 1], 1)
        with self.assertRaises(ValueError):
            LabSem6.puede_colocar_flores([2, 0, 0, 0, 1], -1)

    def test_sopa_de_letras(self):
        test_cases = [
            (
                [
                    "HOLA",
                    [
                        ["a", "w", "a", "q", "s", "t"],
                        ["m", "z", "b", "a", "6", "1"],
                        ["<", "a", "H", "d", "h", "G"],
                        ["s", " ", "*", "O", "a", "$"],
                        ["a", "y", "a", "u", "L", "F"],
                        ["v", "j", ";", "@", "j", "A"],
                    ],
                ],
                True,
            ),
            (
                [
                    "HOLA",
                    [
                        ["a", "w", "a", "q", "s", "t"],
                        ["m", "z", "b", "a", "6", "1"],
                        ["<", "a", "H", "d", "h", "G"],
                        ["s", " ", "*", "8", "a", "$"],
                        ["a", "y", "a", "u", "L", "F"],
                        ["v", "j", ";", "@", "j", "A"],
                    ],
                ],
                False,
            ),
            (["HOLA", []], False),
            (["HOLA", [["H", "O", "L", "A"]]], True),
            (["HOLA", [["H", "O", "L", "@"]]], False),
        ]

        for case_args, expected_result in test_cases:
            self.assertEqual(LabSem6.sopa_de_letras(*case_args), expected_result)

        test_cases2 = [
            (
                ["HOLA", [["HHH", "O", "L", "A"]]],
                "La matriz sólo puede contener caracteres (strings de longitud 1).",
            ),
            (
                ["HOLA", [["H", "O", "L", "A"], []]],
                "La matriz debe ser M × N para algún M, N enteros.",
            ),
        ]

        for case_args, expected_result in test_cases2:
            with self.assertRaises(ValueError) as context:
                LabSem6.sopa_de_letras(*case_args)
                self.assertEqual(str(context.exception), expected_result)

    def tests_jaque(self):
        test_cases = [
            ([(0, 0), [(0, 5)], []], True),
            ([(0, 0), [(3, 3)], []], False),
            ([(0, 0), [], [(3, 3)]], True),
            ([(0, 0), [(3, 3)], [(3, 3)]], True),
        ]

        for case_args, expected_result in test_cases:
            self.assertEqual(LabSem6.jaque(*case_args), expected_result)

        raises_test_cases = [
            ([(0, 0), [], [(0, 0)]], "El rey no puede ocupar la misma posición que otra pieza."),
            ([(10, 0), [(0, 5)], []], "Todas las posiciones deben pertenecer al conjunto [0, 8) × [0, 8)."),
            ([(0, 0), [(0, 10)], []], "Todas las posiciones deben pertenecer al conjunto [0, 8) × [0, 8)."),
            ([(0, 0), [], [(3, 10)]], "Todas las posiciones deben pertenecer al conjunto [0, 8) × [0, 8)."),
        ]

        for case_args, expected_result in raises_test_cases:
            with self.assertRaises(ValueError) as context:
                LabSem6.jaque(*case_args)
                self.assertEqual(str(context.exception), expected_result)


if __name__ == "__main__":
    unittest.main()
