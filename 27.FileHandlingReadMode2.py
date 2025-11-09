#In this Program, We are reading Lines using Readlines Method

file_read = open(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\25.FileCreated2.txt", "rt")

lines = file_read.readlines() #It, Read Multiple line in a file 

file_read.close()

print(lines)
print(type(lines))

#Using Readlines Perfectly

file_read1 = open(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\25.FileCreated2.txt", "rt")

lines = file_read1.readlines()

file_read1.close()

for line in lines :
    print(line.rstrip('\n'))