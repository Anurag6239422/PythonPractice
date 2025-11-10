#Exception Handling File Error

try :
    read_file = (r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\33.FileCreated4.txt", "wt")

    contains = read_file.read()

    read_file.close()
    
    print(contains)

except Exception as file_error :
    print(f"You are doing Something Wrong : {file_error}")

else :
    print("If Try block Executed Successfully then only else block Execute")

finally :
    print("Whatever happen try block executed successfully or not , finally block must execute")