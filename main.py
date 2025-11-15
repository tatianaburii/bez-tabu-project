# main.py
from pathlib import Path
from address_book import AddressBook
from note_book import NoteBook
from router import dispatch
from storage import Serializer

def parse_input(line: str):
    parts = line.strip().split()
    return (parts[0], parts[1:]) if parts else ("", [])

def main():
    
    storage_adress_book = Serializer(Path("data/address_book.pkl"), AddressBook)
    storage_notes = Serializer(Path("data/note_book.pkl"), NoteBook)
    
   
    if storage_adress_book.exists():
        try:
            book = storage_adress_book.load()
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
            storage_adress_book.save(book)
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
