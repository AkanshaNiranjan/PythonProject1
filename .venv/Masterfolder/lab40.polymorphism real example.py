#polymorphism
#over loading

class mathskill:
    def add(self,a=10,b=10):
        return a+b

    def add(self, a=0,b=0,c=0):
        return a+b+c

    def add(self,a=1,b=1,c=1,d=1):
        return a+b+c+d

math=mathskill()
print(math.add(1,2 ,33,44))
print(math.add(2,44))