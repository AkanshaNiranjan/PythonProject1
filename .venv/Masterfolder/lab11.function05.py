n1= input("enter name\n")
n2=input("enter surname\n")

def name(na1="akansha", na2="niranjan"):
    return na1 + na2
fullname=name(n1,n2)
print(fullname)

fullname=name()
print(fullname)



#functions with *args

def numbers(*num):
    for i in num:
        print(i)
num1=numbers(1,2,3)
print(num1)