class Library:

    def __init__(self):
        self.books = []

    # Add Book
    def add_book(self, book_name):

        if book_name in self.books:
            print(f'"{book_name}" already exists.')

        else:
            self.books.append(book_name)
            print(f'"{book_name}" added successfully.')

    # Remove Book
    def remove_book(self, book_name):

        if book_name in self.books:
            self.books.remove(book_name)
            print(f'"{book_name}" removed successfully.')

        else:
            print("Invalid Book")

    # Check Book
    def check_book(self, book_name):

        if book_name in self.books:
            print(f'Book "{book_name}" is available.')

        else:
            print("Invalid Book")

    # Show All Books
    def show_books(self):

        if len(self.books) == 0:
            print("\nNo books available.")

        else:
            print("\nAvailable Books:")

            for book in self.books:
                print("-", book)


# Create Object
library = Library()

# Menu Program
while True:

    print("\n===== LIBRARY MENU =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Check Book")
    print("4. Show Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Book
    if choice == "1":

        name = input("Enter book name: ")
        library.add_book(name)

    # Remove Book
    elif choice == "2":

        name = input("Enter book name to remove: ")
        library.remove_book(name)

    # Check Book
    elif choice == "3":

        name = input("Enter book name to check: ")
        library.check_book(name)

    # Show Books
    elif choice == "4":

        library.show_books()

    # Exit
    elif choice == "5":

        print("Thank you for visit.")
        break

    else:
        print("Invalid Choice")