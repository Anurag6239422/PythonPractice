'''
Docstring for 68.InitMethodBasic
In this program we learn __init__ Method .

In this method it helps to intialize and creating an object.
'''

class Student:
    def __init__(self):
        print("Initializing and Creating an Object")

    def study (self, hour):
        print(f"The Student Study {hour} Hour a Day")

    
student1 = Student()