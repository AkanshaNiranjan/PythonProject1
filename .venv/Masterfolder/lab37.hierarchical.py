#Hierarchical inheritance

class father:
    car="alto"

    def property1(self):
        home1="1bhk"
        print(home1)

class son(father):
    car1="figo"

    def property2(self):
        home="2bhk"
        print(home)

class son1(father):
    car2="s"
    def property3(self):
        home2="bhk"
        print(home2)

s=son()
print(s.car1)
print(s.car)
s.property1()
s.property2()

s1=son1()
print(s1.car)
print(s1.car2)
s1.property1()
s1.property3()