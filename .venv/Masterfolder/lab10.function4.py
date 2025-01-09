#create a number to sum of three number from the user input

number1=int(input("enter number1\n"))
number2=int(input("enter number2\n"))
number3=int(input("enter number3\n"))

def sum_of_3numbers(n1=100,n2=200,n3=300):
    return n1+n2+n3
num=sum_of_3numbers(number1,number2,number3)
print(num)

num=sum_of_3numbers()
print(num)


