#multiple inheritance

class father:
    car="alto"

    def property1(self):
        home1="1bhk"
        print(home1)

class mother:
    car1="figo"

    def property2(self):
        home="2bhk"
        print(home)

class son(father,mother):

    car2="seltos"
    def print_info(self):
        print("son")

s=son()
print(s.car1)
s.property2()
s.property1()
print(s.car)