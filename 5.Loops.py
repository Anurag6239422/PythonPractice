#Loops

for i in range (5):
    print(i)

#****************************************************************************************************************************************************************

#Now, Understand by loop is Necessary
#Sum of N Natural Number

n = int(input("Enter the number : "))

sum = 0

for i in range (n) :
    sum += i + 1

print(f"Sum of {n} natural number is : ", sum)

#*****************************************************************************************************************************************************************

#Range Method

start = int(input("From Which you want to start : "))
stop = int(input("From which you want to stop : "))

#range method : range(start, stop, step)
for i in range (start, stop, 2) :
    print(i)

#******************************************************************************************************************************************************************

#let's do few more thing using for loop

n = int(input("Enter the number : "))

for i in range (n) :
    print("0*", end = '')

print(end='\n')
#Another way to do it 

for j in range (n+1) :
    if j % 2 == 0 :
        print("0", end = '')
    else :
        print("*", end = '')
print(end='\n')