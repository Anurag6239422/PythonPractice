#In this program I am using append or add Method

update_file = open(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\22.FileCreated.txt", "at")

contain = update_file.write("\n My name is Anurag Sandilya")

update_file.close()

print(contain)

# In This Program I am using "a" mode to create a file

file_create = open(r"C:\Users\anura_9posmze\Downloads\GIT\PythonPractice\29.FileCreated3.txt", "at")

file_create.write("This file is created using 'a' Mode \nThank You\nBye")

file_create.close()