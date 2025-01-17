from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
		pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(str(p) for p in self.phones)}"

    def add_phone(self, phone: Phone):
        self.phones.append(phone)
        print(f"Phone {phone} added to contact {self.name}")
        
    
    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p == phone]
        print(f"Phone {phone} deleted")

    
    def edit_phone(self, old_phone, new_phone):
        for index, phone in enumerate(self.phones):
            if phone == old_phone:
                self.phones[index] = Phone(new_phone)
                print(f"Phone {old_phone} changed to {new_phone}")
                return
            else:
                print(f"Phone {old_phone} not found")

    def find_phone(self, phone):
        for p in self.phones:
            if p == phone:
                return p
            elif p not in self.phones:
                print(f"Phone {phone} not found")
       

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[str(record.name)] = record
        print(f"Contact {record.name} added to address book")

    def find(self, name):
        res = self.data.get(name, None)
        if res:
            print(f'{name}: {', '.join(str(p) for p in res.phones)}')
            return res
        else:
            print(f"Contact {name} not found.")
            return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Contact {name} deleted")
        else:
            print(f"Contact {name} not found")


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
