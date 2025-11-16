#Kadane Algorithm in 2D Array

import sys

def kadaneAlgorithm (givenNums) :
    start = 0
    end = 0

    current_sum = 0
    max_sum = -sys.maxsize-1

    n = len(givenNums)

    while end < n :
        while current_sum < 0 :
            current_sum -= givenNums[start]
            start += 1

        current_sum += givenNums[end]
        end += 1

        max_sum = max(max_sum, current_sum)

    return max_sum


matrix = [[3,8,9,1,3],[-4,-1,1,7,-6],[-2,-3,8,1,-1]]

n = len(matrix)
m = len(matrix[0])

ans = -sys.maxsize-1

for i in range(m) :
    temp = [0] *n
    for j in range(n) :
        temp.append(matrix[j][i])
    
    ans = max(ans, kadaneAlgorithm(temp))

    for j in range (i+1, m) :
        for k in range (n) :
            temp[k] += matrix[k][j]

    ans = max(ans, kadaneAlgorithm(temp))

print(ans)
    
