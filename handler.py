from typing import Sequence
from address_book import AddressBook
from contact import Contact

def add_contact(args: Sequence[str], book: AddressBook):
    if not args:
        return "Error: Contact name is required."
    
    name = args[0]
    phone = args[1] if len(args) > 1 else None
    email = args[2] if len(args) > 2 else None
    address = args[3] if len(args) > 3 else None
    birthday = args[4] if len(args) > 4 else None
    
    # Find existing contact or create new one
    contact = book.find(name)
    if contact is None:
        contact = Contact(name)
        book.add_record(contact)
        message = "Contact added."
    else:
        message = "Contact updated."

    if phone:
        try:
            contact.add_phone(phone)
        except ValueError as e:
            return str(e)
    
    if email:
        # Basic email validation
        if "@" not in email or "." not in email.split("@")[1]:
            return "Error: Invalid email format."
        contact.email = email

    if address:
        contact.address = address
    
    if birthday:
        try:
            contact.add_birthday(birthday)
        except ValueError as e:
            return str(e)
    
    return message


def edit_contact(args: Sequence[str], book: AddressBook):
    """
    Редагувати контакт.
    args приклади:
      - змінити телефон:   [name, "phone", old_phone, new_phone]
      - змінити email:     [name, "email", new_email]
      - змінити адресу:    [name, "address", new_address]
      - змінити birthday:  [name, "birthday", DD.MM.YYYY]
    """
    pass


def delete_contact(args: Sequence[str], book: AddressBook):
    """
    Видалити контакт повністю або окреме поле.
    args приклади:
      - видалити контакт:  [name]
      - видалити телефон:  [name, "phone", phone]
      - видалити email:    [name, "email"]
      - видалити address:  [name, "address"]
      - видалити birthday: [name, "birthday"]
    """
    pass


def find_contacts(args: Sequence[str], book: AddressBook):
    """
    Пошук контактів за підрядком у name/phone/email/address.
    args: [query]
    """
    pass


def show_contact(args: Sequence[str], book: AddressBook):
    """
    Показати деталі конкретного контакту.
    args: [name]
    """
    pass


def list_contacts(args: Sequence[str], book: AddressBook):
    """
    Вивести всі контакти у зручному форматі (пагінація опціонально).
    args: []
    """
    pass


def upcoming_birthdays(args: Sequence[str], book: AddressBook):
    """
    Вивести контакти, у яких ДН через вказану кількість днів від сьогодні.
    args: [days:int]
    """
    pass


# =========================
# VALIDATION (опційні командні хендлери)
# =========================

def validate_phone(args: Sequence[str], book: AddressBook):
    """
    Перевірити валідність телефону (10 цифр або ваш формат).
    args: [phone]
    Повернути повідомлення про валідність.
    """
    pass


def validate_email(args: Sequence[str], book: AddressBook):
    """
    Перевірити валідність email.
    args: [email]
    Повернути повідомлення про валідність.
    """
    pass


# =========================
# NOTES
# =========================

def add_note(args: Sequence[str], book: AddressBook):
    """
    Додати нотатку.
    args приклади:
      - простий текст:         [text...]
      - з тегами (за бажання): ["--tags", "tag1,tag2", text...]
    """
    pass


def search_notes(args: Sequence[str], book: AddressBook):
    """
    Пошук нотаток за підрядком у тексті або за тегами.
    args приклади:
      - за текстом: [query]
      - за тегами:  ["--tags", "tag1,tag2"]
    """
    pass


def edit_note(args: Sequence[str], book: AddressBook):
    """
    Редагувати нотатку за ідентифікатором або іншим ключем.
    args приклади:
      - за id: [note_id, new_text...]
      - зміна тегів: [note_id, "--tags", "tag1,tag2"]
    """
    pass


def delete_note(args: Sequence[str], book: AddressBook):
    """
    Видалити нотатку.
    args: [note_id]
    """
    pass


def list_notes(args: Sequence[str], book: AddressBook):
    """
    Вивести список нотаток (опціонально з фільтрами/пагінацією).
    args: []
    """
    pass


# =========================
# HELP / SERVICE
# =========================

def help_command(args: Sequence[str], book: AddressBook):
    """
    Повернути короткий опис доступних команд і формат аргументів.
    args: []
    """
    pass
