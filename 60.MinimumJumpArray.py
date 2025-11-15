#450 DSA
#Minimum Jump of Array

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

first = 0
jump = 0

while True :
    if arr[first] == 0 :
        break
    if arr[first] > len(arr[first : ]) :
        if arr[first] == arr[len(arr)-1] :
            break
        else :
            jump += 1
    else :
        jump += 1
        first += arr[first]

if jump == 0 :
    print(-1)
else :
    print(f"Minimum Jump is : {jump}")