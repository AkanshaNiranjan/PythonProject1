#Multilevel Inheritance
#grandfather->father->son

class grandfather:
    gold1="1bhk"

    def property(self):
        car="alto"
        house="1BHK"
        print(car,house)

class father(grandfather):
    gold2="2kg"

    def property1(self):
        car="figo"
        house="2bhk"
        print(car,house)

class daughter(father):
    diamond="1c"

    def property2(self):
        car="seltos"
        house="3bhk"
        print(car,house)

g=grandfather()
print(g.gold1)
g.property()

f=father()
print(f.gold2)
f.property1()
f.property()

d=daughter()
print(d.diamond)
d.property()
d.property2()
d.property1()

