#Pattern Printing

num = int(input("Enter the number : "))

space = ' '

for row in range (num, 0, -1) :
    for column in range (1, num + 1):
        if column >= row :
            print("*", end = ' ')
        else :
            print(space, end = " ")
    
    print(end = "\n")
    
