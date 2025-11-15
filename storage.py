# storage.py
from __future__ import annotations

import pickle
from pathlib import Path
from typing import TypeVar, Type
from address_book import AddressBook
from note_book import NoteBook

T = TypeVar('T', AddressBook, NoteBook)


class Serializer:
    def __init__(self, file_path: Path, default_class: Type[T]):
        self.file_path: Path = Path(file_path)
        self.default_class = default_class
        # Ensure directory exists
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def exists(self) -> bool:
        return self.file_path.exists()

    def save(self, obj: T) -> None:
        with open(self.file_path, 'wb') as f:
            pickle.dump(obj, f)

    def load(self) -> T:
        try:
            with open(self.file_path, 'rb') as f:
                obj = pickle.load(f)
                # Migration guard: if old AddressBook had notes — drop them
                if isinstance(obj, AddressBook) and hasattr(obj, 'notes'):
                    try:
                        if obj.notes:
                            obj.notes = []
                    except Exception:
                        obj.notes = []
                return obj  # type: ignore[return-value]
        except Exception as e:
            obj_type = "address book" if self.default_class == AddressBook else "notes"
            print(f"Error deserializing {obj_type}: {e}")
            return self.default_class()
