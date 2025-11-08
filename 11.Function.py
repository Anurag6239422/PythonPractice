#Function Program

#Defining

def fun() :                 #Note: First we have to define function
    print("Hello World")

#Calling
fun()  #Here, we are calling

#Now, we use Function Program in different way, using parameter

def twoSum (num1 , num2) :  #Here, we call num1 and num2 is Parameter
    print(f"The sum of {num1} and {num2} is : ", num1+num2)

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

twoSum (a, b) #Here, we call a and b is Argument
twoSum (15, 15)