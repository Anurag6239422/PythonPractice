#450 DSA
#Union and Intersection

number1 = int(input("Enter how many element you want to enter in list1: "))
number2 = int(input("Enter how many element you want to enter in list2: "))

list1 = []
list2 = []

for i in range (0, number1) :
    no1 = int(input(f"Enter {i+1} : "))
    list2.append(no1)

for i in range (0, number2) :
    no2 = int(input(f"Enter {i+1} : "))
    list2.append(no2)

intersection = []

for x in list1 :
    for y in list2 :
        if x == y and y not in intersection:
            intersection.append(x)

result = list1 + list2

union = []

for x in result :
    if x not in union :
        union.append(x)

print(f"Union : {union}")
print(f"Intersection : {intersection}")