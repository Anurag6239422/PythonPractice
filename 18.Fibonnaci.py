#Fibonnaci using recursion

def fibonacci(x) :

    if x == 1  or x == 2 :
        return 1
    
    else :
        return fibonacci(x-1) + fibonacci(x-2)
    
number = int(input("Enter the number : "))

result = fibonacci(number)
print(f"The Sum of Fibonacci series is {result}")
