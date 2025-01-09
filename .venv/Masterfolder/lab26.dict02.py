#Dictionary from two lists

keys=["A","b","c"]
values=[2,4,34]

my_dict=dict(zip(keys,values))
print(my_dict)

#Merge two dictonary
dict1={'A': 2, 'b': 4, 'c': 34}
dict2={"f":6,"g":8,"w":1}
merge_dict=dict1|dict2
print(merge_dict)

#get a value
print(merge_dict.get("g"))