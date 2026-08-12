import logging
from .base import GameCharacter, CharacterDefeatedError, InvalidAttributeError

logger = logging.getLogger(__name__)


class Warrior(GameCharacter):
    """Warrior class specializing in high armor and sword attacks."""

    def __init__(self, name: str, health: int = 120, level: int = 1, shield_power: int = 10):
        super().__init__(name, health, level)
        self.shield_power = shield_power

    @property
    def shield_power(self) -> int:
        return self._shield_power

    @shield_power.setter
    def shield_power(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise InvalidAttributeError("Shield power must be a non-negative integer.")
        self._shield_power = value

    def sword_attack(self, target: GameCharacter, base_damage: int = 25):
        """Executes a melee sword attack against a target."""
        if not self.is_alive:
            raise CharacterDefeatedError(f"{self.name} cannot attack because they are defeated.")
        if not target.is_alive:
            logger.info("%s tried to attack %s, but target is already down.", self.name, target.name)
            return

        total_damage = base_damage + (self.level * 2)
        logger.info("%s swings a sword at %s for %d base damage!", self.name, target.name, total_damage)
        target.take_damage(total_damage)


class Archer(GameCharacter):
    """Archer class specializing in ranged attacks using arrows."""

    def __init__(self, name: str, health: int = 90, level: int = 1, arrows: int = 5):
        super().__init__(name, health, level)
        self.arrows = arrows

    @property
    def arrows(self) -> int:
        return self._arrows

    @arrows.setter
    def arrows(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise InvalidAttributeError("Arrows count must be a non-negative integer.")
        self._arrows = value

    def arrow_attack(self, target: GameCharacter, base_damage: int = 20):
        """Fires an arrow at the target character."""
        if not self.is_alive:
            raise CharacterDefeatedError(f"{self.name} cannot attack because they are defeated.")
        if self.arrows <= 0:
            logger.warning("%s attempted to shoot, but has no arrows left!", self.name)
            return
        if not target.is_alive:
            logger.info("%s tried to shoot %s, but target is already down.", self.name, target.name)
            return

        self.arrows -= 1
        total_damage = base_damage + (self.level * 3)
        logger.info(
            "%s fires an arrow at %s dealing %d damage! (%d arrows remaining)",
            self.name, target.name, total_damage, self.arrows
        )
        target.take_damage(total_damage)


class Wizard(GameCharacter):
    """Wizard class specializing in magic attacks using mana."""

    def __init__(self, name: str, health: int = 80, level: int = 1, mana: int = 50):
        super().__init__(name, health, level)
        self.mana = mana

    @property
    def mana(self) -> int:
        return self._mana

    @mana.setter
    def mana(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise InvalidAttributeError("Mana must be a non-negative integer.")
        self._mana = value

    def magic_attack(self, target: GameCharacter, mana_cost: int = 20, base_damage: int = 35):
        """Casts a spell on a target character."""
        if not self.is_alive:
            raise CharacterDefeatedError(f"{self.name} cannot attack because they are defeated.")
        if self.mana < mana_cost:
            logger.warning("%s tried to cast a spell but lacks enough mana! (%d required)", self.name, mana_cost)
            return
        if not target.is_alive:
            logger.info("%s tried to target %s, but target is already down.", self.name, target.name)
            return

        self.mana -= mana_cost
        total_damage = base_damage + (self.level * 4)
        logger.info(
            "%s casts Fireball at %s dealing %d damage! (%d mana remaining)",
            self.name, target.name, total_damage, self.mana
        )
        target.take_damage(total_damage)