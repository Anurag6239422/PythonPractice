#Here, we learn Return Keyword using Function

def twoSum (*number) :
    sum = 0

    for num in number :
        sum += num

    return sum

f_num = int(input("Enter the first number : "))
s_num = int(input("Enter the second number : "))

result = twoSum(f_num, s_num)
result1 =  twoSum(f_num, s_num, 8)

print("The sum is : ", result)
print("The sum is : ", result1)

#If we write return keyword , function automatically terminate

def sum (*number) :
    sum = 0

    return sum

    print("After Return Terminate")

a = int(input("Enter the number : "))

print(sum (a))