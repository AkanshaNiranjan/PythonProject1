#try and except concept
#its a exception fix

#try:
#    #try this code if error
#except
#   #execute me if try has some error


#EXAMPLE

#a=int(input("enter num1"))  #value error- if string is entered the code will not run
#b=int(input("enter num2"))  #value error- if string is entered the code will not run
#c=a/b  #zero division error- if number is divided by 0, code will not run
#print("result is", c)


#try and except use
print("starting of code")
try:
    a = int(input("enter num1"))
    b = int(input("enter num2"))
    c = a / b
    print("result is", c)

except Exception as e:
    print(e)

print("end of code")