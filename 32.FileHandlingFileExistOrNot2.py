#If file does not exist , In that case it will create it
from pathlib import Path

file_exist = Path(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\33.FileCreated4.txt")

if file_exist.exists() :
    print("This file is exist")
else :
    with open(file_exist, "xt") as file_created :
        file_created.write("This file is created if not exist\nThank You!\nBye")