#Three Sum Problem

number = int(input("Enter how many element you want to enter : "))
list1 = []

for i in range (0, number) :
    no = int(input(f"Enter {i+1} : "))
    list1.append(no)

k = int(input("Enter the Target : "))

list1.sort()

start = 0
end = len(number) - 1
found = False

for i in range (0, len(list1)-2) :
    start = i + 1
    end = len(list1) - 1
    while start < end :
        total = list1[i] + list1[start] + list1[end]

        if total == k :
            print(f"The Total Sum of three Number : {list1[i], list1[start], list1[end]}")
            found = True
            break
        elif total > k :
            end -= 1
        else :
            start += 1

if not found :
    print("Sorry Unable to find the three element of List")
