#To handle the Json 

import json

student = {}

student_number = int(input("How many Student Data you want to enter : "))

for i in range (0, student_number) :
    student_no = input("Enter the Student : ")
    
    student_data = {}
    for j in range(0, 3) :
        k1 = input("Enter Key : ")
        v1 = input("Enter Value : ")

        student_data[k1] = v1

    student[student_no] = student_data

#Dump all Dictionary Data in Json Format


with open(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\42.DictionaryData.json", "w") as file_handler : #Not using x mode because file is already Created
    json.dump(student, file_handler, indent=4)

#To reada json Data we use load Methon

with open(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\42.DictionaryData.json", "r") as file_handler1 : #Not using x mode because file is already Created
    contains = json.load(file_handler1)

print(contains)
print(type(contains))