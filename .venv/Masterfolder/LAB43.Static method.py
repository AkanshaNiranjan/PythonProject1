#static method

class excelreader():

    @staticmethod
    def start():
        print("starting")

class browser(excelreader):
    def tc1(self):
        excelreader.start()


obj_ref=browser()
obj_ref.tc1()