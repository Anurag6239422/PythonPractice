#Two Sum Problem

number = int(input("Enter how many element you want to enter : "))
list1 = []

for i in range (0, number) :
    no = int(input(f"Enter {i+1} : "))
    list1.append(no)

k = int(input("Enter the Target : "))

list1.sort()

start = 0
end = len(list1) - 1

'''
i = 0

while i < len(list1) :
    if list1[start] == list1[end] and list1[start] + list1[end] != k :
        print("Sorry ! Unable to find it")
        break
    if list1[start] + list1[end] > k:
        end -= 1
    else :
        if list1[start] == list1[end] :
            print(f"Two Sum Value : {list1[start]},{list1[end]}")
            break
        else :
            start += 1


'''
found = False
while start < end :
    total = list1[start] + list1[end]

    if total > k :
        end -= 1

    elif total == k :
        print(f"The Two sum is : {list1[start], list1[end]}")
        found = True
        break
    else :
        start += 1

if not found :
    print("Sorry, Unable to find Two sum of given list")