from typing import List, Tuple, NewType

contact_list = []  # Single source of true

# Single Contact data structure [name, last_name, phone]
ContactType = List[str]
CONTACT_NAME: int = 0
CONTACT_LAST_NAME: int = 1
CONTACT_NUMBER: int = 2

EMPTY_STRING = ""
EMPTY_CONTACT: ContactType = []
INVALID_CONTACT_INDEX_VALUE: int = -1

MENU_CREATE_OPTION: str = "1"
MENU_SHOW_OPTION: str = "2"
MENU_EDIT_OPTION: str = "3"
MENU_DELETE_OPTION: str = "4"
MENU_SEARCH_OPTION: str = "5"
MENU_EXIT_OPTION: str = "6"

INVALID_NAME_ERROR_MESSAGE: str = "El nombre debe tener al menos un carácter."
INVALID_LAST_NAME_ERROR_MESSAGE: str = "El apellido debe tener al menos un carácter."
INVALID_PHONE_ERROR_MESSAGE: str = "El número de teléfono es inválido."
INVALID_CONTACT_INDEX_ERROR_MESSAGE: str = "El índice indicado es inválido."
EMPTY_CONTACT_LIST_MESSAGE: str = "No hay ningún contacto almacenado."
PHONE_NUMBER_EXISTS_MESSAGE: str = "Ya existe un contacto con ese número de teléfono."

CONTACT_CREATION_SUCCESS_MESSAGE: str = "¡Contacto creado exitosamente!"
CONTACT_EDITION_SUCCESS_MESSAGE: str = "¡Contacto editado exitosamente!"
CONTACT_DELETION_SUCCESS_MESSAGE: str = "¡Contacto eliminado exitosamente!"


def print_menu() -> None:
    print("\nIndique una opcion")
    print(f"{MENU_CREATE_OPTION}) Crear contacto")
    print(f"{MENU_SHOW_OPTION}) Mostrar contacto")
    print(f"{MENU_EDIT_OPTION}) Editar contacto")
    print(f"{MENU_DELETE_OPTION}) Eliminar contacto")
    print(f"{MENU_SEARCH_OPTION}) Buscar contacto")
    print(f"{MENU_EXIT_OPTION}) Salir")


def clean_input(value: str) -> str:
    return value.strip()


def name_validation(value: str) -> bool:
    return value.strip() != EMPTY_STRING


def phone_validation(value: str) -> bool:
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
    contact: ContactType = [
        "",
        "",
        "",
    ]
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

        if edit and contact[id] == EMPTY_STRING:
            continue

        if not validate(contact[id]):
            print(error_message)
            return EMPTY_CONTACT

    return contact


def check_contact_phone_existence(new_phone) -> bool:
    return any(new_phone == phone for _, _, phone in contact_list)


def create_contact() -> None:
    new_contact: ContactType = contact_form_input()

    if new_contact == EMPTY_CONTACT:
        return

    if check_contact_phone_existence(new_contact[CONTACT_NUMBER]):
        print(PHONE_NUMBER_EXISTS_MESSAGE)
        return

    contact_list.append(new_contact)

    print(CONTACT_CREATION_SUCCESS_MESSAGE)


def print_contact(index: int, name: str, last_name: str, phone: str):
    print(f"{index} | {name} | {last_name} | {phone}")


def show_contacts() -> None:
    print(EMPTY_STRING)  # print line

    if len(contact_list) == 0:
        print(EMPTY_CONTACT_LIST_MESSAGE)

    for index, contact in enumerate(contact_list):
        print_contact(index, *contact)


def contact_exist(index: int) -> bool:
    return index in range(len(contact_list))


def get_contact_by_index(index: int) -> ContactType:
    if not contact_exist(index):
        return EMPTY_CONTACT

    return contact_list[index]


def get_contact_index_input(input_message: str = EMPTY_STRING):
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
