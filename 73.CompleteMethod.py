'''
Docstring for 73.CompleteMethod

In this program , I am going to do practice regarding 3 Method
1. Instance Method
2. Class Method
3. Static Method
'''

class Student:

    #Class Variable
    college_name = "LPU"
    departments = ['BBA','MBA','BCA','MCA','CSE']


    #Initializer
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    #Instance Method
    def student_info(self):
        print(f"The Name of Student is : {self.name}")
        print(f"The roll no of student is : {self.roll_no}")

    @classmethod
    def study(cls, hour) : #Here, cls means class we can use self also
        print(f"The Student study in {cls.college_name} College")
        print(f"Student will Study {hour} Hours a Day")

        print("The Departments are : ")
        for department in cls.departments:
            print(department)

    @staticmethod
    def greet():
        print("Welcome Student")

name = input("Enter Name : ")
roll_no = int(input("Enter Roll Number : "))
hour = int(input("Enter the hour : "))

student1 = Student(name, roll_no)

student1.student_info()
student1.study(hour)
student1.greet()

        