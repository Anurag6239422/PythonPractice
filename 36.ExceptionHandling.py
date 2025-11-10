#Exception Handling using try and except block

num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number : "))

try :
    result = num1 / num2
    print(result)
    
except Exception as e :
    print(f"The Error you are is : {e}")