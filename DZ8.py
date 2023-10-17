
# Инициализация пустого телефонного справочника (словаря)
phone_book = {}

def load_phone_book():
    """Загрузка телефонного справочника из файла."""
    try:
        with open("phone_book.txt", "r") as file:
            for line in file:
                name, phone = line.strip().split(": ")
                phone_book[name] = phone
    except FileNotFoundError:
        print("Файл телефонного справочника не найден.")

def save_phone_book():
    """Сохранение телефонного справочника в файл."""
    with open("phone_book.txt", "w") as file:
        for name, phone in phone_book.items():
            file.write(f"{name}: {phone}\n")

def add_contact(name, phone):
    """Добавление контакта в телефонный справочник."""
    phone_book[name] = phone
    print(f"Контакт {name} добавлен в телефонный справочник.")
    save_phone_book()

def update_contact(name, new_phone):
    """Обновление номера телефона контакта."""
    if name in phone_book:
        phone_book[name] = new_phone
        print(f"Номер телефона для {name} обновлен.")
        save_phone_book()
    else:
        print(f"{name} не найден в телефонной книге.")

def delete_contact(name):
    """Удаление контакта из телефонного справочника."""
    if name in phone_book:
        del phone_book[name]
        print(f"{name} удален из телефонной книги.")
        save_phone_book()
    else:
        print(f"{name} не найден в телефонной книге.")

def print_phone_book():
    """Вывод телефонного справочника."""
    if not phone_book:
        print("Телефонный справочник пуст.")
    else:
        print("Телефонный справочник:")
        for name, phone in phone_book.items():
            print(f"{name}: {phone}")

# Загрузка телефонного справочника при запуске программы
load_phone_book()

# Пример использования
add_contact("Иван", "123-456")
add_contact("Мария", "789-012")
add_contact("Петр", "345-678")

print_phone_book()

update_contact("Иван", "111-111")

delete_contact("Мария")

print_phone_book()

