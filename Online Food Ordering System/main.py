"""
Application Entry Point - Demonstrates functionality.
"""
import logging
from ordering import (
    Restaurant,
    FoodItem,
    Customer,
    FoodOrderingService,
    InvalidInputError,
    FoodOrderingError,
)

# Configure the standard logging output format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)

logger = logging.getLogger("MainProgram")


def main():
    logger.info("Starting Online Food Ordering System...")

    # 1. Instantiate Restaurant
    restaurant = Restaurant("Spice Route Diner")

    # 2. Add 5 Food Items to Menu (Prices in INR)
    try:
        items = [
            FoodItem(1, "Paneer Butter Masala", "Main Course", 280.00),
            FoodItem(2, "Butter Naan", "Bread", 45.00),
            FoodItem(3, "Veg Biryani", "Main Course", 220.00),
            FoodItem(4, "Gulab Jamun", "Dessert", 80.00),
            FoodItem(5, "Masala Chai", "Beverage", 30.00),
        ]
        for item in items:
            restaurant.add_to_menu(item)

    except InvalidInputError as e:
        logger.error(f"Menu Initialization failed: {e}")
        return

    # 3. Create Service Instance
    service = FoodOrderingService(restaurant)

    # 4. Customer Demonstration 1: Successful Order
    logger.info("--- DEMONSTRATION 1: Standard Customer Order ---")
    try:
        customer1 = Customer(101, "Aarav Sharma", "9876543210")
        # Ordering: Paneer Butter Masala, Butter Naan (x2), Masala Chai
        order1 = service.create_order(customer1, item_ids=[1, 2, 2, 5])
        
        # Display the Summary via logging
        logger.info(order1.generate_summary())
    except FoodOrderingError as e:
        logger.error(f"Customer 1 order failed: {e}")

    # 5. Customer Demonstration 2: Second Successful Order
    logger.info("--- DEMONSTRATION 2: Second Customer Order ---")
    try:
        customer2 = Customer(102, "Priya Patel", "9123456789")
        # Ordering: Veg Biryani, Gulab Jamun
        order2 = service.create_order(customer2, item_ids=[3, 4])
        
        # Display the Summary via logging
        logger.info(order2.generate_summary())
    except FoodOrderingError as e:
        logger.error(f"Customer 2 order failed: {e}")

    # 6. Demonstration 3: Exception Handling and Validation
    logger.info("--- DEMONSTRATION 3: Exception Handling Test ---")
    try:
        logger.info("Attempting to order an invalid/out-of-menu item ID...")
        customer3 = Customer(103, "Rohan Verma", "9988776655")
        service.create_order(customer3, item_ids=[1, 99])  # ID 99 does not exist
    except InvalidInputError as e:
        logger.warning(f"Successfully caught expected validation error: {e}")


if __name__ == "__main__":
    main()