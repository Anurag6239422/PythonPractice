'''
Docstring for 74.SingleLevelInheritance

In this program we learn single level Inheritance where we create single Base/Parent class and single Derived/Child class.
vechile = Base Class
car = Child Class
'''

class vechile:
    company = "xyz Motors"

    def __init__(self, n_wheels, n_seats, milage):
        self.n_wheels = n_wheels
        self.n_seats = n_seats
        self.milage = milage

    def details(self):
        return f"This Vechile have {self.n_wheels} wheels , {self.n_seats} seats and have {self.milage} Milage"
    
class car(vechile):
    pass

wheel = int(input("Enter Wheels : "))
seat = int(input("Enter Seat : "))
milage = int(input("Enter Milage : "))

car1 = car(wheel, seat, milage) #Here, we are passing class argument (wheel, seat, milage)

print(car1.company) #Here, we are accessing the parent class variable
print(car1.details()) #Here, we are accessing the parent class method