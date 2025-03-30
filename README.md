# Techplement
# Contact Management System

This is a Python-based **Contact Management System** application that allows users to manage their personal or professional contacts. The system provides functionalities to add, search, update, and view all contacts, which are stored persistently in a JSON file.
## Features

1. **Add a New Contact**  
   - Input: Name, phone number, and email address.
   - Validates phone numbers (must be at least 10 digits) and email addresses (must contain `@` and `.`).
   - Prevents duplicate contacts by name.
   - Saves contacts to a JSON file (`contacts.json`).

2. **Search for a Contact**  
   - Search by name or a part of the name (case-insensitive).
   - Displays matching contacts along with their phone number and email.

3. **Update an Existing Contact**  
   - Choose to update the phone number, email, or both for an existing contact.
   - Validates input for phone numbers and email addresses.
   - Saves updated information to the JSON file.

4. **Display All Contacts**  
   - Lists all saved contacts with their details.
   - Displays a message if no contacts are available.

5. **Persistent Storage**  
   - Contacts are stored in a JSON file (`contacts.json`), ensuring data is not lost when the application is closed.

6. **User-Friendly Menu**  
   - Simple text-based menu for navigation.
   - Options to perform operations like add, search, update, view all, and exit.

---

## Installation and Setup

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/contact-management-system.git
   cd contact-management-system
   ```

2. **Run the Application**  
   - Ensure you have Python 3 installed.
   - Run the script using the following command:
     ```bash
     python contact_management_system.py
     ```

3. **Dependencies**  
   - The application requires no external dependencies. It uses Python's built-in libraries (`os` and `json`).

## How to Use

1. **Starting the Application**  
   - Run the script and follow the on-screen instructions.

2. **Menu Options**  
   - **1. Add Contact:** Add a new contact by entering the required details.  
   - **2. Search Contact:** Search for contacts by entering a name or part of a name.  
   - **3. Update Contact:** Modify the phone number or email of an existing contact.  
   - **4. View All Contacts:** Display all stored contacts.  
   - **5. Exit:** Exit the application.

## Code Overview

### `load_contacts()`
- Loads contacts from `contacts.json`. If the file doesn't exist or is invalid, returns an empty dictionary.

### `save_contacts(contacts)`
- Saves the current state of contacts to `contacts.json` in a readable format.

### `add_contact(contacts)`
- Adds a new contact after validating the name, phone number, and email.

### `search_contact(contacts)`
- Searches for contacts by name and displays matching results.

### `update_contact(contacts)`
- Updates the phone number, email, or both for a specified contact.

### `display_all_contacts(contacts)`
- Lists all contacts along with their details.

### `main()`
- The main program loop, presenting a menu to the user and executing selected operations.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the application.



