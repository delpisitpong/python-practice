class Ticket:
    def __init__(self, ticket_id, movie, show_time, seat_number, price):
        self.ticket_id = ticket_id
        self.movie = movie
        self.show_time = show_time
        self.seat_number = seat_number
        self.price = price
        self.is_booked = False
        self.is_used = False

    def get_ticket_id(self):
        return self.ticket_id

    def get_movie(self):
        return self.movie

    def book_ticket(self):
        if not self.is_booked:
            self.is_booked = True
            return "\n" + "Ticket booked" + "\n"
        else:
            return "\n" + "This ticket is already booked" + "\n"

    def use_ticket(self):
        if not self.is_booked:
            return "\n" + "Please book the ticket first" + "\n"
        if self.is_used:
            return "\n" + "Ticket already used" + "\n"
        else:
            self.is_used = True
            return "\n" + "Enjoy the movie!!" + "\n"

    def __str__(self):
        return (("=" * 50) +
                "\n"
                f"Ticket Id: {self.ticket_id}\n"
                f"Movie: {self.movie}\n"
                f"Show Time: {self.show_time}\n"
                f"Seat Number: {self.seat_number}\n"
                f"Ticket Price: {self.price}\n"
                f"Booked: {'Yes' if self.is_booked else 'No'}\n"
                f"Used: {'Yes' if self.is_used else 'No'}"+
                "\n" +
                ("=" * 50))