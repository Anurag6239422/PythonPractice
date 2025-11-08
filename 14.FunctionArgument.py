#Multiple argument in single Parameter

def twoSum (*number) :  
#    print(f"The sum of {num1} and {num2} is : ", num1+num2) , If we pass like this then in that case it show error

    print(f"The Type of {number} is {type(number)}")
    print(f"The First value is {number[0]} and Second value is {number[1]}")
    print(f"The sum of {number[0]} and {number[1]} is : {number[0] + number[1]}")

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

twoSum (a, b) 

#Another Method Important method

def sum (*number) :
    
    sum = 0
    
    for num in number :
        sum += num

    print("The Sum of number is :", sum)

f_num = int(input("Enter the first number : "))
s_num = int(input("Enter the second number  : "))

sum(f_num, s_num)
