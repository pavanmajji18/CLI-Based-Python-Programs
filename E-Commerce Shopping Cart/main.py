import logging
from ecommerce import (
    CartError,
    OutOfStockError,
    Product,
    ShoppingCart,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)


def run_demo():
    # 1. Initialize Catalog with 5 Products in INR (₹)
    p1 = Product("P101", "Wireless Mouse", "Electronics", 799.00, stock=10)
    p2 = Product("P102", "Mechanical Keyboard", "Electronics", 3499.00, stock=3)
    p3 = Product("P103", "Coffee Mug", "Home", 299.00, stock=15)
    p4 = Product("P104", "USB-C Cable", "Electronics", 199.00, stock=0)  # Out of stock
    p5 = Product("P105", "Desk Lamp", "Home", 1299.00, stock=2)

    cart = ShoppingCart()

    # 2. Add Valid Products
    logging.info("\n=== ADDING PRODUCTS TO CART ===")
    cart.add_product(p1, quantity=2)
    cart.add_product(p2, quantity=2)
    cart.add_product(p3, quantity=1)

    # 3. Display Cart Contents
    logging.info("\n=== CURRENT CART STATUS ===")
    cart.display_cart()

    # 4. Handle Out-Of-Stock Scenario
    logging.info("\n=== SCENARIO: PURCHASING ZERO-STOCK PRODUCT ===")
    try:
        cart.add_product(p4, quantity=1)
    except OutOfStockError as e:
        logging.exception(f"Expected Error Caught: {e}")

    # 5. Handle Over-Stock Scenario
    logging.info("\n=== SCENARIO: EXCEEDING AVAILABLE STOCK ===")
    try:
        cart.add_product(p2, quantity=2)
    except OutOfStockError as e:
        logging.exception(f"Expected Error Caught: {e}")

    # 6. Remove an Item
    logging.info("\n=== REMOVING ITEMS ===")
    cart.remove_product("P101", quantity=1)
    cart.display_cart()

    # 7. Complete Checkout
    logging.info("\n=== EXECUTING CHECKOUT ===")
    try:
        cart.checkout()
    except CartError as e:
        logging.error(f"Checkout failed: {e}")

    logging.info(f"Updated Stock for {p2.name}: {p2.stock}")


if __name__ == "__main__":
    run_demo()