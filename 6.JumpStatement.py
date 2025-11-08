#Writing a code which print power of 2

n = int(input("Enter how much time you need to print power of 2 : "))

for i in range (1, n+1) :
    temp = i

    while temp % 2 == 0 :
        temp /= 2

    if temp == 1 :
        print(i)

#Continue Statement25


print("Here, We see the number which is not power of 2")

for i in range (1, n+1) :
    temp = i

    while temp % 2 == 0 :
        temp /= 2

    if temp == 1 :
        continue

    print(i)


#Break Statement

print("Here, We see only Break statement")

for i in range (1, n+1) :
    temp = i

    while temp % 2 == 0 :
        temp /= 2

    print(i)
    if temp != 1 :
        break

#Let's Understand through break statement

limit = int(input("How many Limit you want to set : "))

currsum = 0

while True :
    num = int(input("Enter the number ; "))

    if currsum + num > limit :
        print(currsum, "Limit Reached")
        break
    currsum += num