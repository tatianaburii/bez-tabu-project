from bez_tabu.contact import Contact
from bez_tabu.note import Note
from typing import List, Optional
from datetime import date, timedelta, datetime


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_record(self, record: Contact) -> bool:
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

    def find_contacts(self, query: str) -> str:
        """
        Find contacts by name/phone/email/address/birthday.
        """
        if not query:
            return "Error: Please provide a search query."
        
        query_lower = query.lower()
        found_contacts = []
        
        for contact in self.contacts:
           
            if query_lower in contact.name.lower():
                found_contacts.append(contact)
                continue
             
            if any(query_lower in phone.lower() for phone in contact.phones):
                found_contacts.append(contact)
                continue
            
            if contact.email and query_lower in contact.email.lower():
                found_contacts.append(contact)
                continue
           
            if contact.address and query_lower in contact.address.lower():
                found_contacts.append(contact)
                continue
            
            if contact.birthday and query_lower in str(contact.birthday).lower():
                found_contacts.append(contact)
                continue
            
            if hasattr(contact, 'notes') and contact.notes and query_lower in contact.notes.lower():
                found_contacts.append(contact)
        
        if not found_contacts:
            return "No contacts found matching the query."
            
        result = "Found contacts:\n"
        for contact in found_contacts:
            result += str(contact) + "\n"
        return result.strip()

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
