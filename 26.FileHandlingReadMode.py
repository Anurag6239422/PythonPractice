#File Handling Read Method

file_Read = open(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\22.FileCreated.txt", "rt")

content = file_Read.read()

file_Read.close()

print(content)

#Using Read Method in another Way

print('###################################################################################################################')

file_Read2 = open(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\22.FileCreated.txt", "rt")

content2 = file_Read2.read(10) #Here, 10 means Read only 10 character

file_Read2.close()

print(content2)

#Using ReadLine method which read whole line of a file in a single row.

print("#####################################################################################################################")

file_Read3 = open(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\25.FileCreated2.txt", "rt") #Read the text

line1 = file_Read3.readline()
line2 = file_Read3.readline() #This takes automatically next line 
line3 = file_Read3.readline(3) #Here, 3 means  3 Character of Line 3

file_Read3.close()

print(f"This is a line 1 of a file : {line1}")
print(f"This is a line 2 of a file : {line2}")
print(f"The 3 Character of a line 3 of a file : {line3}")

#Using ReadLine method which read whole line of a file in a single row.

print("#####################################################################################################################")

file_Read4 = open(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\25.FileCreated2.txt", "rt") #Read the text

line1 = file_Read4.readline()
line2 = file_Read4.readline() 
line3 = file_Read4.readline()
line4 = file_Read4.readline() #Line 3 is EOF(End of File) still Line 4 do not throw error
line5 = file_Read4.readline() #Line 3 is EOF(End of File) still Line 5 do not throw error

file_Read4.close()

print(f"This is a line 1 of a file : {line1}")
print(f"This is a line 2 of a file : {line2}")
print(f"This is a line 3 of a file : {line3}")
print(f"The Line 4 does not exist in a file : {line4}")
print(f"The line 5 does not exixt in file : {line5}")