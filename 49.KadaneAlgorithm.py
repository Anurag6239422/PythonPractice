#450 DSA Cracker
#Kadane Algorithm


number = int(input("Enter the number : "))

list = []

for i in range (0, number) :
    no = int(input(f"Enter {i+1} : "))

    list.append(no)

current_value = list[0]
overall_value = list[0]

i = 1

while i < len(list):
    if current_value + list[i] > list[i] :
        current_value = current_value + list[i]
    else :
        current_value = list[i]

    overall_value = max(overall_value, current_value)

    i += 1

print(current_value)

    