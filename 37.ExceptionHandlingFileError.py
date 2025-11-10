#Eception Handling regarding File error

try :
    with open(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\25.FileCreated22.txt", "rt") as read_file :
        data = read_file.read()

        print(data)

except Exception as file_error :
    print(f"You are doing Something Wrong : {file_error}")