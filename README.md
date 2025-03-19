# online_sales_analysis
Final assignment Git and GitHub
# Online Sales Analysis

This is a Python project designed to manage a simple online store's product inventory, including product management, cart functionality, and total price calculations.

## Classes:

### 1. **Product Class**
- **Attributes**:
  - `name`: The name of the product.
  - `price`: The price of the product.
  - `quantity`: The available quantity of the product.
- **Methods**:
  - `display_info()`: Displays information about the product (name, price, quantity).
  - `update_quantity(amount)`: Updates the product's quantity.

### 2. **ProductManager Class**
- **Attributes**:
  - `products`: A list that contains all available products.
- **Methods**:
  - `add_product(product)`: Adds a new product to the list.
  - `display_products()`: Displays all products.
  - `calculate_total_value()`: Calculates the total value of all products in inventory.
  - `remove_product_by_name(product_name)`: Removes a product by its name.

### 3. **Cart Class**
- **Attributes**:
  - `cart_items`: A list that contains the products added to the cart.
- **Methods**:
  - `add_to_cart(product)`: Adds a product to the cart.
  - `calculate_cart_value()`: Calculates the total value of the cart.
  - `display_cart()`: Displays all items in the cart.

## Project Functionality:

- The project allows you to:
  - Add, remove, and manage products in an online store's inventory.
  - View the list of all products.
  - Calculate the total value of the inventory.
  - Add products to a cart, calculate the total cart value, and view cart contents.
