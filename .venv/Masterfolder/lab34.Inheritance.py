#single inheritance

class father:
    key="2bhk"

    def property(self):
        car="figo"
        print(car)

class daughter(father):
    key="3bhk"

    def property1(self):
        car="seltos"
        print(car)

father.obj=father()
father.obj.property()

daughter.obj=daughter()
daughter.obj.property1()
daughter.obj.property()