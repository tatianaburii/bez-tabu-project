from typing import Optional, Sequence
from address_book import AddressBook

# =========================
# CONTACTS
# =========================

def add_contact(args: Sequence[str], book: AddressBook):
    """
    Додати контакт.
    args: [name, phone?, email?, address?, birthday? (DD.MM.YYYY)]
    - має створити новий запис або оновити існуючий (додати поля).
    - перевірити валідність phone/email/birthday.
    """
    pass


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
