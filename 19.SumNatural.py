#Sum of Natural Number using Recursion

def naturalSum(n) :

    if n == 1 or n == 0 :
        return 1
    else :
        return n + naturalSum(n-1)
    
number = int(input("Enter the number of which you want sum : "))

result = naturalSum(number)

print(f"The Sum of {number} natural number is {result}")