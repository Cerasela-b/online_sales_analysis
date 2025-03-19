from product import Product
from product_manager import ProductManager
from cart import Cart

product1 = Product("Bag", 1500, 95)
product2 = Product("Shoes", 1700, 34)
product3 = Product("Belt", 100, 200)
product4 = Product("Jeans", 500, 50)

product_manager = ProductManager()
cart = Cart()

product_manager.add_product(product1)
product_manager.add_product(product2)
product_manager.add_product(product3)
product_manager.add_product(product4)

#print("All Products in Inventory:")
#print(product_manager.display_all_products())

total_value = product_manager.total_inventory_value()
#print(f"Total Inventory Value: ${total_value}")