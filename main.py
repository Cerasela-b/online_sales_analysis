from product import Product
from product_manager import ProductManager
from cart import Cart

product1 = Product("Bag", 1500, 80)
product2 = Product("Shoes", 1700, 20)
product3 = Product("Belt", 100, 150)
product4 = Product("Jeans", 500, 30)

product_manager = ProductManager()
cart = Cart()

product_manager.add_product(product1)
product_manager.add_product(product2)
product_manager.add_product(product3)
product_manager.add_product(product4)

print("All Products in Inventory:")
print(product_manager.display_all_products())

total_value = product_manager.total_inventory_value()
print(f"Total Inventory Value: ${total_value}")

print("Products in the Cart:")
print(cart.display_cart())  
print(f"Total Price: ${cart.calculate_total()}")