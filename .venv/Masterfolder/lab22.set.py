#collection of unique
#{} - parenthesis
#immutable
#no duplicates
#no order

#SET
num1={1,2,3,4,4,4,6,5}
print(num1)

#union
num1={2,3,4,5,6}
num2={5,6,7,8,9}
numbers=num1.union(num2)
print(numbers)

#intersection
num1={2,3,4,5,6}
num2={5,6,7,8,9}
numbers=num1.intersection(num2)
print(numbers)

#difference
num1={2,3,4,5,6}
num2={5,6,7,8,9}
numbers=num1.difference(num2)
print(numbers)
numbers=num2.difference(num1)
print(numbers)