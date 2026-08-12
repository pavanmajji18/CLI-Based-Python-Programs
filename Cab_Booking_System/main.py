"""Main executable script to demonstrate the Cab Booking System."""

import logging
from cab_booking import Bike, BookingService, Car

# Configure system logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("MainApp")


def run_demo():
    logger.info("--- Initializing Cab Booking System ---")
    service = BookingService()

    # 1. Create Fleet (2 Cars and 2 Bikes)
    try:
        car1 = Car(
            vehicle_number="KA-01-EA-1234",
            brand="Sedan",
            driver_name="Rahul",
            price_per_km=20.0,
        )
        car2 = Car(
            vehicle_number="KA-02-MB-5678",
            brand="SUV",
            driver_name="Priya",
            price_per_km=25.0,
        )
        bike1 = Bike(
            vehicle_number="KA-03-JK-9012",
            brand="Sports Bike",
            driver_name="Amit",
            price_per_km=10.0,
        )
        bike2 = Bike(
            vehicle_number="KA-04-XY-3456",
            brand="Cruiser",
            driver_name="Suresh",
            price_per_km=12.0,
        )

        for vehicle in [car1, car2, bike1, bike2]:
            service.add_vehicle(vehicle)

    except ValueError as e:
        logger.error("Failed to initialize fleet due to validation error: %s", e)
        return

    logger.info("--- Processing Sample Trips ---")

    # Trip 1: Car booking (Matches example spec)
    service.book_ride(vehicle_number="KA-01-EA-1234", distance_km=15)

    # Trip 2: Bike booking
    service.book_ride(vehicle_number="KA-03-JK-9012", distance_km=8)

    # Trip 3: Premium SUV Car booking
    service.book_ride(vehicle_number="KA-02-MB-5678", distance_km=22.5)

    logger.info("--- Testing Exception Handling & Input Validation ---")

    # Case A: Booking non-existent vehicle
    service.book_ride(vehicle_number="MH-12-ZZ-0000", distance_km=10)

    # Case B: Invalid distance (negative value)
    service.book_ride(vehicle_number="KA-04-XY-3456", distance_km=-5)


if __name__ == "__main__":
    run_demo()