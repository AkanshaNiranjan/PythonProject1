#custom exceptions



class LowBalanceExceptionCustom(Exception):

    def __init__(self,message):
        self.message= message
        super().__init__(message)

    balance=100
    withdraw=int(input("enter the withdraw amount"))
    if  withdraw > balance:
        raise LowBalanceExceptionCustom ("balance is low")
    else:
        print("balance", balance-withdraw)