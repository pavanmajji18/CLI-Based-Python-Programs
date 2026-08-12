import logging
from game_system import Warrior, Archer, Wizard, InvalidAttributeError, CharacterDefeatedError


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S"
    )


def main():
    configure_logging()
    logging.info("=== Starting Game Character Interaction Demo ===")

    # 1. Instantiate characters
    try:
        thorin = Warrior(name="Thorin", health=100, level=2, shield_power=15)
        legolas = Archer(name="Legolas", health=70, level=3, arrows=2)
        gandalf = Wizard(name="Gandalf", health=80, level=4, mana=40)
    except InvalidAttributeError as e:
        logging.error("Failed to initialize character: %s", e)
        return

    # 2. Interactions
    logging.info("--- Combat Round 1 ---")
    thorin.sword_attack(legolas)
    legolas.arrow_attack(thorin)
    gandalf.magic_attack(thorin)

    logging.info("--- Combat Round 2 ---")
    legolas.arrow_attack(thorin)
    
    # Archer runs out of arrows on this third try
    legolas.arrow_attack(thorin)

    # Wizard strikes final blow
    gandalf.magic_attack(thorin)

    # 3. Handling exceptions and edge cases
    logging.info("--- Testing Exception Handling & Validation ---")
    
    # Trying to attack a defeated character
    gandalf.magic_attack(thorin)

    # Defeated character attempting to attack
    try:
        thorin.sword_attack(gandalf)
    except CharacterDefeatedError as e:
        logging.error("Caught expected error: %s", e)

    # Input validation test
    try:
        invalid_hero = Warrior(name="", health=-50)
    except InvalidAttributeError as e:
        logging.error("Caught validation error: %s", e)


if __name__ == "__main__":
    main()