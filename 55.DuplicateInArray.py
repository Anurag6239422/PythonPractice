#450 DSA
#Duplicate in array

number = int(input("Enter how many element you want to enter : "))
list1 = []

for i in range (0, number) :
    no = int(input(f"Enter {i+1} : "))
    list1.append(no)

value = 0
seen = set()

for x in list1 :
    if x in seen:
        value = x
        break
    seen.add(x)
    
'''
for i in range(0, len(list1)-1) :
    for j in range(i+1, len(list1)) :
        if list1[i] == list1[j] :
            value = list1[i]
            break
'''


print(f"Duplicate Value is {value}")