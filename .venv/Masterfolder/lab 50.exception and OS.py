#File reading with python


#write mode
file_name="bittu.txt"
content= "bittu is a 30 years old girl"

with open(file_name,"w") as file:
       file.write(content)

#read mode
with open(file_name,"r")as file:
    content2=file.read()
    print(content2)