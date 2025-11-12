#450 DSA Cracker
#Reverse a Array

number = int(input("How Many number you want enter in a array : "))

list1 = []

for i in range(0, number) :
    no = int(input(f"Enter Value {i}: "))

    list1.append(no)


#Here, we start Reverse the array or list

print("Array : ",list1)

first = 0
last = len(list1) - 1

while first < last :
    list1[first], list1[last] = list1[last], list1[first]

    first += 1
    last -= 1

#There is another way to reverse the array, using sort method
#list1.sort()

'''
There is another way also using loop and using athmetic operation to reverse the array

while first < last :
    list1[first] = list1[first] + list1[last]
    list1[last] = list1[first] - list1[last]
    list1[first] = list1[first] - list1[last]
'''

print("Reverse Array : ",list1)
