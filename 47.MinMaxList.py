#450 DSA Cracker
#Min and Max in List

number = int(input("How many number you want to enter in a list : "))

list = []
list1 = []

for i in range (0, number) :
    no = int(input(f"Enter {i+1} : "))
    list.append(no)

print(f'List = {list}')

mini = list[0]
maxi = list[0]

for i in range (1, number) :
    if mini > list[i] :
        mini = list[i]

    maxi = max(maxi,list[i])  #Here, using Max Method

    '''
    if maxi < list[i] :
        maxi = list[i]
    '''
'''
There, is another way also using sort method
list.sort()
mini = list[0]
maxi = list[len(list) - 1]
'''
list1.append(mini)
list1.append(maxi)

print(list1)