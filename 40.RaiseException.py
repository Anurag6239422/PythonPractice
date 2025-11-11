#By using Raise Keyword we can throw exception

salary = float(input("Enter a salary : "))

if salary < 0 :
    raise ValueError("Salary cannot be negative")
else :
    print(f"Your Salary is {salary}")