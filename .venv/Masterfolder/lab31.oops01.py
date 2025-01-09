#with __init__

class person():
    # attributes
    name = None
    age = None
    weight = None


    def __init__(self, name ,age):
        self.name=name
        self.age=age

    # Behaviour
    def sleep(self):
        print(sleep)

    def walk(self):
        print(walk)



person1=person("akansha",30)
print(person1.name)
print(person1.age)

person2=person("bittu",15)
print(person2.name)
print(person2.age)