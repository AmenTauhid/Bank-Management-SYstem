import Account
class SavingAccount(Account.BaseAccount):
    def __init__(self,accNum,accHolderName):
        super().__init__(accNum,accHolderName)
        self._minimumBalance = 5000
        self._rateOfInterest = 15
    
    def deposit(self, depositMoney):
        return super().deposit(depositMoney)

    def withdraw(withdrawMoney):
        pass