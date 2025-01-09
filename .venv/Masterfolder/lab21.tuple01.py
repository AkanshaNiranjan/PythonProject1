#in - is item included in tuple

names = ("bittu", "rajan","aka")
print("bittu" in names)

#append in tuples does not happen.
#change a tuple into list then add a item
name1=list(names)
name1.append("niranjan")
n1=tuple(name1)
print(n1)

