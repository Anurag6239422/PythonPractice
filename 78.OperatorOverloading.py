'''
Docstring for 78.OperatorOverloading

In this program, I learn operator overloading lin "+" plus operator with integer it work different with string it will work different in oops language both are class.

integer:
2+2 = 4
String:
hi+Hello = hiHello

both contain __add__() (Dunder Add Method) but when I create a class in that class have no dunder method then on that case it shows an error we can create our own dunder add 
method and that method is known as Operator overloading.

'''

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
    def __add__(self,other):  #Here, other means R2 which is another object and R1 is self object
        return self.length + other.length
    
length = int(input("Enter the Length : "))
breadth = int(input("Enter the breadth : "))
    
r1 = Rectangle(length, breadth)

print(r1.area())

length1 = int(input("Enter the Length : "))
breadth1 = int(input("Enter the breadth :"))

r2 = Rectangle(length1, breadth1)

print(r2.area())

print(r1+r2) #Here, we are overloading the plus operator
        