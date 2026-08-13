"""Custom exceptions for the e-commerce shopping cart system."""


class CartError(Exception):
    """Base exception class for shopping cart errors."""

    pass


class OutOfStockError(CartError):
    """Raised when an operation attempts to purchase or add an out-of-stock item."""

    pass


class ProductNotFoundError(CartError):
    """Raised when a product is not found in the cart or catalog."""

    pass


class InvalidQuantityError(CartError):
    """Raised when an invalid quantity is specified."""

    pass