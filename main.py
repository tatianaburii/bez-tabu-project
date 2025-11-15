# main.py
from pathlib import Path
from address_book import AddressBook
from note_book import NoteBook
from router import dispatch
from storage import Serializer
import shlex

def parse_input(line: str):
    parts = shlex.split(line.strip())
    return (parts[0], parts[1:]) if parts else ("", [])

def main():
    # Save under user's home directory to meet requirement
    base_dir = Path.home() / ".personal_assistant"
    base_dir.mkdir(parents=True, exist_ok=True)

    storage_address_book = Serializer(base_dir / "address_book.pkl", AddressBook)
    storage_notes = Serializer(base_dir / "note_book.pkl", NoteBook)

    # Load or init
    if storage_address_book.exists():
        try:
            book = storage_address_book.load()
            print("Address book loaded.")
        except Exception as e:
            print(f"Failed to load address book: {e}")
            book = AddressBook()
    else:
        book = AddressBook()

    if storage_notes.exists():
        try:
            note_book = storage_notes.load()
            print("Notes loaded.")
        except Exception as e:
            print(f"Failed to load notes: {e}")
            note_book = NoteBook()
    else:
        note_book = NoteBook()

    print("Welcome to the assistant bot! Type 'help' to see commands.")
    try:
        while True:
            line = input("> ")
            command, args = parse_input(line)
            if not command:
                continue
            result = dispatch(command, args, book, note_book)
            if result == "__EXIT__":
                print("Good bye!")
                break
            if result:
                print(result)
    finally:
        try:
            storage_address_book.save(book)
            print("Address book saved.")
        except Exception as e:
            print(f"Failed to save address book: {e}")
        try:
            storage_notes.save(note_book)
            print("Notes saved.")
        except Exception as e:
            print(f"Failed to save notes: {e}")

if __name__ == "__main__":
    main()
