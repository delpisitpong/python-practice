from movie import Movie
from ticket import Ticket

def select_showtime():
    print("\n--- Select Showtime ---")
    print("Titanic (PG-13, 120 mins)")
    print("1. 13:00")
    print("2. 14:00")
    print("3. 15:00")
    
    choice = input("Enter a number (1-3): ")
    
    showtimes = {
        "1": "13:00",
        "2": "14:00",
        "3": "15:00"
    }
    return showtimes.get(choice, "Error time")

def select_seat_number():
    print("\n--- Select Seat ---")
    input_row = input("Select seat row [A-G]: ")
    input_number = input("Select seat number [1-12]: ")
    return input_row.upper() + input_number

def main():
    movie = Movie("Titanic", 120, "PG-13")
    
    show_time = select_showtime()
    seat_number = select_seat_number()
    
    print(f"\nMovie: {movie.title} | Time: {show_time} | Seat: {seat_number}")
    confirm = input("Do you want to book a Titanic ticket? (y/n): ").lower()
    
    ticket = Ticket("T001", movie, show_time, seat_number, 240)

    if confirm == 'y':
        ticket.book_ticket()
        print("\n[System]: Ticket booked successfully!!")
        print(ticket)
    else:
        print("\n[System]: Booking cancelled.")

if __name__ == "__main__":
    main()