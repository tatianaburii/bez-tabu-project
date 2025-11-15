import re


class Validation:

    @staticmethod
    def email(email):
        email_pattern = r'^((?!\.)[\w\-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])$'
        if re.fullmatch(email_pattern, email):
            return True
        else:
            return False

    @staticmethod
    def phone(phone):
        phone_pattern = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
        if re.fullmatch(phone_pattern, phone):
            return True
        else:
            return False