from book import Book

def main():
    book = Book("Java Programming", 5)

    print("=" * 50)
    print("Welcome to Borrow/Return Book System")
    print("=" * 50)

    while True:
        try:
            answer = input("Do you want to borrow/return book? (yes/no): ")
        except EOFError:
            print("=" * 50)
            print("END PROGRAM")
            print("=" * 50)
            return

        ans = answer.strip().lower()
        if ans in ("y", "yes"):
            try:
                print("=" * 50)
                choice_input = input("Press 1 to borrow book\nPress 2 to return book\nYour choice: ")
            except EOFError:
                print("=" * 50)
                print("END PROGRAM")
                print("=" * 50)
                return

            if choice_input is None:
                print("=" * 50)
                print("END PROGRAM")
                print("=" * 50)
                return

            try:
                choice = int(choice_input)
            except ValueError:
                print("=" * 50)
                print("Please enter only 1 or 2")
                continue

            if choice == 1:
                if book.get_available_book() > 0:
                    book.borrow_book()
                    print("=" * 50)
                    print("Borrowed 1 book, available " + str(book.get_available_book()) + " books.")
                else:
                    print("=" * 50)
                    print("No books available to borrow...")
            elif choice == 2:
                if book.get_available_book() < book.get_total_book():
                    book.return_book()
                    print("=" * 50)
                    print("Returned 1 book, available " + str(book.get_available_book()) + " books.")
                else:
                    print("=" * 50)
                    print("Cannot return! All books are already here.")
            else:
                print("=" * 50)
                print("Please enter only 1 or 2")
        elif ans in ("n", "no"):
            print("=" * 50)
            print("END PROGRAM")
            print("=" * 50)
            break
        else:
            print("=" * 50)
            print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()