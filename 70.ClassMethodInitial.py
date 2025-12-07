'''
Docstring for 70.ClassMethodInitial

In this program we are using class Method in class method we use decorater which is @classmethod and this method is bound to class.
In Instance Method we pass argument as object but in class method we pass argument as class
'''

class Student:

    @classmethod
    def study(self):
        print(f"This Denote the Class : {self}")
        print("Student study 3 Hours a Day")


student1 = Student()

print(f"This is outside the class : {Student}")
print(f"This is object : {student1}")

student1.study() #Here, In this parameter we are passing class