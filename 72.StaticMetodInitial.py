'''
Docstring for 72.StaticMetodInitial

In this program we learn Static Method , Static Method is a Method which is not bound to the class nor with the object.

To use static Method we use decorator @staticmethod
'''

class Student:

    def __init__(self, name, roll_no, hour):
        self.name = name
        self.roll_no = roll_no
        self.hour = hour


    @staticmethod
    def greet(): #For, Static we don't need to pass self parameter
        '''
        Docstring for study

        print(f"My name is {name}") 
        
        Here, I understand that static  method is not 
        related to class and object if we have to tell name we have to pass self but it static method we don't need it

        '''
        print("Welcome Student")


name = input("Enter the name : ")
roll_no = int(input("Enter the Roll No : "))
hour = int(input("Enter the Hour : "))

student1 = Student(name, roll_no, hour)

student1.greet()