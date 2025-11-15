#450 DSA
#Array Factorial Large Number

n = int(input("Enter the Number :"))

fact = 1

if n == 0 or n == 1 :
    print("[1]")

for i in range (2, n+1) :
    fact *= i

result = [int(x) for x in str(fact)]

print(result)