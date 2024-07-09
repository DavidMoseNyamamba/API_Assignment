#Create a base Vehicle class with attributes registration_number, make, and model
#The Vehicle class is the base class with attributes registration_number, make, and model.
class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

#method display_info to return a formatted string with vehicle information.
    def display_info(self):
        return f"Registration Number: {self.registration_number}, Make: {self.make}, Model: {self.model}"
#Car class inherit from the Vehicle class.
class Car(Vehicle):
    def __init__(self, registration_number, make, model, number_of_seats):
        super().__init__(registration_number, make, model)
        self.number_of_seats = number_of_seats

#override the display_info method to include the number_of_seats attribute.
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Number of Seats: {self.number_of_seats}"
    
#Truck class inherit from the Vehicle class.
class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

#override the display_info method to include the cargo_capacity attribute.
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Cargo Capacity: {self.cargo_capacity}"
    
#Motorcycle class inherit from the Vehicle class.
class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

#override the display_info method to include the engine_capacity attribute.
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Engine Capacity: {self.engine_capacity}"

class Fleet:
    def __init__(self):
        self.vehicles = []
# method to add a vehicle in fleet class
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle.registration_number} added successfully.\n")

# method to display a vehicle in fleet class
    def display_all_vehicles(self):
        if not self.vehicles:
            print("No vehicles to display.\n")
        else:
            for vehicle in self.vehicles:
                print(vehicle.display_info())
            print("")

# method to search a vehicle in fleet class by registration number
    def search_vehicle_by_registration_number(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                print("Vehicle found:")
                print(vehicle.display_info())
                print("")
                return
        print(f"Vehicle with registration number {registration_number} not found.\n")

#def main()
#provides a menu for the user to add a vehicle, display all vehicles, search for a vehicle by registration number, or exit the program.
#Based on the user's choice, it performs the corresponding action by calling the appropriate methods from the Fleet class
def main():
    fleet = Fleet()
    while True:
        print("Transport Fleet Management System")
        print("1. Add a new vehicle")
        print("2. Display all vehicles")
        print("3. Search for a vehicle by registration number")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            vehicle_type = input("Enter vehicle type (car/truck/motorcycle): ").lower()
            registration_number = input("Enter registration number: ")
            make = input("Enter make: ")
            model = input("Enter model: ")
            
            if vehicle_type == 'car':
                number_of_seats = input("Enter number of seats: ")
                vehicle = Car(registration_number, make, model, number_of_seats)
            elif vehicle_type == 'truck':
                cargo_capacity = input("Enter cargo capacity: ")
                vehicle = Truck(registration_number, make, model, cargo_capacity)
            elif vehicle_type == 'motorcycle':
                engine_capacity = input("Enter engine capacity: ")
                vehicle = Motorcycle(registration_number, make, model, engine_capacity)
            else:
                print("Invalid vehicle type. Please try again.\n")
                continue
            
            fleet.add_vehicle(vehicle)
        
        elif choice == '2':
            fleet.display_all_vehicles()
        
        elif choice == '3':
            registration_number = input("Enter the registration number of the vehicle to search for: ")
            fleet.search_vehicle_by_registration_number(registration_number)
        
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
