#Conditional Statement

#if Condition Only

n = int(input("Enter the number : "))

#In that case if condition is fullfilled it will return both condition
if n % 2 == 0 :
    print("It is divisible by 2")

print("It is not divible by 2")

#Else If Condition 

n = int(input("Enter the number once again : "))

#In that Condition If Condition is not fullfilled it automatically moved to Else Condition
if n % 2 == 0 :
    print("It is divisible by 2")
else :
    print("It is not divisible by 2")

#elif Condition

n = int(input("Enter the number once again : "))

#In that case if condition is not fullfilled then it moved to Elif Condition then it moved to else condition
if n % 2 == 0 :
    print("It is divisible by 2")
elif n % 3 == 0 :
    print("It is divisible by 3")
else :
    print("Nither it is divisible 2 nor divisiblke by 3")

#Conditional Statement with logical Operator
if n % 2 == 0 :
    print("It is Divisible by 2")
elif n % 2 != 0 and n % 3 == 0 : #We can use OR operatorn also instead of and operator
    print("It is perfect divisible by 3")
else :
    print("It is nither divisible by 2 nor divisible by 3")