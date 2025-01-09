#Abstraction
#hide the details


from abc import ABC, abstractmethod


class animal(ABC):
    def __init__(self,name):
        self.name=name

    def  make_sound1(self):
        print("bark")

    @abstractmethod
    def make_sound2(self):
        pass

class elephant(animal):
    def make_sound3(self):
        print("bhooon...")

obj_animal=animal
obj_animal.make_sound1("bgheera")
obj_animal.make_sound2("cat")

obj_ani=elephant

obj_ani.make_sound3("ele")