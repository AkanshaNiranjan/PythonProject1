#try except and else

try:
    a = int(input("enter num1"))
    b = int(input("enter num2"))
    c = a / b

except ZeroDivisionError as e:
    print(e)
except ValueError as e :
    print(e)
else:
    print("result is", c)
finally:

    print("end of code") #this code will run at every condition
    