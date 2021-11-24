import Account

class ChecquingAccount(Account.BaseAccount):
    def __init__(self,accNum,accHolderName):
        super().__init__(accNum,accHolderName)
        self.overdraftAllowed = 5000
        self._rateOfInterest = 5

    def withdraw(self,withdrawMoney):
        pass