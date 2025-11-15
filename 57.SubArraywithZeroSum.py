#450 DSA
#Sum of Sub Array will be zero

number = int(input("Enter how many element you want to enter : "))
list1 = []

for i in range (0, number) :
    no = int(input(f"Enter {i+1} : "))
    list1.append(no)
'''
for i in range (0, len(list1)-1) :
    current_value = list1[i]
    for j in range (i+1, len(list1)) :
        if current_value + list1[j] == 0 or list1[j] == 0:
            count += 1
            break
        else :
            current_value = current_value + list1[j]

if count > 0 :
    print("True")
else :
    print("False")

'''

is_sum_zero = False

prefix_sum = 0

seen = set()

for num in list1 :
    prefix_sum += num

    if prefix_sum == 0 or prefix_sum in seen or num == 0 :
        is_sum_zero = True
        break

    seen.add(prefix_sum)

print(is_sum_zero)

