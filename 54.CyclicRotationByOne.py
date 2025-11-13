#450 DSA
#Cyclic Rotation by kth term

number = int(input("Enter how many element you want to enter : "))
k = int(input("How many term you want to rotate : "))
list1 = []

for i in range (0, number) :
    no = int(input(f"Enter {i+1} : "))
    list1.append(no)

i = 0

while i < k :
    temp = list1[0]

    for j in range(0, len(list1)-1) :
        list1[j] = list1[j+1]
        
        list1[len(list1)-1] = temp

    i += 1

print(f"After {k}th term : {list1}")