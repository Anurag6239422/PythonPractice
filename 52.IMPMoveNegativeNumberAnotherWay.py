#450 DSA
#Move Negative Number in more efficient way

number = int(input("Enter how many element you want to enter : "))
list1 = []

for i in range (0, number) :
    no = int(input(f"Enter {i+1} : "))
    list1.append(no)

temp = []

for x in list1 :
    if x >= 0 :
        temp.append(x)

for x in list1 :
    if x < 0 :
        temp.append(x)

for i in range (0, len(list1)) :
    list[i] = temp[i]

print(list1)