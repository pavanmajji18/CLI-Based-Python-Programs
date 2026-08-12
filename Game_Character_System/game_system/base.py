import logging

logger = logging.getLogger(__name__)


class GameError(Exception):
    """Base exception for game errors."""
    pass


class InvalidAttributeError(GameError, ValueError):
    """Raised when invalid character attributes are provided."""
    pass


class CharacterDefeatedError(GameError):
    """Raised when attempting an action on or with a defeated character."""
    pass


class GameCharacter:
    """Base class representing a general game character."""

    def __init__(self, name: str, health: int, level: int = 1):
        self.name = name
        self.health = health
        self.level = level
        logger.info("Created %s (Level %d, Health: %d)", self.name, self.level, self.health)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise InvalidAttributeError("Character name must be a non-empty string.")
        self._name = value.strip()

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int):
        if not isinstance(value, (int, float)):
            raise InvalidAttributeError("Health must be a numerical value.")
        self._health = max(0, int(value))

    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, value: int):
        if not isinstance(value, int) or value < 1:
            raise InvalidAttributeError("Level must be an integer greater than or equal to 1.")
        self._level = value

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def take_damage(self, damage: int) -> int:
        """Reduces health by the damage amount and returns actual damage taken."""
        if damage < 0:
            raise InvalidAttributeError("Damage value cannot be negative.")
        
        actual_damage = min(self.health, damage)
        self.health -= actual_damage
        
        logger.warning(
            "%s took %d damage! Remaining health: %d",
            self.name, actual_damage, self.health
        )
        
        if not self.is_alive:
            logger.error("%s has been defeated!", self.name)
            
        return actual_damage