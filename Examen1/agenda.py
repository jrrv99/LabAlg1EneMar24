from typing import List, Tuple, NewType

contact_list = []  # Single source of true

# Single Contact data structure [name, last_name, phone]
ContactType = List[str]
CONTACT_NAME: int = 0
CONTACT_LAST_NAME: int = 1
CONTACT_NUMBER: int = 2

# Empty values
EMPTY_STRING = ""
EMPTY_CONTACT: ContactType = []
INVALID_CONTACT_INDEX_VALUE: int = -1

# Menu option values
MENU_CREATE_OPTION: str = "1"
MENU_SHOW_OPTION: str = "2"
MENU_EDIT_OPTION: str = "3"
MENU_DELETE_OPTION: str = "4"
MENU_SEARCH_OPTION: str = "5"
MENU_EXIT_OPTION: str = "6"

# Error messages
INVALID_NAME_ERROR_MESSAGE: str = "El nombre debe tener al menos un carácter."
INVALID_LAST_NAME_ERROR_MESSAGE: str = "El apellido debe tener al menos un carácter."
INVALID_PHONE_ERROR_MESSAGE: str = "El número de teléfono es inválido."
INVALID_CONTACT_INDEX_ERROR_MESSAGE: str = "El índice indicado es inválido."
EMPTY_CONTACT_LIST_MESSAGE: str = "No hay ningún contacto almacenado."
PHONE_NUMBER_EXISTS_MESSAGE: str = "Ya existe un contacto con ese número de teléfono."

# Success messages
CONTACT_CREATION_SUCCESS_MESSAGE: str = "¡Contacto creado exitosamente!"
CONTACT_EDITION_SUCCESS_MESSAGE: str = "¡Contacto editado exitosamente!"
CONTACT_DELETION_SUCCESS_MESSAGE: str = "¡Contacto eliminado exitosamente!"


def print_menu() -> None:
    """
    prints the main menu
    """
    print("\nIndique una opcion")
    print(f"{MENU_CREATE_OPTION}) Crear contacto")
    print(f"{MENU_SHOW_OPTION}) Mostrar contacto")
    print(f"{MENU_EDIT_OPTION}) Editar contacto")
    print(f"{MENU_DELETE_OPTION}) Eliminar contacto")
    print(f"{MENU_SEARCH_OPTION}) Buscar contacto")
    print(f"{MENU_EXIT_OPTION}) Salir")


def clean_input(value: str) -> str:
    """
    Removes unnecessary spaces

    example
    ```python
    clean_input("Doe     ") # "Doe"
    """
    return value.strip()


def name_validation(value: str) -> bool:
    """
    Validates that the value is not an empty string. For name and last name mainly
    """
    return value.strip() != EMPTY_STRING


def phone_validation(value: str) -> bool:
    """
    Validates that the phone number is in the correct format (XXXX-XXXXXXX where X can only be digits).
    """
    VALID_PHONE_CODE_LENGHT: int = 4
    VALID_PHONE_NUMBER_LENGHT: int = 7

    code: str
    number: str
    phone: List[str] = value.split("-")

    if len(phone) != 2:
        return False

    code, number = phone

    return (
        len(code) == VALID_PHONE_CODE_LENGHT
        and len(number) == VALID_PHONE_NUMBER_LENGHT
        and "".join(phone).isdigit()
    )


def contact_form_input(edit: bool = False) -> ContactType:
    """
    Reads and validates the contact data either for editing or creating a new contact, if any data is wrong in the validations, it returns an empty contact.
    """
    contact: ContactType = [
        "",
        "",
        "",
    ]
    # [
    #   (
    #       position of the value in the Single Contact data structure,
    #       string to print in input,
    #       validation function,
    #       error message,
    #   )
    # ]
    inputs: List[Tuple[int, str, function, str]] = [
        (
            CONTACT_NAME,
            "\nNombre",
            name_validation,
            INVALID_NAME_ERROR_MESSAGE,
        ),
        (
            CONTACT_LAST_NAME,
            "Apellido",
            name_validation,
            INVALID_LAST_NAME_ERROR_MESSAGE,
        ),
        (
            CONTACT_NUMBER,
            "Número de Teléfono",
            phone_validation,
            INVALID_PHONE_ERROR_MESSAGE,
        ),
    ]

    for id, label, validate, error_message in inputs:
        contact[id] = clean_input(input(f"{label}: "))

        # if is editing and the the data entered is a empty string skip (Extra Activity 2.2 - Efficient editing)
        if edit and contact[id] == EMPTY_STRING:
            continue

        # if the data entered is invalid, prints the corresponding error and return a empty contact
        if not validate(contact[id]):
            print(error_message)
            return EMPTY_CONTACT

    return contact


def check_contact_phone_existence(new_phone) -> bool:
    """
    Checks if a contact with the given phone number already exists in the contact list.
    """
    return any(new_phone == phone for _, _, phone in contact_list)


def create_contact() -> None:
    """
    Creates a new contact from the data entered by the user and adds it to the contact list if it is valid or does not already exist.
    """
    new_contact: ContactType = contact_form_input()

    if new_contact == EMPTY_CONTACT:
        return

    if check_contact_phone_existence(new_contact[CONTACT_NUMBER]):
        print(PHONE_NUMBER_EXISTS_MESSAGE)
        return

    contact_list.append(new_contact)

    print(CONTACT_CREATION_SUCCESS_MESSAGE)


def print_contact(index: int, name: str, last_name: str, phone: str):
    """
    Prints the details of a contact in a formatted way.
    ## Example
    ```python
    print(0, "Joe", "Doe", "0424-0000000")
    # Outout: `0 | Joe | Doe | 0424-0000000
    """
    print(f"{index} | {name} | {last_name} | {phone}")


def show_contacts() -> None:
    """
    Displays all the contacts in the contact list.
    """
    print(EMPTY_STRING)  # print line

    if len(contact_list) == 0:
        print(EMPTY_CONTACT_LIST_MESSAGE)

    for index, contact in enumerate(contact_list):
        print_contact(index, *contact)


def contact_exist(index: int) -> bool:
    """
    Checks if a contact exists in the contact list based on the index.
    """
    return index in range(len(contact_list))


def get_contact_by_index(index: int) -> ContactType:
    """
    Retrieves the contact details based on the index provided.
    """
    if not contact_exist(index):
        return EMPTY_CONTACT

    return contact_list[index]


def get_contact_index_input(input_message: str = EMPTY_STRING):
    """
    Takes input from the user for the contact index and validates it.
    """
    contact_index: int
    try:
        contact_index = int(input(input_message))
    except ValueError:
        contact_index = INVALID_CONTACT_INDEX_VALUE

    if not contact_exist(contact_index):
        print(INVALID_CONTACT_INDEX_ERROR_MESSAGE)
        return INVALID_CONTACT_INDEX_VALUE

    return contact_index


def edit_contact() -> None:
    """
    Allows the user to edit an existing contact's information.
    """
    contact_to_edit_index: int = get_contact_index_input(
        "\n¿Cuál contacto desea modificar? "
    )

    # contact not found
    if contact_to_edit_index == INVALID_CONTACT_INDEX_VALUE:
        return

    new_contact_info: ContactType = contact_form_input(edit=True)

    # Invalid user data
    if new_contact_info == EMPTY_CONTACT:
        return

    contact: ContactType = get_contact_by_index(contact_to_edit_index)

    # if no data edited, do nothing
    if not any(
        value != EMPTY_STRING and value != contact[index]
        for index, value in enumerate(new_contact_info)
    ):
        return  # No data has been edited

    # Checking for existing number different from current contact number
    if (
        check_contact_phone_existence(new_contact_info[CONTACT_NUMBER])
        and contact[CONTACT_NUMBER] != new_contact_info[CONTACT_NUMBER]
    ):
        print(PHONE_NUMBER_EXISTS_MESSAGE)
        return

    # save edited data
    for index, value in enumerate(new_contact_info):
        if value != EMPTY_STRING:
            contact_list[contact_to_edit_index][index] = value

    print(CONTACT_EDITION_SUCCESS_MESSAGE)


def delete_contact() -> None:
    """
    Allows the user to delete an existing contact from the contact list if exists.
    """
    contact_to_delete_index: int = get_contact_index_input(
        "\n¿Cuál contacto desea eliminar? "
    )

    # contact not found
    if contact_to_delete_index == INVALID_CONTACT_INDEX_VALUE:
        return

    # delete contact
    contact_list.pop(contact_to_delete_index)

    print(CONTACT_DELETION_SUCCESS_MESSAGE)


def search_contact():
    """
    Allows the user to search for contacts based on a query and display the results if they have all the tokens passed in the query.
    """
    query: str = input("Busqueda: ")
    no_results: bool = True

    print(EMPTY_STRING)  # print line

    for index, contact in enumerate(contact_list):
        if all(token in " ".join(contact) for token in query.split(" ")):
            no_results = False
            print_contact(index, *contact)

    if no_results:
        print(f"No se encontraron coincidencias para: {query}")


def main() -> None:
    option: str = ""

    while option != MENU_EXIT_OPTION:
        print_menu()

        option = input()

        if option == MENU_CREATE_OPTION:
            create_contact()
        elif option == MENU_SHOW_OPTION:
            show_contacts()
        elif option == MENU_EDIT_OPTION:
            edit_contact()
        elif option == MENU_DELETE_OPTION:
            delete_contact()
        elif option == MENU_SEARCH_OPTION:
            search_contact()
        elif option == MENU_EXIT_OPTION:
            break
        else:
            print("Introduzca una opción correcta")


if __name__ == "__main__":
    main()
