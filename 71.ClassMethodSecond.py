'''
Docstring for 71.ClassMethodSecond

Here, In this program we learn why we have to use class Method?
We use class method to access the class variable
'''

class Student:

    #class variable
    college_name = "LPU"
    departments = ["BCA", "MCA", "CSE", "Mechanical"]

    def __init__(self, hour):
        self.hour = hour

    def study(self) :
        print(f"Student study {self.hour} Hours a Day")

    @classmethod
    def student_info(self) :
        print(f"Student study in {self.college_name}")
        print("The Departments are : ")

        for department in self.departments :
            print(department)

student1 = Student

student1.student_info()
