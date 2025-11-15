from typing import Optional
from datetime import date, datetime
from bez_tabu.validation import Validation

class Contact:
    def __init__(self, name):
        self.name = name
        self.phones = []
        self.address = None
        self.email = None
        self.birthday = None

    # implement getters, setters, str etc.
    def _validate_phone(self, phone: str) -> bool:
        return Validation.phone(phone)
        

    def add_phone(self, phone: str) -> bool:
        is_phone_valid = self._validate_phone(phone)
        if phone not in self.phones and is_phone_valid:
            self.phones.append(phone)
            return True
        elif not is_phone_valid:
            print("The phone number is not valid. Example: +380963215698")
        else:
            print("This contact already has this phone number.")

    def remove_phone(self, phone: str) -> bool:
        if phone in self.phones:
            self.phones.remove(phone)
            return True
        return False

    def edit_phone(self, old_phone: str, new_phone: str) -> str:
        if old_phone not in self.phones:
            return "Old phone not found"

        is_phone_valid = self._validate_phone(new_phone)
        if is_phone_valid:
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone
            return "Phone updated."
        else:
            return "The new phone number is not valid. Example: +380963215698"


    def find_phone(self, phone: str) -> Optional[str]:
        return phone if phone in self.phones else None

    def add_birthday(self, birthday: str | date) -> bool:
        if isinstance(birthday, str):
            try:
                dt = datetime.strptime(birthday, "%d.%m.%Y").date()
                self.birthday = dt
            except ValueError:
                raise ValueError("Invalid date format. Use DD.MM.YYYY")
        elif isinstance(birthday, date):
            self.birthday = birthday
        else:
            raise ValueError("Birthday must be a string (DD.MM.YYYY) or date object")
        return True

    def __str__(self) -> str:
        phones_str = "; ".join(self.phones) if self.phones else "—"
        email_str = self.email if self.email else "—"
        address_str = self.address if self.address else "—"
        bday_str = self.birthday.strftime("%d.%m.%Y") if self.birthday else "—"
        return f"Contact name: {self.name}, phones: {phones_str}, email: {email_str}, address: {address_str}, birthday: {bday_str}"
