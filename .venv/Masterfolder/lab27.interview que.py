#frequency of character in a string

string=str(input("enter the input"))

char={}
for i in string:
    char[i]=char.get(i,0)+1
print(char)