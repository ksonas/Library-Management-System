import mysql.connector
from datetime import date

conn = mysql.connector.connect(
    host="localhost",
    user="root",      
    password="system",  
    database="library_db"
)
cursor = conn.cursor()

# Add a new book
def add_book(title, author):
    cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
    conn.commit()
    print("Book added successfully.")

# Add a new member
def add_member(name, email):
    cursor.execute("INSERT INTO members (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Member added successfully.")

# Borrow a book
def borrow_book(book_id, member_id):
    cursor.execute("SELECT available FROM books WHERE book_id=%s", (book_id,))
    available = cursor.fetchone()
    if available and available[0]:
        cursor.execute("INSERT INTO loans (book_id, member_id, loan_date) VALUES (%s, %s, %s)",
                       (book_id, member_id, date.today()))
        cursor.execute("UPDATE books SET available=FALSE WHERE book_id=%s", (book_id,))
        conn.commit()
        print("Book borrowed successfully.")
    else:
        print("Book is not available.")

# Return a book
def return_book(book_id):
    cursor.execute("UPDATE loans SET return_date=%s WHERE book_id=%s AND return_date IS NULL",
                   (date.today(), book_id))
    cursor.execute("UPDATE books SET available=TRUE WHERE book_id=%s", (book_id,))
    conn.commit()
    print("Book returned successfully.")

# View all books
def view_books():
    cursor.execute("SELECT * FROM books")
    for row in cursor.fetchall():
        print(row)

def menu():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)

        elif choice == "2":
            name = input("Enter member name: ")
            email = input("Enter member phone number : ")
            add_member(name, email)

        elif choice == "3":
            book_id = int(input("Enter book ID: "))
            member_id = int(input("Enter member ID: "))
            borrow_book(book_id, member_id)

        elif choice == "4":
            book_id = int(input("Enter book ID: "))
            return_book(book_id)

        elif choice == "5":
            view_books()

        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

menu()