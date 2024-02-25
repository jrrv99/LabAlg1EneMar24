import unittest
from unittest.mock import patch
from io import StringIO

import agenda


class TestPrintMenu(unittest.TestCase):

    @patch("sys.stdout", new_callable=StringIO)
    def test_print_menu(self, mock_stdout):
        EXPECTED_OUTPUT = "\nIndique una opcion\n1) Crear contacto\n2) Mostrar contacto\n3) Editar contacto\n4) Eliminar contacto\n5) Buscar contacto\n6) Salir\n"

        agenda.print_menu()
        self.assertEqual(mock_stdout.getvalue(), EXPECTED_OUTPUT)

    def test_name_validation(self):
        self.assertTrue(agenda.name_validation("Joe Doe"))
        self.assertTrue(agenda.name_validation("Joe "))
        self.assertFalse(agenda.name_validation(""))
        self.assertFalse(agenda.name_validation("         "))

    def test_phone_validation(self):
        self.assertFalse(agenda.phone_validation(""))
        self.assertFalse(agenda.phone_validation("00001234567"))
        self.assertFalse(agenda.phone_validation("aaaaaaaaaaa"))
        self.assertFalse(agenda.phone_validation("aaaa-aaaaaaa"))
        self.assertFalse(agenda.phone_validation("aaaa-1234567"))
        self.assertFalse(agenda.phone_validation("0000-1a34567"))
        self.assertFalse(agenda.phone_validation("00a0-1234567"))
        self.assertFalse(agenda.phone_validation("000-1234567"))
        self.assertFalse(agenda.phone_validation("0000-123456"))
        self.assertTrue(agenda.phone_validation("0000-1234567"))

    def test_contact_form_input_valid_input(self):
        cases = [
            (["John", "Doe", "1234-5678901"], ["John", "Doe", "1234-5678901"]),
            (
                ["John     ", "Doe      ", "1234-5678901 "],
                ["John", "Doe", "1234-5678901"],
            ),
        ]

        for value, expected_output in cases:
            with patch("builtins.input", side_effect=value):
                new_contact = agenda.contact_form_input()
                self.assertEqual(new_contact, expected_output)

    def test_contact_form_input_invalid_name(self):
        with patch("builtins.input", side_effect=["", "Doe", "1234-567890"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                expected_output = f"{agenda.INVALID_NAME_ERROR_MESSAGE}\n"

                new_contact = agenda.contact_form_input()
                self.assertEqual(new_contact, [])
                self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_contact_form_input_invalid_last_name(self):
        with patch("builtins.input", side_effect=["John", "", "1234-567890"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                expected_output = f"{agenda.INVALID_LAST_NAME_ERROR_MESSAGE}\n"

                new_contact = agenda.contact_form_input()
                self.assertEqual(new_contact, [])
                self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_contact_form_input_invalid_phone(self):
        with patch("builtins.input", side_effect=["John", "Doe", "1234567890"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                expected_output = f"{agenda.INVALID_PHONE_ERROR_MESSAGE}\n"

                new_contact = agenda.contact_form_input()
                self.assertEqual(new_contact, [])
                self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_edit_contact_invalid_phone(self):
        with patch("builtins.input", side_effect=["", "", "1234567890"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                expected_output = f"{agenda.INVALID_PHONE_ERROR_MESSAGE}\n"

                new_contact = agenda.contact_form_input(True)
                self.assertEqual(new_contact, [])
                self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_edit_contact_invalid_phone(self):
        with patch("builtins.input", side_effect=["", "", "1234567890"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                expected_output = f"{agenda.INVALID_PHONE_ERROR_MESSAGE}\n"

                new_contact = agenda.contact_form_input(True)
                self.assertEqual(new_contact, [])
                self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_edit_contact_valid_input(self):
        cases = [
            (["John", "Doe", "1234-5678901"], ["John", "Doe", "1234-5678901"]),
            (
                ["John ", "Doe ", "1234-5678901 "],
                ["John", "Doe", "1234-5678901"],
            ),
            (
                ["", "", ""],
                ["", "", ""],
            ),
        ]

        for value, expected_output in cases:
            with patch("builtins.input", side_effect=value):
                new_contact = agenda.contact_form_input(True)
                self.assertEqual(new_contact, expected_output)

    def test_create_contact(self):
        contacts = [
            ["John", "Doe", "1234-5678901"],
            ["Jane", "Doe", "2345-6789012"],
        ]

        succcess_expected_output = f"{agenda.CONTACT_CREATION_SUCCESS_MESSAGE}\n"
        for contact in contacts:
            with patch("builtins.input", side_effect=contact):
                with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                    agenda.create_contact()

                    if agenda.EMPTY_STRING in contact:
                        self.assertNotIn(contact, agenda.contact_list)
                        continue

                    self.assertIn(contact, agenda.contact_list)
                    self.assertEqual(mock_stdout.getvalue(), succcess_expected_output)

        invalid_contact = ["", "", ""]
        with patch("builtins.input", side_effect=invalid_contact):
            expected_output = f"{agenda.INVALID_NAME_ERROR_MESSAGE}\n"
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                agenda.create_contact()
                self.assertNotIn(invalid_contact, agenda.contact_list)
                self.assertEqual(mock_stdout.getvalue(), expected_output)

        existing_contact = ["Jhon", "Doe", "1234-5678901"]
        with patch("builtins.input", side_effect=existing_contact):
            expected_output = f"{agenda.PHONE_NUMBER_EXISTS_MESSAGE}\n"
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                agenda.create_contact()
                self.assertNotIn(existing_contact, agenda.contact_list)
                self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_show_contacts(self, mock_stdout):
        EXPECTED_OUTPUT = "".join(
            [
                f"{index} | {name} | {last_name} | {phone}\n"
                for index, (name, last_name, phone) in enumerate(agenda.contact_list)
            ]
        )

        agenda.show_contacts()
        self.assertEqual(mock_stdout.getvalue(), f"\n{EXPECTED_OUTPUT}")

    # @patch("sys.stdout", new_callable=StringIO)
    # def test_show_contacts(self, mock_stdout):



if __name__ == "__main__":
    unittest.main()
