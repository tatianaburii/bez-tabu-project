import re


class Validation:

    @staticmethod
    def email(email):
        email_pattern = r'^((?!\.)[\w\-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])$'
        if re.fullmatch(email_pattern, email):
            return email
        else:
            raise ValueError("The email address is not valid. Example: example@gmail.com")

    @staticmethod
    def phone(phone):
        phone_pattern = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
        if re.fullmatch(phone_pattern, phone):
            return phone
        else:
            raise ValueError("The phone number is not valid. Example: +380963215698")