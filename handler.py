from __future__ import annotations
from typing import Sequence, Optional
from address_book import AddressBook
from note_book import NoteBook
from contact import Contact
from note import Note
from validation import Validation


def add_contact(args: Sequence[str], book: AddressBook) -> str:
    if not args:
        return "Error: Contact name is required."
    name = args[0]
    phone = args[1] if len(args) > 1 else None
    email = args[2] if len(args) > 2 else None
    address = args[3] if len(args) > 3 else None
    birthday = args[4] if len(args) > 4 else None

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
        is_email_valid = Validation.email(email)
        if is_email_valid:
            contact.email = email
        else:
            print("The email address is not valid. Example: example@gmail.com")

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
            is_phone_update = contact.edit_phone(old_phone, new_phone)
            return is_phone_update                
        case "email":
            email = args[2] if len(args) > 2 else None
            is_email_valid = Validation.email(email)
            if is_email_valid:
                contact.email = email
                return "Email updated."
            else:
                return "The email address is not valid. Example: example@gmail.com"
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


def find_contacts(args: Sequence[str], book: AddressBook) -> str:
    if not args:
        return "Error: Please provide a search query."
    query = args[0]
    return book.find_contacts(query)


def show_contact(args: Sequence[str], book: AddressBook) -> str:
    if not args:
        return "Error: Contact name is required."
    name = args[0]
    contact = book.find(name)
    if contact is None:
        return f"Contact with name {name} does not exist."
    return str(contact)


def list_contacts(args: Sequence[str], book: AddressBook) -> str:
    if not book.contacts:
        return "No contacts."
    lines = []
    for i, c in enumerate(book.contacts, 1):
        lines.append(f"{i}. {c}")
    return "\n".join(lines)


def upcoming_birthdays(args: Sequence[str], book: AddressBook) -> str:
    if not args:
        return "Error: Please provide number of days."
    try:
        days = int(args[0])
    except ValueError:
        return "Error: days must be an integer."
    items = book.get_upcoming_birthdays(days)
    if not items:
        return "No upcoming birthdays in the given range."
    lines = [f"{it['name']}: {it['congratulation_date']}" for it in items]
    return "\n".join(lines)


def _format_notes_list(notes) -> str:
    if not notes:
        return "No notes."
    lines = []
    for i, n in enumerate(notes, 1):
        lines.append(f"{i}. {n}")
    return "\n".join(lines)


def _find_note_by_id(book: NoteBook, note_id: str) -> Optional[Note]:
    return book.find_by_id(note_id)


def add_note(args: Sequence[str], note_book: NoteBook) -> str:
    if not args:
        return "Error: Note text is required."

    tags: list[str] = []
    text_parts: list[str] = []

    for a in args:
        if a.startswith("#"):
            tag_spec = a[1:]
            if not tag_spec:
                continue
            tags.extend(t.strip() for t in tag_spec.split(",") if t.strip())
        else:
            text_parts.append(a)

    joined_text = " ".join(text_parts).strip()
    if not joined_text:
        return "Error: Note text is required."

    note = Note(joined_text)
    if tags:
        note.add_tags(*tags)

    note_book.add_note(note)
    return f"Note added. Id: {note.id}"


def search_notes(args: Sequence[str], note_book: NoteBook) -> str:
    """
    note-search <query...>
    note-search --tag <tag1[,tag2,...]>
    """
    if not args:
        return "Error: Provide a search query."

    if args[0] == "--tag":
        if len(args) < 2:
            return "Error: Provide at least one tag after --tag."

        raw = ",".join(args[1:])
        tags = [t.strip() for t in raw.split(",") if t.strip()]
        if not tags:
            return "Error: Provide at least one tag after --tag."

        if hasattr(note_book, "find_notes_by_tags"):
            notes = note_book.find_notes_by_tags(tags, match_all=False)
        else:
            wanted = {t.lower() for t in tags}
            notes = []
            for n in note_book.get_all_notes():
                note_tags = set(getattr(n, "tags", []) or [])
                if note_tags.intersection(wanted):
                    notes.append(n)

        if not notes:
            return "No notes found."

        return note_book.format_notes(notes)

    query = " ".join(args).strip().lower()
    if not query:
        return "Error: Provide a search query."

    matches: list[Note] = []
    for n in note_book.get_all_notes():
        text_match = query in n.text.lower()
        tags_match = any(query in t for t in n.tags)
        if text_match or tags_match:
            matches.append(n)

    if not matches:
        return "No notes found."

    return note_book.format_notes(matches)


def edit_note(args: Sequence[str], note_book: NoteBook) -> str:
    if len(args) < 2:
        return "Usage: note-edit <note_id> <new text...> | note-edit <note_id> --tags tag1,tag2"
    note_id = args[0]
    if args[1] == "--tags":
        if len(args) < 3:
            return "Error: Provide tags."
        tags = [t.strip() for t in ",".join(args[2:]).split(",") if t.strip()]
        ok = note_book.set_note_tags(note_id, tags)
        return "Tags updated." if ok else f"Note {note_id} not found."
    else:
        new_text = " ".join(args[1:])
        ok = note_book.edit_note_text(note_id, new_text)
        return "Note updated." if ok else f"Note {note_id} not found."


def delete_note(args: Sequence[str], note_book: NoteBook) -> str:
    if not args:
        return "Error: note-delete <note_id>"
    note_id = args[0]
    ok = note_book.delete_note(note_id)
    return "Note deleted." if ok else f"Note {note_id} not found."

def list_notes(args: Sequence[str], note_book: NoteBook) -> str:
    notes = note_book.get_all_notes()
    if not notes:
        return "No notes found."
    res = f"Total notes: {len(notes)}\n\n"
    for i, note in enumerate(notes, 1):
        res += f"{i}. {note}\n"
    return res.strip()


# Tag-specific
def add_note_tags(args: Sequence[str], note_book: NoteBook) -> str:
    if len(args) < 2:
        return "Error: Usage: note-tags-add <note_id> <tag1> [tag2 ...]"
    note_id = args[0]
    tags = []
    for a in args[1:]:
        tags.extend(t.strip() for t in a.split(",") if t.strip())
    note = note_book.find_by_id(note_id)
    if note is None:
        return f"Error: Note with id '{note_id}' not found."
    note.add_tags(*tags)
    return f"Tags added. Updated note:\n{note}"


def remove_note_tags(args: Sequence[str], note_book: NoteBook) -> str:
    if len(args) < 2:
        return "Error: Usage: note-tags-remove <note_id> <tag1> [tag2 ...]"
    note_id = args[0]
    tags = []
    for a in args[1:]:
        tags.extend(t.strip() for t in a.split(",") if t.strip())
    note = note_book.find_by_id(note_id)
    if note is None:
        return f"Error: Note with id '{note_id}' not found."
    note.remove_tags(*tags)
    return f"Tags removed. Updated note:\n{note}"


def search_notes_by_tags(args: Sequence[str], note_book: NoteBook) -> str:
    if not args:
        return "Error: Usage: note-tags-search [--all] <tag1> [tag2 ...]"
    match_all = False
    raw = list(args)
    if "--all" in raw:
        match_all = True
        raw = [a for a in raw if a != "--all"]
    if not raw:
        return "Error: Provide at least one tag."
    tags = []
    for a in raw:
        tags.extend(t.strip() for t in a.split(",") if t.strip())
    notes = note_book.find_notes_by_tags(tags, match_all=match_all)
    if not notes:
        return "No notes found by given tags."
    return note_book.format_notes(notes)


def help_command(args: Sequence[str], book: AddressBook) -> str:
    """
    Return a short description of available commands and argument formats.
    args: []
    """
    return """
Available commands:
- add <name> [phone] [email] [address] [birthday]: Add or update a contact. Example: add John +1234567890 john@example.com Kyiv 01.01.1990
- edit <name> <field> <old_value> <new_value>: Edit a contact field. Example: edit John phone +1234567890 +0987654321
- delete <name>: Delete a contact. Example: delete John
- find <query>: Search contacts by substring. Example: find John
- show <name>: Show contact details. Example: show John
- list: List all contacts. Example: list
- upcoming <days>: Contacts with birthdays in N days. Example: upcoming 7
- add_note <text>: Add a note. Example: add_note Buy bread
- search_notes <query>: Search notes. Example: search_notes bread
- edit_note <id> <new_text>: Edit a note. Example: edit_note 1 New text
- delete_note <id>: Delete a note. Example: delete_note 1
- list_notes: List all notes. Example: list_notes
- help: Show this help. Example: help
- exit: Exit the program. Example: exit
"""