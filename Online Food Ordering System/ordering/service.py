"""
Service layer to orchestrate order processing workflows.
"""
import logging
from .models import Restaurant, Customer, Order
from .exceptions import InvalidInputError, FoodOrderingError

logger = logging.getLogger(__name__)


class FoodOrderingService:
    """Manages order creations and processing interactions."""

    def __init__(self, restaurant: Restaurant):
        self.restaurant = restaurant

    def create_order(self, customer: Customer, item_ids: list[int]) -> Order:
        """
        Creates an order for a customer given a list of item IDs.
        """
        if not item_ids:
            logger.error("Attempted to place an order without any items.")
            raise InvalidInputError("Order must contain at least one item ID.")

        order = Order(customer)
        
        for item_id in item_ids:
            try:
                food_item = self.restaurant.get_item(item_id)
                order.add_item(food_item)
            except InvalidInputError as err:
                logger.error(f"Failed to add item ID {item_id} to Order #{order.order_id}: {err}")
                raise

        logger.info(f"Successfully finalized Order #{order.order_id} for {customer.name}")
        return order