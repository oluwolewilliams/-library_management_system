from library import Library


def menu():
    library = Library()
    filename = "library_data.txt"
    library.load_from_file(filename)

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Add Magazine")
        print("3. Remove Item")
        print("4. Borrow Item")
        print("5. Return Item")
        print("6. View Available Items")
        print("7. View All Items")
        print("8. Search by Title or Author")
        print("9. Sort Items by Title")
        print("10. Sort Items by Year")
        print("11. View Borrow History")
        print("12. Save Library Data")
        print("13. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            try:
                year = int(input("Enter year: "))
            except ValueError:
                print("Invalid year. Please enter a number.")
                continue
            genre = input("Enter genre: ")
            library.add_book(title, author, year, genre)

        elif choice == "2":
            title = input("Enter magazine title: ")
            author = input("Enter author/editor: ")
            try:
                year = int(input("Enter year: "))
            except ValueError:
                print("Invalid year. Please enter a number.")
                continue
            issue_number = input("Enter issue number: ")
            library.add_magazine(title, author, year, issue_number)

        elif choice == "3":
            title = input("Enter title of item to remove: ")
            library.remove_item(title)

        elif choice == "4":
            title = input("Enter title of item to borrow: ")
            library.borrow_item(title)

        elif choice == "5":
            title = input("Enter title of item to return: ")
            library.return_item(title)

        elif choice == "6":
            library.view_available_items()

        elif choice == "7":
            library.view_all_items()

        elif choice == "8":
            keyword = input("Enter title or author to search: ")
            library.search_item(keyword)

        elif choice == "9":
            library.sort_items_by_title()

        elif choice == "10":
            library.sort_items_by_year()

        elif choice == "11":
            library.view_borrow_history()

        elif choice == "12":
            library.save_to_file(filename)

        elif choice == "13":
            library.save_to_file(filename)
            print("Exiting the system. Goodbye.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 13.")


menu()