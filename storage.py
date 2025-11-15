# storage.py
from __future__ import annotations

import pickle
import os
from typing import TypeVar, Type
from address_book import AddressBook
from note_book import NoteBook

T = TypeVar('T', AddressBook, NoteBook)


class Serializer:

    def __init__(self, file_path, default_class: Type[T]):
        self.file_path = file_path
        self.default_class = default_class
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    def exists(self):
        return os.path.exists(self.file_path)
    
    def save(self, obj: T) -> None:
        try:
            with open(self.file_path, 'wb') as f:
                pickle.dump(obj, f)
        except Exception as e:
            obj_type = "address book" if isinstance(obj, AddressBook) else "notes"
            print(f"Error serializing {obj_type}: {e}")
  
    def load(self) -> T:
        try:
            with open(self.file_path, 'rb') as f:
                obj = pickle.load(f)
                
                if isinstance(obj, AddressBook) and hasattr(obj, 'notes'):
                    if obj.notes:
                        obj.notes = []
                
                return obj
                
        except Exception as e:
            obj_type = "address book" if self.default_class == AddressBook else "notes"
            print(f"Error deserializing {obj_type}: {e}")

            return self.default_class()
