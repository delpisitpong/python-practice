class Book:
    def __init__(self, title = "", total_book = 0):
        self.title = title
        self.total_book = total_book
        self.available_book = total_book

    def get_title(self):
        return self.title

    def get_total_book(self):
        return self.total_book

    def get_available_book(self):
        return self.available_book

    def borrow_book(self):
        if self.available_book > 0:
            self.available_book -= 1
        else:
            print("No book available to borrow")

    def return_book(self):
        if self.available_book < self.total_book:
            self.available_book += 1
        else:
            print("All books are already returned")