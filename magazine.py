from library_item import LibraryItem


class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Type: Magazine, Issue Number: {self.issue_number}"

    def to_file_string(self):
        return f"Magazine|{self.title}|{self.author}|{self.year}|{self.issue_number}|{self.available}"