#450 DSA
#Move Negative array from list

number = int(input("Enter how many element you want to enter : "))
list1 = []

for i in range (0, number) :
    no = int(input(f"Enter {i+1} : "))
    list1.append(no)
end = list1[number-1]
i =0

while list1[i] != end:
    if list1[i] < 0 :
        temp = list1[i]
        for j in range (i, number-1) :
            list1[j] = list1[j + 1]
        
        list1[number-1] = temp

        if i == 0 :
            i = 0
        else :
            i -= 1
    else :
        i += 1

print(list1)
