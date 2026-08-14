"""
Custom Exception Classes for Input Validation and Domain Logic Errors.
"""

class FoodOrderingError(Exception):
    """Base exception class for the ordering system."""
    pass


class InvalidInputError(FoodOrderingError):
    """Raised when provided user input fails validation constraints."""
    pass


class ItemNotFoundError(FoodOrderingError):
    """Raised when a food item or entity cannot be found in the system."""
    pass