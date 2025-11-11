from typing import Optional
from datetime import date

class Contact:
    def __init__(self, name):
        self.name = name
        self.phones = []
        self.address = None
        self.email = None
        self.birthday = None

    # implement getters, setters, str etc.

    def add_phone(self, phone: str) -> bool:
        # implementation
        pass

    def remove_phone(self, phone: str) -> bool:
        # implementation
        pass

    def edit_phone(self, old_phone: str, new_phone: str ) -> bool:
        # implementation
        pass

    def find_phone(self, phone: str) -> Optional[str]:
        # implementation
        pass

    def add_birthday(self, birthday: str | date) -> bool:
        # implementation
        pass

    def __str__(self) -> str:
        # implementation
        return "some string"
