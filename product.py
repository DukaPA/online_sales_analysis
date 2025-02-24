class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def display_info(self):
        """Displaying product information"""
        return f"Product Name: {self.name}, Price: {self.price:.2f}$, Quantity: {self.quantity}"
    
    def quantity_update(self, amount):
        """Updating product quantity"""
        self.quantity += amount
        if self.quantity < 0:
            self.quantity = 0
            print(f"Quantity for {self.name} can't less than 0.")
    