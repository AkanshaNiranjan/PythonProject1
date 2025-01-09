#ENCAPSLATION
#hide your data members
#by using __ , we can hide the member


class person:

    def __init__(self):
        self.password ="123" #public variable, available to all
        self.__password_secure="pass123"  #private variable #availble in class only

    def password1(self):
        print(self.password)

loginpass=person()
loginpass.password1()
loginpass.password1()

print(loginpass.password)
print(loginpass.__password_secure)