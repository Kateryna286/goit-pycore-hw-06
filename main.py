from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name is required")
        super().__init__(value)

    def __str__(self):
        return f"Name: {self.value}"

class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() or len(value) == 10):
            raise ValueError("Phone number must be a 10-digit number")
        super().__init__(value)

    def __str__(self):
        return f"Phone: {self.value}"

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone_value = phone.value if isinstance(phone, Phone) else phone

        for p in self.phones:
            if p.value == phone_value:
                raise ValueError(f"Phone {phone_value} already exists for this contact.")

        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_value = phone.value if isinstance(phone, Phone) else phone

        for p in self.phones:
            if p.value == phone_value:
                self.phones.remove(p)
                return

        raise ValueError(f"Phone {phone_value} not found in record") 
    
    def edit_phone(self, old_phone, new_phone):
        old_phone_value = old_phone.value if isinstance(old_phone, Phone) else old_phone
        new_phone_value = new_phone.value if isinstance(new_phone, Phone) else new_phone

        for i, p in enumerate(self.phones):
            if p.value == old_phone_value:
                self.phones[i] = Phone(new_phone_value)
                return

        raise ValueError(f"Phone {old_phone_value} not found in record")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
		pass

phone = Phone("2345678909")
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("0987654321")
print(john_record)
john_record.remove_phone("1234567890")
print(john_record)
john_record.edit_phone("0987654321", "1112223333")
print(john_record)
