from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_all_products(self):
        if not self.products:
            return "No products available."
        
        product_info = ""
        for product in self.products:
            product_info += product.display_info() + "\n\n"
        return product_info

    def total_inventory_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.price * product.quantity
        return total_value
