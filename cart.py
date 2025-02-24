from product import Product

class Cart:
    """Initializing an empty cart"""
    def __init__(self):
        self.cart_items = []
        
    def add_to_cart(self, product, quantity):
        """Adding a product to the cart with specified quantity"""
        if quantity <= product.quantity:
            self.cart_items.append({"product": product, "quantity": quantity})
            product.quantity_update(-quantity)  # Corrected method name
        else:
            print(f"Not enough stock for {product.name}. Available: {product.quantity}")

    def calculate_total(self):
        """Calculating the total price of items in the cart"""
        return sum(item["product"].price * item["quantity"] for item in self.cart_items)

    def display_cart(self):
        """Displaying cart contents"""
        if not self.cart_items:
            print("Your cart is empty.")
        else:
            print("Cart Contents:")
            for item in self.cart_items:
                product = item["product"]
                quantity = item["quantity"]
                print(f"{product.name} - {quantity} pcs - ${product.price * quantity:.2f}")
