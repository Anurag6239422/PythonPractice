#450 DSA Cracker
#kth Smallest Term

number = int(input("How many element you want to enter : "))

list = []

for i in range (0, number) :
    no = int(input(f"Enter {i+1} : "))
    list.append(no)

#selection sort
i = 0
while i < len(list) - 1:
    for j in range(i+1, len(list)) :
        if list[i] > list [j] :
            list[i], list[j] = list[j], list[i]

    i += 1

print(list)

k = int(input("Enter Value : "))

mini = list[k-1]

print(mini)