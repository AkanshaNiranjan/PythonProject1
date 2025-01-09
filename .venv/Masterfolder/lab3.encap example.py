class bank:

    def __init__(self, account_number, balance):
        self.account_number=account_number
        self.__balance=balance

    def check_balance(self):
        print(self.__balance)

    def check_account_num(self):
        print(self.account_number)

icici=bank(123456,100)
print(icici.check_balance())
print(icici.check_account_num())
print(icici.account_number)