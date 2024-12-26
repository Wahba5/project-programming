from abc import ABC, abstractmethod

# Single Responsibility Principle (SRP)
class Ride:
    def _init_(self, ride_number, start, destination):
        self.ride_number = ride_number
        self.start = start
        self.destination = destination
        self.status = "Pending"

class Rider:
    def _init_(self, rider_number, name):
        self.rider_number = rider_number
        self.name = name

class Driver:
    def _init_(self, driver_number, name, vehicle):
        self.driver_number = driver_number
        self.name = name
        self.vehicle = vehicle

# Open/Closed Principle (OCP)
class RideCalculator(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass

class BasicRide(RideCalculator):
    def calculate_fare(self, distance):
        return distance * 10  # Example: 10LE per km

class PremiumRide(RideCalculator):
    def calculate_fare(self, distance):
        return distance * 20  # Example: 20LE per km

# Liskov Substitution Principle (LSP)
class Vehicle(ABC):
    def _init_(self,  capacity):
        
        self.capacity = capacity

class Car(Vehicle):
    def _init_(self,  capacity, model):
        super()._init_( capacity)
        self.model = model

class Bike(Vehicle):
    def _init_(self,  capacity):
        super()._init_( capacity)

# Interface Segregation Principle (ISP)
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processed credit card payment of ${amount}")

class cashPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processed cash payment of ${amount}")

# Dependency Inversion Principle (DIP)
class RideService:
    def _init_(self, ride_calculator: RideCalculator, payment_processor: PaymentProcessor):
        self.ride_calculator = ride_calculator
        self.payment_processor = payment_processor

    def complete_ride(self, distance, rider: Rider):
        fare = self.ride_calculator.calculate_fare(distance)
        self.payment_processor.process_payment(fare)
        print(f"Ride completed for {rider.name}. Fare: ${fare}")

# Example Usage

ride = Ride(ride_number=1, start="Point A", destination="Point B")
rider = Rider(rider_number=1, name="abdelrahman")
driver = Driver(driver_number=1, name="Bob", vehicle=Car("123-ABC", 4, "Toyota"))

# Choosing calculator and payment method
ride_calculator = PremiumRide()  
payment_processor = cashPayment()  

# Completing the ride
ride_service = RideService(ride_calculator, payment_processor)
ride_service.complete_ride(distance=15, rider=rider)