#list
#[]

mylist=["bittu", 3,8,"nir"]
print(mylist)
print(mylist[0])

#Append=add a item to the end of list

mylist.append("akansha")
mylist.append(7)
print(mylist)

#extend-append a new list
mylist.extend([8,9,"rajan"])
print(mylist)

#insert-add a item in middle of a list

mylist.insert(2,"niranjan")
print(mylist)

print(len(mylist))

#remove-remove a item from list

mylist.remove(9)
print(mylist)

#sort
list1=[0,30,21,5,7]
list1.sort()
print(list1)

#pop- it will remove the last item of the list
list1.pop()
print(list1)