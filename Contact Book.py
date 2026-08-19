import json
import os

FILE_NAME = "contacts.json"

# Load contacts
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save contacts
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()

    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print("✅ Contact added!")

# View contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found!")
        return

    print("\n📋 Contact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

# Search contact
def search_contact(contacts):
    keyword = input("Enter name to search: ").lower()

    found = [c for c in contacts if keyword in c["name"].lower()]

    if found:
        print("\n🔍 Results:")
        for c in found:
            print(f"{c['name']} - {c['phone']}")
    else:
        print("❌ No matching contact found.")

# Delete contact
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        num = int(input("Enter number to delete: "))
        removed = contacts.pop(num - 1)
        save_contacts(contacts)
        print(f"🗑️ Deleted: {removed['name']}")
    except:
        print("Invalid input!")

# Main program
def main():
    contacts = load_contacts()

    while True:
        print("\n--- CONTACT BOOK ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
