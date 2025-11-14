#450 DSA
#Maximum Product of Sub Array Element

number = int(input("Enter how many element you want to enter : "))
list1 = []

for i in range (0, number) :
    no = int(input(f"Enter {i+1} : "))
    list1.append(no)


'''
Do it but Time Complexity is High

previous_value = 0

i = 0

while i < number :
    current_value = 1
    for j in range (i, len(list1)) :
        current_value = current_value * list1[j]

        if current_value > previous_value :
            previous_value = current_value

    i += 1

'''

max_product = list1[0]
min_product = list1[0]
overall_product = list1[0]

for i in range (1, number) :
    if list1[i] < 0 :
        max_product, min_product = min_product, max_product

    max_product = max(list1[i], max_product * list1[i])
    min_product = min(list1[i], min_product * list1[i])
    overall_product = max(overall_product, max_product)

print(f"The Maximum Product of Sub Array : {overall_product}")