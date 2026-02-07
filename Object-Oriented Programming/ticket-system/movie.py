class Movie:
    def __init__(self, title = "", minutes = 0, rating = ""):
        self.title = title
        self.minutes = minutes
        self.rating = rating

    def __str__(self):
        return f"{self.title}, {self.minutes} minutes, Rating: {self.rating}"