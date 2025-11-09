#Writing a code of File Handling using with statement

with open(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\29.FileCreated3.txt", "rt") as file_handler :
    contain = file_handler.read()

    print(contain)

#We can use w, x, r, a mode using with Statement
#Making only code with w mode

with open(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\25.FileCreated2.txt", "wt") as file_handler2 :
    file_handler2.write("My Name is Anurag Sandliya\nI work in CoreCard as QA Engineer")
