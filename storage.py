# storage.py
from __future__ import annotations

import pickle
import os
from address_book import AddressBook


# поки що прибра Protocol так як серіалізуємо в pickle
class Serializer:
# серіалізація/десеріалізація адресної книги в файл
# ініціалізується з шляхом до файлу
    def __init__(self, file_path):
        self.file_path = file_path
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
    # перевірка чи існує файл
    def exists(self):
        return os.path.exists(self.file_path)
    # серіалізація
    def save(self, book: AddressBook) -> None:
        try:
            with open(self.file_path, 'wb') as f:
                pickle.dump(book, f)
        except Exception as e:
            print(f"Error serializing book: {e}")
    # десеріалізація
    def load(self) -> AddressBook:
        try:
            with open(self.file_path, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            print(f"Error deserializing book: {e}")
            return AddressBook()