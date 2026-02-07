class Product:
    def __init__(self, name = "", price = 0.0, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def sell(self, amount):
        if 0 < amount <= self.quantity:
            self.quantity -= amount
            print(f"Sold {amount} of {self.name} Stock Remaining: {self.quantity}")
        else:
            raise ValueError("Insufficient stock or invalid amount to sell")
        
    def show_info(self):
        return (f"Name : {self.name}\n"
                f"Price : {self.price:.2f} Baht/Item\n"
                f"Stock : {self.quantity} Items")