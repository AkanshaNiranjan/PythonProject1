#oops example

class FBLogin:

    def __init__(self, email ,password ):
        self.email=email
        self.password = password

    def login_confirm(self):
        if (self.email=="akansha@" and self.password=="bittu"):
            print("login successful")
        else:
            print("login failed")


email1=input("enter your email")
pass1=input("enter your password")

fbloginnew= FBLogin(email1,pass1)
fbloginnew.login_confirm()


