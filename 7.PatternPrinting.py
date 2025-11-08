#Printing a Pattern

n = int(input("Enter the Row no. : "))
m = int(input("Enter the Column no. : "))

for i in range (1, n+1) :
    for j in range (1, m+1):
        print(j, end = " ")

    print(end='\n')