#In this Program, we learn how finally block execute

try :
    read_file = open(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\33.FileCreated4.txt", "wt")

    contains = read_file.write("\nBye")

except Exception as file_error :
    print(f"You are doing Something Wrong : {file_error}")

# Else and finally block is option , but finally block must choose
#else :
#    print("If Try block Executed Successfully then only else block Execute")

finally :
    read_file.close()
    print(contains)