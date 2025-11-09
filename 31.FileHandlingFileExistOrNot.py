#Checking File Exist or Not

import os

file_name = r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\25.FileCreated2.txt"

if os.path.exists(file_name) :
    print("File Exists")
else :
    print("File Does Not Exists")

#Another Method

print("###############################################################################################################")

from pathlib import Path

file_name1 = Path(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\25.FileCreated2.txt")

if file_name1.exists() :
    print("File Exists")
else :
    print("File Does Not Exists")

