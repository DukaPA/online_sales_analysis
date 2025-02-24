from product import Product
from product_manager import ProductManager
from cart import Cart
import random


def main():
    manager = ProductManager()
    
    manager.add_product(Product("Coca Cola Zero", 74.99, 10))
    manager.add_product(Product("PERSIL deterdžent", 799.92, 12))
    manager.add_product(Product("Čokolada MILKA",  283.99, 15))
    manager.add_product(Product("Salata ARGETA", 239.99, 15))
    manager.add_product(Product("Bombonjere MERCI", 559.2, 10))
    
    #Displaying all products
    # print("Display all products")
    # manager.display_all_products()
    
    print(80*"*")
    
    #total value
    # total_value = manager.total_products_value()
    # print(f"Total value of all products: {total_value:.2f} $")
    
    # Removing a product
    # manager.remove_product("Čokolada MILKA")
    # print("\nAfter removing Čokolada MILKA:")
    # manager.display_all_products()
    
    cart = Cart()

    # Selecting 3 random products from the available products
    products = manager.products  
    for _ in range(3):
        product = random.choice(products)  # Select a random product
        max_quantity = min(product.quantity, 1)  # Limit quantity to available stock (max 3)
        
        if max_quantity > 0:  # Ensure the product is in stock
            quantity = random.randint(1, max_quantity)  # Random quantity (1 to max_quantity)
            cart.add_to_cart(product, quantity)

    # Display cart contents
    #print(80*"*")
    cart.display_cart()

    # Display total cart value
    print(80*"*")
    cart_total = cart.calculate_total()
    print(f"\nTotal Cart Value: ${cart_total:.2f}")
    
if __name__ =="__main__":
    main()
    