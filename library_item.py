class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def display_info(self):
        status = "Available" if self.available else "Borrowed"
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Status: {status}"

    def to_file_string(self):
        return f"LibraryItem|{self.title}|{self.author}|{self.year}|{self.available}"