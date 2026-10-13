'''
Create a pythn program to manage a small library using a dictonary. The program must repeatedly allow the user to add books,issue books,
return books, and display the current book record.

Conditions:
- Store book title as the key and available copies as the value.
- A book can be issued only if it exists and at least one copy is available.
- Return a book only if it already exists in the library record.
- Book names should workk regardless of uppercase or lowercase letters.

'''

library = {}

while True:
    print("\n1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book = input("Enter book name: ").lower()
        copies = int(input("Enter copies: "))
        library[book] = copies
        print("Book added")

    elif choice == "2":
        book = input("Enter book name: ").lower()

        if book in library and library[book] > 0:
            library[book] -= 1
            print("Book issued")
        else:
            print("Book not available")

    elif choice == "3":
        book = input("Enter book name: ").lower()

        if book in library:
            library[book] += 1
            print("Book returned")
        else:
            print("Book not found")

    elif choice == "4":
        print("Library:", library)

    elif choice == "5":
        break

    else:
        print("Invalid choice")