"""Base User class implementing shared attributes and behaviors."""

import re
import logging
from elearning.exceptions import ValidationError

logger = logging.getLogger(__name__)

class User:
    """Parent class representing any system user."""

    EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    def __init__(self, user_id: str, name: str, email: str):
        self._validate_inputs(user_id, name, email)
        self.user_id = user_id.strip()
        self.name = name.strip()
        self.email = email.strip()
        logger.debug("Initialized base user %s (%s)", self.name, self.user_id)

    def _validate_inputs(self, user_id: str, name: str, email: str) -> None:
        if not isinstance(user_id, str) or not user_id.strip():
            raise ValidationError("User ID must be a non-empty string.")
        if not isinstance(name, str) or not name.strip():
            raise ValidationError("Name must be a non-empty string.")
        if not isinstance(email, str) or not re.match(self.EMAIL_REGEX, email.strip()):
            raise ValidationError(f"Invalid email address provided: '{email}'")

    def display_profile(self) -> str:
        """Shared method accessible by all child classes."""
        return f"ID: {self.user_id} | Name: {self.name} | Email: {self.email}"