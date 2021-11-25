import Account
class SavingAccount(Account.BaseAccount):
    def __init__(self,accNum,accHolderName):
        super().__init__(accNum,accHolderName)
        self._minimumBalance = 5000
        self._rateOfInterest = 10
    
    def withdraw(self,withdrawMoney):
        if self._currentBalance > self._minimumBalance:
            self._currentBalance = self._currentBalance - withdrawMoney
            return True
        else:
            return False
        
    