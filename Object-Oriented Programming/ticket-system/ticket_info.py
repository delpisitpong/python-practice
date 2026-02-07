from movie import Movie
from ticket import Ticket

def select_showtime():
    print("Titanic (PG-13, 120 mins)")
    print("\nPress 1 to select show time = 13:00")
    print("Press 2 to select show time = 14:00")
    print("Press 3 to select show time = 15:00")
    print("=" * 50)
    
    choice = input("\nEnter a number: ")
    
    showtimes = {
        "1": "13:00",
        "2": "14:00",
        "3": "15:00"
    }
    
    return showtimes.get(choice, "Error time")

def select_seat_number():
    input_row = input("Select seat row [A-G]: ")
    input_number = input("Select seat number [1-12]: ")
    return input_row.upper() + input_number

if __name__ == "__main__":
    movie = Movie("Titanic", 120, "PG-13")
    
    show_time = select_showtime()
    seat_number = select_seat_number()
    
    ticket = Ticket("T001", movie, show_time, seat_number, 240)
    
    print(ticket)