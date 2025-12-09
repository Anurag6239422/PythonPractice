'''
Docstring for 75.SingleLevelInheritanceSecond

In this program we learn what happen if we need to use __init__() method in parent class as well as derived class
'''

class Vechile:
    company = "xyz Motors"

    def __init__(self, n_wheel, n_seats, milage):
        self.n_wheel = n_wheel
        self.n_seats = n_seats
        self.milage = milage

    def vechile_info(self):
        return f"This vechile have {self.n_wheel} wheels , {self.n_seats} seats and {self.milage} milage"
    
class bike(Vechile):
    def __init__(self, name, n_wheel, n_seats, milage) :
        self.name = name
        super().__init__(n_wheel, n_seats, milage)

    def bike_name(self) :
        return f"The Name of Bike is {self.name}"
    
name = input("Enter the Name of Bike : ")
n_wheel = int(input("Enter the number of wheel : "))
n_seats = int(input("Enter the number of seats : "))
milage = int(input("Enter the milage of a Bike : "))


vechile1 = Vechile(n_wheel, n_seats, milage)

print(vechile1.vechile_info())


b1 = bike(name, n_wheel, n_seats, milage)

print(b1.bike_name())
print(b1.vechile_info())


'''
Output:
Enter the Name of Bike : BMW
Enter the number of wheel : 2
Enter the number of seats : 1
Enter the milage of a Bike : 25
This vechile have 2 wheels , 1 seats and 25 milage
The Name of Bike is BMW
This vechile have 2 wheels , 1 seats and 25 milage

'''
    