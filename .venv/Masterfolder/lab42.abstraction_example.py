#real example

from abc import ABC , abstractmethod

class excel(ABC):

    @abstractmethod
    def start(self):
        pass


class browser(excel):

    @abstractmethod
    def start(self):
        pass

class testcase(browser):

    def start(self):
        print("starting")

    def stop(self):
        print("stopping")

    def TC1(self):
        self.start()
        self.stop()

obj_ref=testcase()
obj_ref.TC1()