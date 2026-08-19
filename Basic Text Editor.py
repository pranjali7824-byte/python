FILE_NAME = "notes.txt"

# Write new note
def write_note():
    print("\n✍️ Write your note (type 'SAVE' on a new line to finish):")
    
    lines = []
    while True:
        line = input()
        if line.upper() == "SAVE":
            break
        lines.append(line)

    with open(FILE_NAME, "w") as file:
        file.write("\n".join(lines))

    print("✅ Note saved successfully!")

# Append note
def append_note():
    print("\n➕ Add more text (type 'SAVE' to finish):")

    lines = []
    while True:
        line = input()
        if line.upper() == "SAVE":
            break
        lines.append(line)

    with open(FILE_NAME, "a") as file:
        file.write("\n" + "\n".join(lines))

    print("✅ Text appended!")

# View note
def view_note():
    try:
        with open(FILE_NAME, "r") as file:
            content = file.read()
            print("\n📄 Your Notes:")
            print("--------------------------------")
            print(content)
            print("--------------------------------")
    except:
        print("❌ No notes found!")

# Main program
def main():
    while True:
        print("\n--- BASIC TEXT EDITOR ---")
        print("1. Write New Note")
        print("2. Append Note")
        print("3. View Notes")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            write_note()
        elif choice == "2":
            append_note()
        elif choice == "3":
            view_note()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
