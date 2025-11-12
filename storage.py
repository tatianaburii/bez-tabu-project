# storage.py
import pickle
import os
from __future__ import annotations
from typing import Any

from address_book import AddressBook


class Serializer:

    def __init__(self, file_path):
        self.file_path = file_path
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

    def exists(self):
        return os.path.exists(self.file_path)

    def save(self, book: AddressBook) -> None:
        try:
            with open(self.file_path, 'wb') as f:
                pickle.dump(book, f)
        except Exception as e:
            print(f"Error serializing book: {e}")

    def load(self) -> AddressBook:
        try:
            with open(self.file_path, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            print(f"Error deserializing book: {e}")
            return AddressBook()