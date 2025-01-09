#include dict into list

my_dict={"name":"akansha", "age":30, "company":"google", "account":"ICICI"}
my_dict1={"name":"rajan", "age":34, "company":"cienna", "account":"ICICI"}
my_dict3={"name":"bagheera", "age":3, "company":"amrapali", "account":"NIL"}

my_list=[my_dict,my_dict1,my_dict3]
print(my_list)
print(my_list[0])
print(my_list[0]["age"])
print(my_list[2]["company"])

