"""Vehicle module containing base and specialized vehicle classes."""

import logging

logger = logging.getLogger(__name__)


class Vehicle:
    """Base class representing a general vehicle in the fleet."""

    def __init__(
        self, vehicle_number: str, brand: str, driver_name: str, price_per_km: float
    ):
        self._validate_inputs(vehicle_number, brand, driver_name, price_per_km)

        self.vehicle_number = vehicle_number.strip().upper()
        self.brand = brand.strip()
        self.driver_name = driver_name.strip()
        self.price_per_km = float(price_per_km)

        logger.info(
            "Registered vehicle %s (%s) driven by %s at ₹%.2f/KM.",
            self.vehicle_number,
            self.brand,
            self.driver_name,
            self.price_per_km,
        )

    @staticmethod
    def _validate_inputs(
        vehicle_number: str, brand: str, driver_name: str, price_per_km: float
    ):
        """Validates initialization attributes for vehicles."""
        if not isinstance(vehicle_number, str) or not vehicle_number.strip():
            raise ValueError("Vehicle number must be a non-empty string.")

        if not isinstance(brand, str) or not brand.strip():
            raise ValueError("Brand must be a non-empty string.")

        if not isinstance(driver_name, str) or not driver_name.strip():
            raise ValueError("Driver name must be a non-empty string.")

        if not isinstance(price_per_km, (int, float)) or price_per_km <= 0:
            raise ValueError("Price per KM must be a positive number.")

    def calculate_fare(self, distance_km: float) -> float:
        """Calculates total fare based on distance."""
        if not isinstance(distance_km, (int, float)) or distance_km <= 0:
            logger.error(
                "Invalid distance provided for %s: %s",
                self.vehicle_number,
                distance_km,
            )
            raise ValueError("Distance must be a positive number greater than zero.")

        fare = distance_km * self.price_per_km
        return round(fare, 2)

    def get_details(self) -> str:
        """Returns string representation of vehicle details."""
        return (
            f"Type: {self.__class__.__name__} | Reg No: {self.vehicle_number} | "
            f"Brand: {self.brand} | Driver: {self.driver_name} | Rate: ₹{self.price_per_km}/KM"
        )


class Car(Vehicle):
    """Child class representing a Car."""

    def __init__(
        self,
        vehicle_number: str,
        brand: str,
        driver_name: str,
        price_per_km: float = 20.0,
    ):
        super().__init__(vehicle_number, brand, driver_name, price_per_km)


class Bike(Vehicle):
    """Child class representing a Bike."""

    def __init__(
        self,
        vehicle_number: str,
        brand: str,
        driver_name: str,
        price_per_km: float = 10.0,
    ):
        super().__init__(vehicle_number, brand, driver_name, price_per_km)