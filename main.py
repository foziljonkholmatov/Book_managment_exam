from models.authors import add_author, get_all_authors
from models.books import (
    add_book, update_book, delete_book, get_all_books, search_books_by_author
)
from models.users import get_all_users, register_user, get_user_by_email_and_password, get_admin_by_email_and_password
from models.borrows import (
    borrow_book, return_book, get_user_borrows, get_all_borrows
)

def user_menu(user_id):
    while True:
        print("\n--- Users menu ---")
        print("1. List of books")
        print("2. Search books by author")
        print("3. Give to rent")
        print("4. Return books")
        print("5. History of rent")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            books = get_all_books()
            for b in books:
                print(f"{b['id']}. {b['title']} | {b['author']} | Available: {b['available_count']}")
        elif choice == "2":
            name = input("Enter authr name: ")
            books = search_books_by_author(name)
            for b in books:
                print(f"{b['title']} ({b['full_name']}) - Available: {b['available_count']}")
        elif choice == "3":
            book_id = int(input("Book ID: "))
            borrow_book(user_id, book_id)
            print("Book rented.")
        elif choice == "4":
            book_id = int(input("The book being returned ID: "))
            return_book(user_id, book_id)
            print("Books returned.")
        elif choice == "5":
            borrows = get_user_borrows(user_id)
            for b in borrows:
                print(f"{b['title']} | Rented: {b['borrowed_at']} | Returned: {b['returned_at']}")
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

def admin_menu():
    while True:
        print("\n=== ADMIN MENU ===")
        print("1. Add author")
        print("2. Add book")
        print("3. Book edit")
        print("4. Delete book")
        print("5. List of users")
        print("6. List of rent")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Author name: ")
            add_author(name)
            print("Author added successfully!.")
        elif choice == "2":
            title = input("Book name: ")
            author_id = int(input("Author ID: "))
            date = input("Release date (YYYY-MM-DD): ")
            count = int(input("Book count: "))
            add_book(title, author_id, date, count)
            print("Book added successfully!.")
        elif choice == "3":
            book_id = int(input("Book ID: "))
            title = input("New book name: ")
            author_id = int(input("Author ID: "))
            date = input("New release date: ")
            total = int(input("Total: "))
            available = int(input("Available count: "))
            update_book(book_id, title, author_id, date, total, available)
            print("Book edited.")
        elif choice == "4":
            book_id = int(input("Book ID: "))
            delete_book(book_id)
            print("Book  deleted.")
        elif choice == "5":
            users = get_all_users()
            for u in users:
                print(f"{u['id']}. {u['full_name']} | {u['email']}")
        elif choice == "6":
            borrows = get_all_borrows()
            for b in borrows:
                print(f"{b['full_name']} - {b['title']} | {b['borrowed_at']} > {b['returned_at']}")
        elif choice == "0":
            break
        else:
            print("Invalid number.")

def main():
    while True:
        print("\nLibrary Management System")
        print("1 - Admin")
        print("2 - Login (user)")
        print("3 - Registration")
        print("0 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            email = input("Admin email: ")
            password = input("Password: ")
            admin = get_admin_by_email_and_password(email, password)
            if admin:
                print(f"Welcome admin: {admin['full_name']}")
                admin_menu()
            else:
                print("Invalid email or password.")
        elif choice == "2":
            email = input("Email: ")
            password = input("Password: ")
            user = get_user_by_email_and_password(email, password)
            if user:
                print(f"Welcome, {user['full_name']} (ID: {user['id']})")
                user_menu(user['id'])
            else:
                print("Invalid email or password.")
        elif choice == "3":
            full_name = input("Name: ")
            email = input("Email: ")
            user_id = register_user(full_name, email)
            if user_id:
                print(f"Registration successfully. Your ID: {user_id}")
            else:
                print(" Registration error.")
        elif choice == "0":
            print("Exit...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
