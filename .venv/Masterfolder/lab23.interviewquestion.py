#find the first non repeating character in a string using sets.

def non_rep(string):
    for i in string:
        if string.count(i)==1:
            return i
    return None
print(non_rep("swiss"))
print(non_rep("pepper"))
print(non_rep("dada"))