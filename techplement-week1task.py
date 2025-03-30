import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from JSON file"""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_contacts(contacts):
    """Save contacts to JSON file"""
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    """Add a new contact"""
    print("\nAdd New Contact")
    name = input("Enter name: ").strip()
    
    # Check if contact already exists
    if name in contacts:
        print("Contact already exists!")
        return
    
    phone = input("Enter phone number: ").strip()
    while not phone.isdigit() or len(phone) < 10:
        print("Invalid phone number. Must be at least 10 digits.")
        phone = input("Enter phone number: ").strip()
    
    email = input("Enter email address: ").strip()
    while "@" not in email or "." not in email:
        print("Invalid email address. Must contain '@' and '.'")
        email = input("Enter email address: ").strip()
    
    contacts[name] = {
        'phone': phone,
        'email': email
    }
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

def search_contact(contacts):
    """Search for a contact"""
    print("\nSearch Contact")
    search_term = input("Enter name to search: ").strip().lower()
    
    found = False
    for name, details in contacts.items():
        if search_term in name.lower():
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            found = True
    
    if not found:
        print("No contacts found matching your search.")

def update_contact(contacts):
    """Update an existing contact"""
    print("\nUpdate Contact")
    name = input("Enter name of contact to update: ").strip()
    
    if name not in contacts:
        print("Contact not found!")
        return
    
    print("\nCurrent Contact Details:")
    print(f"Name: {name}")
    print(f"Phone: {contacts[name]['phone']}")
    print(f"Email: {contacts[name]['email']}")
    
    print("\nWhat would you like to update?")
    print("1. Phone number")
    print("2. Email address")
    print("3. Both phone and email")
    choice = input("Enter your choice (1-3): ").strip()
    
    if choice == "1":
        new_phone = input("Enter new phone number: ").strip()
        while not new_phone.isdigit() or len(new_phone) < 10:
            print("Invalid phone number. Must be at least 10 digits.")
            new_phone = input("Enter new phone number: ").strip()
        contacts[name]['phone'] = new_phone
    elif choice == "2":
        new_email = input("Enter new email address: ").strip()
        while "@" not in new_email or "." not in new_email:
            print("Invalid email address. Must contain '@' and '.'")
            new_email = input("Enter new email address: ").strip()
        contacts[name]['email'] = new_email
    elif choice == "3":
        new_phone = input("Enter new phone number: ").strip()
        while not new_phone.isdigit() or len(new_phone) < 10:
            print("Invalid phone number. Must be at least 10 digits.")
            new_phone = input("Enter new phone number: ").strip()
        
        new_email = input("Enter new email address: ").strip()
        while "@" not in new_email or "." not in new_email:
            print("Invalid email address. Must contain '@' and '.'")
            new_email = input("Enter new email address: ").strip()
        
        contacts[name]['phone'] = new_phone
        contacts[name]['email'] = new_email
    else:
        print("Invalid choice. No changes made.")
        return
    
    save_contacts(contacts)
    print("Contact updated successfully!")

def display_all_contacts(contacts):
    """Display all contacts"""
    print("\nAll Contacts:")
    if not contacts:
        print("No contacts found.")
        return
    
    for name, details in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")

def main():
    """Main program loop"""
    contacts = load_contacts()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. View All Contacts")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            display_all_contacts(contacts)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    main()
