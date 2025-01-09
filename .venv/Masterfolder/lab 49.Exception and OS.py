import os

print(os.getcwd())  #get current directory


#get list of directory
files=os.listdir('\Users\AKANSHA\PycharmProjects\PythonProject\.venv\Scripts\python.exe')
print(files)

#create a new directory
os.mkdir("test2")


#check if a file exist
file_exist=os.path.exists("akansha.txt")
print(file_exist)