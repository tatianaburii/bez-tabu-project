from contact import Contact
from typing import Optional


class AddressBook:
    def __init__(self):
        self.address_book = []  # or different data structure

    def add_record(self, record: Contact) -> bool:
        # implementation
        pass

    def find(self, name: str) -> Optional[Contact]:
        # implementation
        pass

    def delete(self, name: str) -> bool:
        # implementation
        pass

    def get_upcoming_birthdays(self, number_of_days: int) -> list[Contact]:
        # implementation
        pass
