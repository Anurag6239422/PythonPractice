'''
Docstring for 77.MultilevelInheritance

In this program, I learn Multilevel Inheritance
create a grandparent class = vechile
create a parent class = car
create a child class electric_car
'''

class vechile:
    company_name = "xyz Motors"

    def __init__(self, n_wheel, n_seats, milage):
        self.n_wheel = n_wheel
        self.n_seats = n_seats
        self.milage = milage

    def vechile_info(self):
        return f"This car have {self.n_wheel} wheels , {self.n_seats} seats and {self.milage} Milage"
    
class car(vechile) :
    model = "ABC123"

    def __init__(self, car_name, car_type, n_wheel, n_seats, milage):
        self.car_name = car_name
        self.car_type = car_type
        super().__init__(n_wheel, n_seats, milage)

    def car_info(self):
        return f"Car Name = {self.car_name}\nCar Type = {self.car_type}"
    
class electric_car(car):
    def __init__(self, battery_capacity, distance_range, car_name, car_type, n_wheel, n_seats, milage):
        self.battery_capacity = battery_capacity
        self.distance_range = distance_range
        super().__init__(car_name, car_type, n_wheel, n_seats, milage)

    def electric_car_info(self):
        return f"This car have {self.battery_capacity} battery capacity and cover {self.distance_range}"
    
battery_capacity = int(input("Enter the Battery Capacity : "))
distance_range = int(input("Enter how many distance this will cover in kms : "))
car_name = input("Enter the car name : ")
car_type = input("Either it is Manual/Automation : ")
n_wheel = int(input("Enter the number of wheels : "))
n_seats = int(input("Enter the number of seats : "))
milage = int(input("Enter the Mialge : "))

ec1 = electric_car(battery_capacity, distance_range, car_name, car_type, n_wheel, n_seats, milage)

print(ec1.company_name)
print(ec1.vechile_info())
print(ec1.model)
print(ec1.car_info())
print(ec1.electric_car_info())