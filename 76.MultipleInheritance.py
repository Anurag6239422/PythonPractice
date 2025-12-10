'''
Docstring for 76.MultipleInheritance

In this program , I learn Multiple Inheritance

Create classes:
Flyer (method fly())
Swimmer (method swim())
Walker (method walk())

Create class Athlete that inherits all three and call all abilities.
'''

class flyer:
    def __init__(self, wings):
        self.wings = wings

    def fly(self):
        return f"I can fly because I have {self.wings} wings"
    
class swimmer:
    def swim(self):
        return f"I can swim because i am a swimmer"
    
class walker:
    legs = 2

    def walk(self):
        return f"I can walk with my {walker.legs} legs"
    
class athelete(flyer, swimmer, walker):

    def __init__(self, wings):
        super().__init__(wings)

    def ability(self):
        return "I am a athelete because I can do all three things"
    
wings = int(input("How many wings do you have : "))
    
a1 = athelete(wings)

print(a1.fly())
print(a1.swim())
print(a1.walk())
print(a1.ability())