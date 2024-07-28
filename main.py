"""homework"""

import re
from collections import UserDict


class Field:
    """
    Base class for storing field values of a record.

    Attributes:
        value (str): The value of the field.
    """

    def __init__(self, value):
        """
        Initializes the field.

        Args:
            value (str): The value of the field.
        """
        self.value = value

    def __str__(self):
        """
        Returns a string representation of the field value.

        Returns:
            str: The value of the field as a string.
        """
        return str(self.value)


class Name(Field):
    """
    Class for storing a contact's name. Inherits from Field.
    """

    pass


class Phone(Field):
    """
    Class for storing a phone number. Inherits from Field.
    Validates the phone number format (10 digits).
    """

    def __init__(self, value: str):
        """
        Initializes the phone number with validation.

        Args:
            value (str): The phone number.

        Raises:
            ValueError: If the phone number does not match the format (10 digits).
        """
        if not re.fullmatch(r"\d{10}", value):
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)


class Record:
    """
    Class for storing contact information, including name and a list of phone numbers.

    Attributes:
        name (Name): The contact's name.
        phones (list of Phone): The contact's phone numbers.
    """

    def __init__(self, name: str):
        """
        Initializes the record with the contact's name.

        Args:
            name (str): The contact's name.
        """
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number: str):
        """
        Adds a phone number to the record.

        Args:
            phone_number (str): The phone number to add.
        """
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        """
        Removes a phone number from the record.

        Args:
            phone_number (str): The phone number to remove.
        """
        phone_to_remove = self.find_phone(phone_number)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)

    def edit_phone(self, old_number: str, new_number: str):
        """
        Edits a phone number in the record.

        Args:
            old_number (str): The old phone number.
            new_number (str): The new phone number.
        """
        phone_to_edit = self.find_phone(old_number)
        if phone_to_edit:
            phone_to_edit.value = new_number

    def find_phone(self, phone_number: str):
        """
        Finds a phone number in the record.

        Args:
            phone_number (str): The phone number to find.

        Returns:
            Phone: The phone number if found, or None.
        """
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        """
        Returns a string representation of the record.

        Returns:
            str: The string representation of the record.
        """
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """
    Class for storing and managing contact records. Inherits from UserDict.
    """

    def add_record(self, record: Record):
        """
        Adds a record to the address book.

        Args:
            record (Record): The record to add.
        """
        self.data[record.name.value] = record

    def find(self, name: str):
        """
        Finds a record by name in the address book.

        Args:
            name (str): The name to search for.

        Returns:
            Record: The record if found, or None.
        """
        return self.data.get(name)

    def delete(self, name: str):
        """
        Deletes a record by name from the address book.

        Args:
            name (str): The name of the record to delete.
        """
        if name in self.data:
            del self.data[name]


# Usage Example

# Create a new address book
book = AddressBook()

# Create a record for John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Add John's record to the address book
book.add_record(john_record)

# Create and add a new record for Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Print all records in the book
for name, record in book.data.items():
    print(record)

# Find and edit a phone number for John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Output: Contact name: John, phones: 1112223333; 5555555555

# Find a specific phone number in John's record
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Output: 5555555555

# Delete Jane's record
book.delete("Jane")
