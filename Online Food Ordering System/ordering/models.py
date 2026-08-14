"""
Domain Models representing core business entities.
"""
import logging
from typing import List
from .exceptions import InvalidInputError

logger = logging.getLogger(__name__)


class FoodItem:
    """Represents an individual menu item."""
    
    def __init__(self, item_id: int, name: str, category: str, price_inr: float):
        self.item_id = self._validate_id(item_id)
        self.name = self._validate_string(name, "Food Item Name")
        self.category = self._validate_string(category, "Category")
        self.price_inr = self._validate_price(price_inr)

    @staticmethod
    def _validate_id(item_id: int) -> int:
        if not isinstance(item_id, int) or item_id <= 0:
            raise InvalidInputError(f"Item ID must be a positive integer. Got: {item_id}")
        return item_id

    @staticmethod
    def _validate_string(value: str, field_name: str) -> str:
        if not isinstance(value, str) or not value.strip():
            raise InvalidInputError(f"{field_name} must be a non-empty string.")
        return value.strip()

    @staticmethod
    def _validate_price(price: float) -> float:
        if not isinstance(price, (int, float)) or price <= 0:
            raise InvalidInputError(f"Price must be a positive number in ₹. Got: {price}")
        return float(price)

    def __str__(self) -> str:
        return f"{self.name} ({self.category}) - ₹{self.price_inr:.2f}"


class Customer:
    """Represents a customer placing orders."""
    
    def __init__(self, customer_id: int, name: str, phone: str):
        if not isinstance(customer_id, int) or customer_id <= 0:
            raise InvalidInputError(f"Customer ID must be a positive integer. Got: {customer_id}")
        if not isinstance(name, str) or not name.strip():
            raise InvalidInputError("Customer name must be a non-empty string.")
        if not isinstance(phone, str) or len(phone.strip()) < 10:
            raise InvalidInputError("Customer phone must be a valid contact string.")

        self.customer_id = customer_id
        self.name = name.strip()
        self.phone = phone.strip()

    def __str__(self) -> str:
        return f"Customer: {self.name} (ID: {self.customer_id}, Phone: {self.phone})"


class Order:
    """Represents an individual order made by a customer."""
    
    _order_counter = 1000

    def __init__(self, customer: Customer):
        if not isinstance(customer, Customer):
            raise InvalidInputError("Order requires a valid Customer instance.")
        
        Order._order_counter += 1
        self.order_id = Order._order_counter
        self.customer = customer
        self.items: List[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        """Adds a food item to the order."""
        if not isinstance(item, FoodItem):
            raise InvalidInputError("Can only add instances of FoodItem to an order.")
        self.items.append(item)
        logger.info(f"Added '{item.name}' (₹{item.price_inr:.2f}) to Order #{self.order_id}")

    def calculate_total(self) -> float:
        """Calculates total cost in Indian Rupees (₹)."""
        return sum(item.price_inr for item in self.items)

    def generate_summary(self) -> str:
        """Constructs a readable textual summary of the order."""
        lines = [
            f"\n{'='*40}",
            f"ORDER SUMMARY - Order ID #{self.order_id}",
            f"{'='*40}",
            f"{self.customer}",
            f"{'-'*40}",
            "Items Ordered:"
        ]
        
        if not self.items:
            lines.append("  (No items added)")
        else:
            for index, item in enumerate(self.items, 1):
                lines.append(f"  {index}. {item.name:<20} : ₹{item.price_inr:>7.2f}")

        total = self.calculate_total()
        lines.extend([
            f"{'-'*40}",
            f"Total Bill Amount       : ₹{total:>7.2f}",
            f"{'='*40}\n"
        ])
        return "\n".join(lines)


class Restaurant:
    """Represents the restaurant offering food items and taking orders."""
    
    def __init__(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise InvalidInputError("Restaurant name cannot be empty.")
        self.name = name.strip()
        self.menu: dict[int, FoodItem] = {}

    def add_to_menu(self, item: FoodItem) -> None:
        """Registers a FoodItem on the restaurant's menu."""
        if item.item_id in self.menu:
            logger.warning(f"Overwriting menu item ID {item.item_id}")
        self.menu[item.item_id] = item
        logger.info(f"Added item '{item.name}' to {self.name}'s menu.")

    def get_item(self, item_id: int) -> FoodItem:
        """Fetches an item by ID from the menu."""
        if item_id not in self.menu:
            raise InvalidInputError(f"Food item ID {item_id} is not on the menu.")
        return self.menu[item_id]