#In this program we learn different Data Type and Variable
#Numeric

a = 10
b = 7.5
c = 1 + 5j

print(f"Variable Value : {a}, Type : {type(a)}")
print(f"Variable Value : {b}, Type : {type(b)}")
print(f"Variable Value : {c}, Type : {type(c)}")

#Sequential Data Type

d = "Anurag"
e = [10, 15, 'A', 1.5, 5 + 8j, [16, 12]]

print(f"Variable Value : {d}, Type : {type(d)}")
print(f"Variable Value : {e}, Type : {type(e)}")

#There are Few more Variable in a Python :
#1. Tuple
#2. Sets
#3. Dictionary

#Let's Understand How to take input from user:

myvar = input("Enter Something : ")

print(f"myvar Value : {myvar}, myvar Type : {type(myvar)}") #By Default it take String to convert into integer we have to do type cast

myvar2 = int(input("Enter Something : "))

print(f"myvar2 Value : {myvar2}, myvar2 Type : {type(myvar2)}")