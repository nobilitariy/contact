import os
os.system("cls")


def print_data():
    number_book = int(input("Какую контактную книгу открыть (укажите номер):\n"
                            "1. phonebook\n"
                            "2. phonebook2\n"))
    if number_book == 1:
        with open("phonebook.txt", "r", encoding="utf-8") as file:
            phonebook_str = file.read()
            print(phonebook_str)
    else:
        with open("phonebook2.txt", "r", encoding="utf-8") as file:
            phonebook_str2 = file.read()
            print(phonebook_str2)
    print()


def input_name():
    return input("Введите имя контакта: ")


def input_surname():
    return input("Введите фамилию контакта: ")


def input_patronymic():
    return input("Введите отчество контакта: ")


def input_phone():
    return input("Введите номер телефон контакта: ")


def input_address():
    return input("Введите адрес контакта: ")


def input_data():
    name = input_name().title()
    surname = input_surname().title()
    patronymic = input_patronymic().title()
    phone = input_phone()
    address = input_address().title()
    return f"{surname} {name} {patronymic} {phone}\n{address}\n\n"


def add_contact():
    contact_str = input_data()
    with open("phonebook.txt", "a", encoding="utf-8") as file:
        file.write(contact_str)


def search_contact():
    print("Варианты поиска:\n"
          "1. По имени\n"
          "2. По отчеству\n"
          "3. По фамилии\n"
          "4. По телефону\n"
          "5. По адресу")
    command = input("Выберите вартант поиска: ")
    print()

    while command not in ("1", "2", "3", "4", "5"):
        print("Некорректный код, повторите запрос")
        command = input("Выберите вартант поиска: ")

    search = input("Введите данные для поиска: ").title()
    print()
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contacts_list = file.read().rstrip().split("\n\n")

    i_search = int(command)-1
    check_cont = False
    for contact_str in contacts_list:
        lst_contact = contact_str.replace("\n", " ").split()
        if search in lst_contact[i_search]:
            print(contact_str)
            check_cont = True
    if not check_cont:
        print("Такого контакта нет")


def copy_contact():
    with open("phonebook2.txt", "a", encoding="utf-8"):
        pass

    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contacts_list = file.read().rstrip().split("\n\n")

    contact_num = list(enumerate(map(lambda x: x.replace(
        "\n", " "), contacts_list), 1))

    for contact in contact_num:
        print(*contact)
    print()
    row = ''
    row_contact = int(input("Введите номер строки: "))
    for contact in contact_num:
        if contact[0] == row_contact:
            row = f"{contact[1]}\n\n"
    with open("phonebook2.txt", "a", encoding="utf-8") as file:
        file.write(row)
    interface()


def interface():
    with open("phonebook.txt", "a", encoding="utf-8"):
        pass
    command = ""
    os.system("cls")
    while command != "4":
        print("Меню пользователя:\n\n"
              "1. Ввывод данных на экран\n"
              "2. Добавить контакт\n"
              "3. Поиск контакта\n"
              "4. Копирование контакта\n"
              "5. Выход\n")
        command = input("Выберите пункт меню: ")
        print()

        while command not in ("1", "2", "3", "4", "5"):
            print("Некорректный код, повторите запрос")
            command = input("Выберите пункт меню: ")

        match command:
            case "1":
                print_data()
            case "2":
                add_contact()
            case "3":
                search_contact()
            case "4":
                copy_contact()
            case "5":
                print("Завершение программы")
        print()


if __name__ == "__main__":
    interface()
