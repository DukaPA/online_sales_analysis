from product import Product
from product_manager import ProductManager


def main():
    manager = ProductManager()
    
    manager.add_product(Product("Coca Cola Zero", 74.99, 1))
    manager.add_product(Product("PERSIL deterdžent", 799.92, 2))
    manager.add_product(Product("Čokolada MILKA",  283.99, 5))
    manager.add_product(Product("Salata ARGETA", 239.99, 5))
    manager.add_product(Product("Bombonjere MERCI", 559.2, 10))
    
    print("Display all products")
    manager.display_all_products()
    
    print(80*"*")
    
    total_value = manager.total_products_value()
    print(f"Total value of all products: {total_value:.2f} $")
    
if __name__ =="__main__":
    main()
    