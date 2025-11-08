# Pattern Printing 

num = int(input("Enter the number : "))

for row in range (1, num+1) :
    for column in range (1, row + 1) :
        print(column, end = ' ')

    print(end = '\n')

#Another Method using Space
print("**************************************************************************************************************************************************")

space = " "

for row in range (1, num + 1):
    for column in range (1, num + 1):
        if column <= row :
            print(column, end = ' ')
        else :
            print(space, end = ' ')
    
    print(end = '\n')
