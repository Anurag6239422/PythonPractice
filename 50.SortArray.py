#450 DSA 
#sort the array without using sort method

number = int(input("Enter the number which you want to insert : "))

list1 = []

for i in range (0, number) :
    no = int(input(f"Enter {i + 1} : "))
    list1.append(no)

for i in range (0, number - 1) :
    for j in range (i+1, number):
        if list1[i] > list1[j] :
            list1[i], list1[j] = list1[j], list1[i]

print(f"Sorted List : {list1}")

