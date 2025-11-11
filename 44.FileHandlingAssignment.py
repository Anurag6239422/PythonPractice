#Assignment 1
'''
Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''
import os

try :
    i = 0
    with open(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\25.FileCreated2.txt", "rt") as file_Handler :
        while True :
            data = file_Handler.readline()

            if data =="" :
                break

            print(f"Line {i+1} : {data}")

            i += 1

except Exception as e :
    print(e)

        
