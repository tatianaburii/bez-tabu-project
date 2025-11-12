from contact import Contact
from typing import Optional
from datetime import date, timedelta, datetime


class AddressBook:
    def __init__(self):
        self.contacts = []  # store contacts

    def add_record(self, record: Contact) -> bool:
        # сheck if contact already exists
        existing = self.find(record.name)
        if existing:
            index = self.contacts.index(existing)
            self.contacts[index] = record
        else:
            self.contacts.append(record)
        return True

    def find(self, name: str) -> Optional[Contact]:
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def delete(self, name: str) -> bool:
        contact = self.find(name)
        if contact:
            self.contacts.remove(contact)
            return True
        return False

    def get_upcoming_birthdays(self, number_of_days: int) -> list[Contact]:
        today = date.today()
        end_day = today + timedelta(days=number_of_days)
        result = []

        for contact in self.contacts:
            if not contact.birthday:
                continue

            bday: date = contact.birthday
            next_bd = bday.replace(year=today.year)

            if next_bd < today:
                next_bd = bday.replace(year=today.year + 1)
            if today <= next_bd <= end_day:
                congr_date = next_bd
                if congr_date.weekday() == 5:
                    congr_date += timedelta(days=2)
                elif congr_date.weekday() == 6:
                    congr_date += timedelta(days=1)

                result.append({
                    "name": contact.name,
                    "congratulation_date": congr_date.strftime("%d.%m.%Y")
                })

        result.sort(key=lambda d: datetime.strptime(d["congratulation_date"], "%d.%m.%Y"))
        return result
