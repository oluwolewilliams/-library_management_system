from library_item import LibraryItem


class Book(LibraryItem):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Type: Book, Genre: {self.genre}"

    def to_file_string(self):
        return f"Book|{self.title}|{self.author}|{self.year}|{self.genre}|{self.available}"