import logging
from typing import Dict, Tuple
from .exceptions import InvalidQuantityError, OutOfStockError, ProductNotFoundError
from .product import Product
from ecommerce.exceptions import CartError

logger = logging.getLogger(__name__)


class ShoppingCart:
    """Manages customer items, quantities, and cart totals."""

    def __init__(self):
        # Internal storage mapping: product_id -> (Product instance, quantity)
        self.items: Dict[str, Tuple[Product, int]] = {}
        logger.info("New shopping cart initialized.")

    def add_product(self, product: Product, quantity: int = 1):
        """Adds a product to the cart after validating stock availability."""
        if quantity <= 0:
            logger.warning(
                f"Attempted to add non-positive quantity ({quantity}) for {product.name}."
            )
            raise InvalidQuantityError(
                "Quantity to add must be greater than zero."
            )

        current_in_cart = (
            self.items[product.product_id][1]
            if product.product_id in self.items
            else 0
        )
        total_requested = current_in_cart + quantity

        if not product.is_available(total_requested):
            logger.error(
                f"Failed to add '{product.name}'. Requested total: {total_requested}, Available stock: {product.stock}."
            )
            raise OutOfStockError(
                f"Cannot add {quantity} unit(s) of '{product.name}'. Only {product.stock - current_in_cart} additional unit(s) available."
            )

        self.items[product.product_id] = (product, total_requested)
        logger.info(
            f"Added {quantity} x '{product.name}' to cart. Total in cart: {total_requested}."
        )

    def remove_product(self, product_id: str, quantity: int = None):
        """Removes a specific quantity or the entire product entry from the cart."""
        if product_id not in self.items:
            logger.warning(
                f"Attempted to remove product ID '{product_id}' which is not in the cart."
            )
            raise ProductNotFoundError("Product is not in the shopping cart.")

        product, current_qty = self.items[product_id]

        if quantity is None or quantity >= current_qty:
            del self.items[product_id]
            logger.info(f"Removed all units of '{product.name}' from cart.")
        elif quantity > 0:
            self.items[product_id] = (product, current_qty - quantity)
            logger.info(
                f"Removed {quantity} unit(s) of '{product.name}'. {current_qty - quantity} remain in cart."
            )
        else:
            raise InvalidQuantityError("Quantity to remove must be positive.")

    def calculate_total(self) -> float:
        """Calculates the total amount of all items in Indian Rupees."""
        total = sum(
            product.price * qty for product, qty in self.items.values()
        )
        return round(total, 2)

    def display_cart(self):
        """Logs the detailed contents and total of the cart in INR (₹)."""
        if not self.items:
            logger.info("Shopping Cart is currently empty.")
            return

        logger.info("--- Shopping Cart Summary ---")
        for product, qty in self.items.values():
            subtotal = product.price * qty
            logger.info(
                f" - {product.name} (x{qty}) @ ₹{product.price:.2f} each = ₹{subtotal:.2f}"
            )
        logger.info(f"Total Amount Due: ₹{self.calculate_total():.2f}")
        logger.info("-----------------------------")

    def checkout(self):
        """Finalizes the purchase by reducing product stock levels."""
        if not self.items:
            logger.warning("Attempted to checkout with an empty cart.")
            raise CartError("Cannot checkout an empty cart.")

        # Re-verify stock before committing
        for product, qty in self.items.values():
            if not product.is_available(qty):
                logger.error(f"Checkout failed: '{product.name}' went out of stock.")
                raise OutOfStockError(
                    f"Checkout failed. '{product.name}' no longer has enough stock."
                )

        # Commit stock reduction
        for product, qty in self.items.values():
            product.reduce_stock(qty)

        total_paid = self.calculate_total()
        self.items.clear()
        logger.info(
            f"Checkout completed successfully! Total Paid: ₹{total_paid:.2f}"
        )