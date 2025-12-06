'''
Docstring for 67.ClassInstanceMethod

In this code we learn that when we create a Instance Method on that time we need to argument because when we create an object and call a Instance method on that time 
by default python code with pass object as argument.

object_name and self both address will be same.

'''

class Student :
    def study(self) :
        print("The self Address : ", self)
        return "The Student Study 3 Hour a Day"
    
    def studyFunctionWithArgument(self, hour) : #Here, we pass parameter as hour and self where self take object
        print(f"The student study {hour} Hours a Day")
    
student1 = Student()

print("The Student Address : ", student1)
print(student1.study())

hour = int(input("Enter the Hour : "))

student1.studyFunctionWithArgument(hour)

