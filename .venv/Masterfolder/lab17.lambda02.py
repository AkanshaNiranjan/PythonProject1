#write a function to check its even or odd

def check(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
check(5)

#with lambda
check=lambda num: "Even" if num%2==0 else "odd"
print(check(18))