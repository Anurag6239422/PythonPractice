'''
Docstring for 69.InitMethond

Here, we learn actual Reason why we need __init__() method .
The reason is that if we create two object which have almost name arrtibutes but value willl be change on that case we don't have to add attributes all time we have to create 
__init__() method and in __init__() method we pass self which take object and object can we different.
'''

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    
    def study(self, hour) :
        print(f"The student will study {hour} Hours a  Day")

    def student_Info(self) :
        print(f"The Name of Student is {self.name}")
        print(f"The Roll No of student is {self.roll_no}")

name = input("Enter the Name : ")
roll_no = int(input("Enter the Roll Number : "))
hour = int(input("Enter the Hour : "))

student1 = Student(name, roll_no)

student1.student_Info()
student1.study(hour)