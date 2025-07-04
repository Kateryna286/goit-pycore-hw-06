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
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must be a 10-digit number")
        super().__init__(value)

    def __str__(self):
        return f"Phone: {self.value}"

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # Check if phone is an object of Phone class or a string and return string
    def _get_phone_value(self, phone):
        return phone.value if isinstance(phone, Phone) else phone

    def add_phone(self, phone):
        phone_value = self._get_phone_value(phone)

        for p in self.phones:
            if p.value == phone_value:
                raise ValueError(f"Phone {phone_value} already exists for this contact.")

        self.phones.append(Phone(phone))
        print(f"Phone {phone_value} added to contact {self.name.value}")

    def remove_phone(self, phone):
        phone_value = self._get_phone_value(phone)

        for p in self.phones:
            if p.value == phone_value:
                print(f"Phone {phone_value} removed from contact {self.name.value}")
                self.phones.remove(p)
                return

        raise ValueError(f"Phone {phone_value} not found in record") 
    
    def edit_phone(self, old_phone, new_phone):
        old_phone_value = self._get_phone_value(old_phone)
        new_phone_value = self._get_phone_value(new_phone)

        if old_phone_value == new_phone_value:
            raise ValueError("New phone number must be different from the old one")  

        for i, p in enumerate(self.phones):
            if p.value == old_phone_value:
                print(f"Phone {old_phone_value} changed to {new_phone_value} in contact {self.name.value}") 
                self.phones[i] = Phone(new_phone_value)
                return

        raise ValueError(f"Phone {old_phone_value} not found in record")
    
    def find_phone(self, phone):
        phone_value = self._get_phone_value(phone)

        for p in self.phones:
            if p.value == phone_value:
                # print(f"Phone {phone_value} found in contact {self.name.value}")
                print(f"Phone found: {p.value}")
                return p

        raise ValueError(f"Phone {phone_value} not found in record")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record
        print(f"Record for '{record.name.value}' added to address book.")

    def find(self, name):
        if name in self.data:
            print(f"Record found: {self.data[name]}")
            return self.data[name]
        else:
            raise ValueError(f"Record with name {name} not found")

    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
            print(f"Record for '{name}' deleted from address book.") 
        else:
            raise ValueError(f"Record with name {name} not found")