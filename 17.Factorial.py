#Factorial Program using recurssion

def factorial(num) :

    if num == 0 or num == 1:
        return 1

    else :
       return num * factorial(num-1)

    

number = int(input("Enter the number of which you want factorial : "))

result = factorial(number)

print(result)