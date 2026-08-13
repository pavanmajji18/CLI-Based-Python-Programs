import logging

logger = logging.getLogger(__name__)


class Product:
    """Represents an item available in the store catalog."""

    def __init__(
        self,
        product_id: str,
        name: str,
        category: str,
        price: float,
        stock: int,
    ):
        self._validate_inputs(product_id, name, price, stock)

        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = float(price)
        self.stock = int(stock)

        logger.info(
            f"Product created: '{self.name}' (ID: {self.product_id}) - ₹{self.price:.2f} [Stock: {self.stock}]"
        )

    def _validate_inputs(
        self, product_id: str, name: str, price: float, stock: int
    ):
        if not product_id or not isinstance(product_id, str):
            raise ValueError("Product ID must be a non-empty string.")
        if not name or not isinstance(name, str):
            raise ValueError("Product Name must be a non-empty string.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if stock < 0:
            raise ValueError("Stock cannot be negative.")

    def is_available(self, requested_quantity: int = 1) -> bool:
        """Checks if the required quantity is currently in stock."""
        return self.stock >= requested_quantity

    def reduce_stock(self, quantity: int):
        """Decrements product stock when purchased."""
        if quantity <= 0:
            raise ValueError("Quantity to reduce must be greater than zero.")
        if quantity > self.stock:
            raise ValueError("Cannot reduce stock below zero.")
        self.stock -= quantity
        logger.info(
            f"Stock updated for '{self.name}': {self.stock} remaining."
        )

    def __repr__(self) -> str:
        return f"Product({self.product_id}, '{self.name}', ₹{self.price:.2f}, Stock: {self.stock})"