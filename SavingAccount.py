import Account
class SavingAccount(Account.BaseAccount):
    def __init__(self,accNum,accHolderName):
        super().__init__(accNum,accHolderName)
        self._minimumBalance = 5000
        self._rateOfInterest = 15
    
    def withdraw(self,withdrawMoney):
        pass