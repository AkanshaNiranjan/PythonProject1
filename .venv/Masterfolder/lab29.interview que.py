#check vowels in a string

my_string="akanshaniranjan"

vowels="aeiou"
vowels_count=0

for i in my_string:
    if i in vowels:
        vowels_count=vowels_count+1
print(vowels_count)
