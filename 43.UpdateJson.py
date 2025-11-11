#By using Update Method We can Update the json file

import json

student = {}

number = int(input("How many data you want to enter : "))

for i in range (0, number) :
    student_number = input("Enter the student Number : ")

    student_data = {}
    for j in range (0, 3) :
        key = input("Enter the Key : ")
        value = input("Enter the value : ")

        student_data[key] = value

    student[student_number] = student_data

with open(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\42.DictionaryData.json", "r") as file_Handler :
    data = file_Handler.read()


key1 = input("Which Student Number you want : ")
key2 = input("Which thing you want to update : ")
Value = input("What is the update one : ")

if key1 in student and key2 in student[key1]:
    student[key1][key2] = Value

#Here, Updating the value

data.update(student)

#After Update we have to dump Again

with open(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\42.DictionaryData.json", "w") as file_handler1 :
    json.dump(student, file_handler1, indent=4)
