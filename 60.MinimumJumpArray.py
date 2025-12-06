#450 DSA
#Minimum Jump of Array

number = int(input("Enter how many element you want to enter : "))
list1 = []

for i in range (0, number) :
    no = int(input(f"Enter {i+1} : "))
    list1.append(no)
'''
This is the best code but does not pass multiple test case

next_value = 0
step = 0
count = 0
updated_index = 0

while next_value < len(list1) :
    if next_value == len(list1) - 1:
        break
    
    step = list1[next_value]

    if step <= 0 :
        print(f"Sorry, Unable to jump : {count}")

    updated_index = step + next_value
    next_value = updated_index
    count += 1

print("Total Count :", count)


'''

n = len(list1)

if n <= 1 :
    print(0)

if list[0] == 0 :
    print(-1)

step = list1[0]
updated_index = list1[0]
count = 1

for i in range (1, n):
    if i == n-1 :
        print("Minimum Count Jump : ", count)

    updated_index = max(updated_index, i+list1[i])

    step -= 1

    if step == 0 :
        count += 1
        if i >= updated_index :
            print("Minimum Jump : -1")

        step = updated_index - i

        
