#Cpu example


from abc import ABC,abstractmethod

class CPU():

    def computer(self):
        pass

    @staticmethod
    def load_os():
        print("loading os")


    def mouse(self):
        print("start mouse")

    def headphone(self):
        print("using headphone")


class motherboard(CPU):
    @abstractmethod
    def startmotherboard(self):
        print("starting")

class RAM(CPU):
     @abstractmethod
     def startRAM(self):
         print("starting")

class processor(CPU):
    @abstractmethod
    def startprocessor(self):
        print("starting processor")

class storage(CPU):
    def storagedate(self):
        print("stogaedatallimit")



obj_ref=storage()
obj_ref.storagedate()
obj_ref.mouse()
obj_ref.headphone()
CPU.load_os()


