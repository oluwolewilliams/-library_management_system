from book import Book
from magazine import Magazine


class Library:
    def __init__(self):
        self.items = []
        self.borrow_history = []

    def add_book(self, title, author, year, genre):
        book = Book(title, author, year, genre)
        self.items.append(book)
        print(f"Book '{title}' added successfully.")

    def add_magazine(self, title, author, year, issue_number):
        magazine = Magazine(title, author, year, issue_number)
        self.items.append(magazine)
        print(f"Magazine '{title}' added successfully.")

    def remove_item(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                self.items.remove(item)
                print(f"'{title}' removed successfully.")
                return
        print(f"Item '{title}' not found.")

    def view_all_items(self):
        if not self.items:
            print("The library is empty.")
        else:
            print("\nAll Library Items:")
            for item in self.items:
                print(item.display_info())

    def view_available_items(self):
        available_items = [item for item in self.items if item.available]

        if not available_items:
            print("No items are currently available.")
        else:
            print("\nAvailable Library Items:")
            for item in available_items:
                print(item.display_info())

    def borrow_item(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                if item.available:
                    item.available = False
                    self.borrow_history.append(item.title)
                    print(f"You have borrowed '{item.title}'.")
                else:
                    print(f"'{item.title}' is currently not available.")
                return
        print(f"Item '{title}' does not exist in the library.")

    def return_item(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                if not item.available:
                    item.available = True
                    print(f"You have returned '{item.title}'.")
                else:
                    print(f"'{item.title}' was not borrowed.")
                return
        print(f"Item '{title}' does not exist in the library.")

    def search_item(self, keyword):
        found_items = []

        for item in self.items:
            if keyword.lower() in item.title.lower() or keyword.lower() in item.author.lower():
                found_items.append(item)

        if not found_items:
            print("No matching items found.")
        else:
            print("\nSearch Results:")
            for item in found_items:
                print(item.display_info())

    def sort_items_by_title(self):
        self.items.sort(key=lambda item: item.title.lower())
        print("Items sorted by title successfully.")

    def sort_items_by_year(self):
        self.items.sort(key=lambda item: item.year)
        print("Items sorted by year successfully.")

    def view_borrow_history(self):
        if not self.borrow_history:
            print("No borrow history available.")
        else:
            print("\nBorrow History:")
            for title in self.borrow_history:
                print(title)

    def save_to_file(self, filename):
        try:
            with open(filename, "w") as file:
                for item in self.items:
                    file.write(item.to_file_string() + "\n")
            print("Library data saved successfully.")
        except Exception as e:
            print(f"Error saving file: {e}")

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                self.items.clear()
                for line in file:
                    parts = line.strip().split("|")

                    if parts[0] == "Book":
                        book = Book(parts[1], parts[2], int(parts[3]), parts[4])
                        book.available = parts[5] == "True"
                        self.items.append(book)

                    elif parts[0] == "Magazine":
                        magazine = Magazine(parts[1], parts[2], int(parts[3]), parts[4])
                        magazine.available = parts[5] == "True"
                        self.items.append(magazine)

            print("Library data loaded successfully.")
        except FileNotFoundError:
            print("File not found. Starting with an empty library.")
        except Exception as e:
            print(f"Error loading file: {e}")