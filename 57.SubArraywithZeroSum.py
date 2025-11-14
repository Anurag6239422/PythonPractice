#450 DSA
#Sum of Sub Array will be zero
'''
number = int(input("Enter how many element you want to enter : "))
list1 = []

for i in range (0, number) :
    no = int(input(f"Enter {i+1} : "))
    list1.append(no)



'''

list1 = [4,2,-3,1,6]

current_value = list1[0]
overall_value = list1[0]

print(f"list : {list1}")
for i in range (1, len(list1)) :
    if current_value + list1[i] > list1[i] :
        current_value = current_value + list1[i]
        print(f"Current Value {i} : {current_value}")

    overall_value = min(list1[i], current_value)
    print(f"Overall Value {i} : {overall_value}")

'''
if overall_value == 0 :
    print("True")
else :
    print("False")
'''
