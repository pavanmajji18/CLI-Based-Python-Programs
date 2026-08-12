"""Booking service module to manage fleet and process rides."""

import logging
from typing import Dict, Optional
from .vehicles import Vehicle

logger = logging.getLogger(__name__)


class BookingService:
    """Service to handle vehicle management and booking operations."""

    def __init__(self):
        self.fleet: Dict[str, Vehicle] = {}

    def add_vehicle(self, vehicle: Vehicle) -> None:
        """Adds a vehicle to the booking system fleet."""
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Only instances of Vehicle can be added to the fleet.")

        self.fleet[vehicle.vehicle_number] = vehicle
        logger.debug(
            "Vehicle %s added to active fleet inventory.", vehicle.vehicle_number
        )

    def book_ride(
        self, vehicle_number: str, distance_km: float
    ) -> Optional[Dict[str, str]]:
        """Processes a cab booking request and outputs trip details."""
        vehicle_key = vehicle_number.strip().upper()

        try:
            if vehicle_key not in self.fleet:
                raise KeyError(
                    f"Vehicle with number '{vehicle_number}' is not available in our fleet."
                )

            selected_vehicle = self.fleet[vehicle_key]
            total_fare = selected_vehicle.calculate_fare(distance_km)

            booking_summary = {
                "Driver": selected_vehicle.driver_name,
                "Vehicle Type": selected_vehicle.__class__.__name__,
                "Vehicle Number": selected_vehicle.vehicle_number,
                "Brand": selected_vehicle.brand,
                "Distance": f"{distance_km} KM",
                "Rate": f"₹{selected_vehicle.price_per_km}/KM",
                "Total Fare": f"₹{total_fare:.2f}",
            }

            logger.info(
                "BOOKING SUCCESSFUL -> Driver: %s | Vehicle: %s | Distance: %s KM | Rate: ₹%s/KM | Total Fare: ₹%.2f",
                selected_vehicle.driver_name,
                selected_vehicle.__class__.__name__,
                distance_km,
                selected_vehicle.price_per_km,
                total_fare,
            )
            return booking_summary

        except (KeyError, ValueError) as err:
            logger.warning("Booking failed: %s", err)
            return None