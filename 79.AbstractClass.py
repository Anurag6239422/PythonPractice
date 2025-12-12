'''
Docstring for 79.AbstractClass
It contain two file to learn Abstract class
'''

from my_abstract_class import shape

class square(shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side ** 2
    
class rectangle(shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
sqr1 = square(10)
print(sqr1.area())

rect1 = rectangle(6,5)
print(rect1.area())


c1 = circle(10)
print(c1.area())