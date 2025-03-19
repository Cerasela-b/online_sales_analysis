class Cart:
    def __init__(self):
        self.cart_items = [] 

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def calculate_total(self):
        total_value = sum(item.price * item.quantity for item in self.cart_items)
        return total_value

    def display_cart(self):
        cart_content = ""
        for product in self.cart_items:
            cart_content += f"Product: {product.name}\nPrice: ${product.price}\nQuantity: {product.quantity} pcs\n\n"
        return cart_content
