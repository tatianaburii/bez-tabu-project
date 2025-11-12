# main.py
from pathlib import Path
from address_book import AddressBook
from router import dispatch
from storage import Serializer

def parse_input(line: str):
    parts = line.strip().split()
    return (parts[0], parts[1:]) if parts else ("", [])

def main():
    
    storage = Serializer(Path("data/address_book.pkl"))
    
   
    if storage.exists():
        try:
            book = storage.load()
            print("Address book loaded.")
        except Exception as e:
            print(f"Failed to load address book: {e}")
            book = AddressBook()
   
    else:
        book = AddressBook()


    print("Welcome to the assistant bot! Type 'help' to see commands.")
    try:
        while True:
            line = input("> ")
            command, args = parse_input(line)
            if not command:
                continue
            result = dispatch(command, args, book)
            if result == "__EXIT__":
                print("Good bye!")
                break
            if result: 
                print(result)
    finally:
        
        try:
            storage.save(book)
            print("Address book saved.")
        except Exception as e:
            print(f"Failed to save address book: {e}")
       

if __name__ == "__main__":
    main()
