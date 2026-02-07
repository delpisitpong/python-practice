from movie import Movie
from ticket import Ticket

def show_movie_list(tickets):
    result = ""
    for t in tickets:
        result += f"{t.ticket_id}: {t.movie.title}\n"
    return result

def get_safe_int(message):
    while True:
        try:
            user_input = input(message)
            if user_input == "": return None
            return int(user_input)
        except ValueError:
            print("\n>> [Error] Enter number only! <<\n")

def main():
    tickets = [
        Ticket("T001", Movie("Titanic", 120, "PG-13"), "12:00", "B7", 280),
        Ticket("T002", Movie("A Walk to Remember", 102, "PG"), "11:00", "G11", 240),
        Ticket("T003", Movie("Silent Hill", 125, "R-13"), "14:30", "H2", 240)
    ]

    print("==================================================")
    print("                  Ticket--System                  ")
    confirm = input("Do you want to book or use a ticket? (y/n): ").lower()

    while confirm == 'y':
        print("==================================================")
        print("                Available--Movies:                ")
        print(show_movie_list(tickets))
        print("==================================================")
        
        ticket_id = input("Enter a ticket id: ").strip()
        
        selected_ticket = next((t for t in tickets if t.ticket_id.lower() == ticket_id.lower()), None)

        if selected_ticket:
            menu_text = (
                "==================================================\n"
                f"\n[{selected_ticket.ticket_id}: {selected_ticket.movie.title}]\n"
                "Press [1] to book a ticket\n"
                "Press [2] to use a ticket\n"
                "Press [3] to see ticket status\n"
                "\n"
                "==================================================\n"
                "Enter menu: "
            )
            
            menu = get_safe_int(menu_text)

            if menu is not None:
                output = ""
                if menu == 1:
                    output = selected_ticket.book_ticket()
                elif menu == 2:
                    output = selected_ticket.use_ticket()
                elif menu == 3:
                    output = "\n" + "Ticket Status" + "\n"
                else:
                    print("Invalid Menu.")
                    continue
                
                print("=" * 50)
                print(f"{output}")
                print(selected_ticket)
                print()
        else:
            print("==================================================")
            print("        >> [Error] Ticket ID not found! <<        ")
            print("==================================================")

        confirm = input("Do you want to continue? (y/n): ").lower()

    print("==================================================")
    print("         Thank you for using our service!         ")
    print("==================================================")

if __name__ == "__main__":
    main()