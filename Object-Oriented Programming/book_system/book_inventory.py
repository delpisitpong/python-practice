from book import Book

def show_end_message():
    print("=" * 50)
    print("END PROGRAM")
    print("=" * 50)

def main():
    books = [None] * 3
    i = 0

    print("=" * 50)
    print("Welcome to Book Inventory System")
    print("=" * 50)
    
    while i < len(books):
        try:
            input_title = input(f"Enter book title (Book {i + 1}): ")
        except EOFError:
            show_end_message()
            return

        if input_title.strip() == "":
            show_end_message()
            return

        try:
            print("=" * 50)
            input_total_str = input(f"Enter the total number for: {input_title}: ")
        except EOFError:
            show_end_message()
            return

        if input_total_str.strip() == "":
            show_end_message()
            return

        try:
            input_total_book = int(input_total_str)
            books[i] = Book(input_title, input_total_book)

            print("=" * 50)
            print(books[i].get_title() +
                  " has " + str(books[i].get_total_book()) +
                  " books, can borrow " + str(books[i].get_available_book()) + " books.")
            print("=" * 50)

            i += 1
        except ValueError:
            print("=" * 50)
            print("Invalid number! Please try again.")
            print("=" * 50)

if __name__ == "__main__":
    main()