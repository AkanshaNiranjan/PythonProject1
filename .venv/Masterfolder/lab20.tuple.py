#tuple
#collection of items
#()
#immutable-can not be changed


mytuple=(4,6,5,"bittu")
print(mytuple)

#change list into tuple
t1=tuple([4,6,5,"bittu"])
print(t1)

#add a tuple in tuple
t1=(4,6,5,"bittu")
t2=(7,2,1,"nir")
mytuple=(t1,t2)
print(mytuple)

#indexing
t1=(4,6,5,"bittu")
t2=(7,2,1,"nir")
mytuple=(t1,t2)
print(mytuple[0])
print(mytuple[0][0])