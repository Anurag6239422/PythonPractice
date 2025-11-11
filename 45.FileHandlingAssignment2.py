#Assignment 2

'''Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file
'''
import os

try :
    with open(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\25.FileCreated2.txt", "rt") as file_handler :
        while True :
            data = file_handler.readline()

            if data == "" :
                with open(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\25.FileCreated2.txt", "at") as file_handler1 :
                    Data = input("Enter the line : ")
                    file_handler1.write(f"\n{Data}\n")

                break
    with open(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\25.FileCreated2.txt", "rt") as file_handler2 :
        data1 = file_handler2.read()

    print(data1)
    
except Exception as e :
    print(e)
