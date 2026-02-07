from book import Book

def main():
    book = Book("C# Programming", 5)
    valid_input = False

    print("=" * 50)
    print("Welcome to Borrow Book System")
    print("=" * 50)
    
    while not valid_input:
        try:
            answer = input("Do you want to borrow books? (yes/no): ")
        except EOFError:
            print("=" * 50)
            print("END PROGRAM")
            print("=" * 50)
            return

        if answer.strip().lower() in ("y", "yes"):
            if book.get_available_book() != 0:
                book.borrow_book()
                print("=" * 50)
                print("Borrowed 1 book, available " + str(book.get_available_book()) + " books.")
            else:
                print("=" * 50)
                print("No books available to borrow...")
                print("=" * 50)
                valid_input = True
        elif answer.strip().lower() in ("n", "no"):
            print("=" * 50)
            print("END PROGRAM")
            print("=" * 50)
            valid_input = True
        else:
            print("=" * 50)
            print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()