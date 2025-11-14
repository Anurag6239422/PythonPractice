#450 DSA
#Sum of Largest Number of factorial

def factorial (n) :
    if n == 1 :
        return 1
    return n * factorial(n-1)

number = int(input("Enter the number : "))

result = factorial (number)

rem = 0
list2 = []

for i in range (len(str(result))) :
    rem = result % 10
    list2.append(rem)
    result = result // 10
list2.reverse()

print(list2)