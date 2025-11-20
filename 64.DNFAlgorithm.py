#450 DSA
#DNF (Dutuch National Flag) Algorithm
# Sorting of 0's,1's,2'nd without sort method

number = int(input("Enter how many element you want to enter : "))
list1 = []

for i in range (0, number) :
    no = int(input(f"Enter {i+1} : "))
    list1.append(no)

low = 0
mid = 0
high = len(list1) - 1

while mid <= high :
    if list1[mid] == 0 :
        list1[low], list1[mid] = list1[mid], list1[low]

        mid += 1
        low += 1
    
    elif list1[mid] == 1 :
        mid += 1

    else :
        list1[mid], list1[high] = list1[high], list1[mid]

        high -= 1

print(list1)