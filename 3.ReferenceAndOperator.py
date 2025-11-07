#Let's Understand how data is store in main memory:

myvar = 10

print(f"myvar Value : {myvar},  In this location it is store in Main Memory : {id(myvar)}")

#In Python if two variable have same value, In that case we should share same location in main memory

myvar2 = 10

print(f"myvar2 Value : {myvar2}, This time myvar2 have also a same location in Main Memory : {id(myvar2)}")

myvar3 = 19

print(f"myvar3 Value : {myvar3}, This time myvar3 have different id in Main Memory because variable value has changed : {id(myvar3)}")

#Let's Understand with operators:

#Numeric

a = 17
b = 3

print(f"Sum is {a} + {b} :", a+b)
print(f"Subtraction is {a} - {b}:", a-b)
print(f"Multiplication is {a} * {b}:", a*b)
print(f"Division is {a} / {b}:", a/b)
print(f"Remainder is {a} % {b}:", a%b)
print(f"{a} to the power {b} is :", a**b)
print(f"Only integer value not float  value (Decimal Value in Division) is {a} // {b}:", a//b)

#Assignment

myvar4 = 17 #Equal to Operator

myvar4 += 3
print(f"+= Addition : ", myvar4)

myvar4 -= 3
print(f"-= Subtraction :", myvar4)

myvar4 *= 3
print(f"*= Multiplication :", myvar4)

myvar4 **= 3
print(f"**=, The power of 3 :", myvar4)

myvar4 /= 3
print(f"/= divison :", myvar4)

myvar4 %= 3
print(f'%= Modulus :', myvar4)

myvar4 //= 3
print(f"//= Floor Value :", myvar4)

#Comparitor Operator

a = int(input("Enter the First Number : "))
b = int(input("Enter the Second Number : "))

print(f"Result of {a} == {b} is : ", a==b)
print(f"Result of {a} > {b} is : ", a>b)
print(f'Result of {a} < {b} is : ', a<b)
print(f"Result of {a} >= {b} is : ", a>=b)
print(f"Result of {a} <= {b} is : ", a<=b)
#print(f"Result of {a} ! {b} is : ", a!b) 
print(f"Result of {a} != {b} is : ", a!=b)

#Logical Operator

c = int(input("Enter the Third Number : "))
d = int(input("Enter the fourth Number ; "))

print(f"{a} == {b} and {c} == {d} : ", a==b and c==d)
print(f"{a} == {b} or {c} == {d} : ", a==b or c==d)
print(f"not {c} == {d} : ", not c==d)