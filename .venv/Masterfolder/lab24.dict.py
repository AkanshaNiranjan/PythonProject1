#dictionary
#mutable
#key:value
#{}

my_dict={"name":"akansha", "age":30, "company":"google", "account":"ICICI"}
print(my_dict)

#acesing value
print(my_dict["age"])


#changing value
my_dict["name"]="bittu"
print(my_dict)

#delete key
del my_dict["account"]
print(my_dict)

#Iterate
for key,value in my_dict.items():
    print(key,value)

#check is key present
print("age" in my_dict)

