from typing import Sequence
from address_book import AddressBook
from note_book import NoteBook
from contact import Contact
from note import Note
from validation import Validation


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
        contact.email = Validation.email(email)

    if address:
        contact.address = address
    
    if birthday:
        try:
            contact.add_birthday(birthday)
        except ValueError as e:
            return str(e)
    
    return message


def edit_contact(args: Sequence[str], book: AddressBook) -> str:
    if not args:
        return "Error: Contact name is required."

    name = args[0]
    field_name = args[1] if len(args) > 1 else None

    contact = book.find(name)
    if contact is None:
        return "Contact with name {} does not exist.".format(name)
    match field_name:
        case "phone":
            old_phone = args[2] if len(args) > 2 else None
            new_phone = args[3] if len(args) > 3 else None
            contact.edit_phone(old_phone, new_phone)
            return "Phone updated."
        case "email":
            email = args[2] if len(args) > 2 else None
            contact.email = Validation.email(email)
            return "Email updated."
        case "address":
            address = args[2] if len(args) > 2 else None
            contact.address = address
            return "Address updated."
        case "birthday":
            birthday = args[2] if len(args) > 2 else None
            contact.add_birthday(birthday)
            return "Birthday updated."
        case _:
            return "Contact was not updated."


def delete_contact(args: Sequence[str], book: AddressBook) -> str:
    if not args:
        return "Error: Contact name is required."
    name = args[0]
    contact = book.find(name)
    if contact in book.contacts:
        book.contacts.remove(contact)
        return "Contact deleted."
    return "Contact was not deleted."


def find_contacts(args: Sequence[str], book: AddressBook):
    """
    Пошук контактів за підрядком у name/phone/email/address.
    args: [query]
    """
    if not args:
        return "Error: Please provide a search query."
    query = args[0]
    return book.find_contacts(query)



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

def add_note(args: Sequence[str], note_book: NoteBook):
    if not args:
        return "Error: Note text is required."
    
    joined_text = " ".join(args)

    note = Note(joined_text)
    note_book.add_note(note)

    return f"Note added."


def search_notes(args: Sequence[str], note_book: NoteBook):
    """
    Пошук нотаток за підрядком у тексті або за тегами.
    args приклади:
      - за текстом: [query]
      - за тегами:  ["--tags", "tag1,tag2"]
    """
    pass

def edit_note(args: str, note_book: NoteBook):
    if not args or len(args) < 2:
        return "Error: The required arguments are missing."
    
    id, *new_text = args
    notes = note_book.get_all_notes()
    note_exist = False
    note_ind = None

    if not notes:
        return "No notes found."
    
    for note in notes:
        if note.id == id:
            note_ind = notes.index(note)
            note_exist = True
            break

    if note_exist:
        notes[note_ind].text = " ".join(new_text)
        return f"Note number {note_ind + 1} has been changed"
    else:
        return "Note not found"

def delete_note(id: str, note_book: NoteBook):
    if not id:
        return "Error: Note id is required."

    id = id[0]
    notes = note_book.get_all_notes()
    note_exist = False
    note_ind = None

    if not notes:
        return "No notes found."
    
    for note in notes:
        if note.id == id:
            note_ind = notes.index(note)
            note_exist = True
            break

    if note_exist:
        notes.pop(note_ind)
        return f"Note number {note_ind + 1} has been deleted"
    else:
        return "Note not found"

def list_notes(args: Sequence[str], note_book: NoteBook):
    notes = note_book.get_all_notes()
    
    if not notes:
        return "No notes found."
    
    result = f"Total notes: {len(notes)}\n\n"
    for i, note in enumerate(notes, 1):
        result += f"{i}. {note}\n"
    
    return result.strip()


# =========================
# HELP / SERVICE
# =========================

def help_command(args: Sequence[str], book: AddressBook):
    """
    Повернути короткий опис доступних команд і формат аргументів.
    args: []
    """
    pass
