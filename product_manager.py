from product import Product

class ProductManager:
    
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        """Adding a product"""
        self.products.append(product)
        
    def display_all_products(self):
        """Displaying all products"""
        if not self.products:
            print("No products available")
        else:
            for product in self.products:
                print(product.display_info())
                
    def total_products_value(self):
        """Calculating total value of all products"""
        total_value = sum(product.price * product.quantity for product in self.products)
        return total_value
    
    def remove_product(self, product_name):
        """Removing a product by name"""
        self.products = [product for product in self.products if product.name != product_name]