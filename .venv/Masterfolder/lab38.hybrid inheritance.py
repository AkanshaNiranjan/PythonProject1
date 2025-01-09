#hybrid inheritance

#diff types of inheritance
#like single
#multiple
#multilevel
#hierarchical


class father:
    key="2bhk"

    def property(self):
        car="figo"
        print(car)



class mother:
    car1="figo"

    def property2(self):
        home="2bhk"
        print(home)



class daughter(father,mother):
    key="3bhk"

    def property2(self):
        home="2bhk"
        print(home)


class son(daughter):
        car2 = "seltos"

        def print_info(self):
            print("son")



