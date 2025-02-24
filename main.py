from product import Product
from product_manager import ProductManager


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
    manager.remove_product("Čokolada MILKA")
    print("\nAfter removing Čokolada MILKA:")
    manager.display_all_products()
    
if __name__ =="__main__":
    main()
    