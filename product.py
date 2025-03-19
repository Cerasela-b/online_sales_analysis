class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        return f"Product Name: {self.name}\nPrice: ${self.price}\nQuantity: {self.quantity} pcs"

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
