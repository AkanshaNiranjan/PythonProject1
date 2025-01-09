#sort a dict in ascending and descending order
dict1={"a":5,"b":2,"c":3,"d":1}
#in ascending order
for i in sorted(dict1.values()):
    print(i)


#in descending order
dict1={"a":5,"b":2,"c":3,"d":1}

output = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))

print(output)





#remove a duplicate value from dict

my_dict={"a":1,"b":2,"c":1,"d":4}

unique_value= set()
result={}

for key,value in my_dict.items():
    if value not in unique_value():
        result[key]=value
        unique_value.add(value)
print(result)



