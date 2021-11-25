import Account

class ChecquingAccount(Account.BaseAccount):
    def __init__(self,accNum,accHolderName):
        super().__init__(accNum,accHolderName)
        self._overdraftAllowed = 5000
        self._rateOfInterest = 5

    def withdraw(self,withdrawMoney):
        if self._currentBalance > withdrawMoney:
            self._currentBalance = self._currentBalance - withdrawMoney
            return True
        elif self._currentBalance < withdrawMoney:
            self._currentBalance = (self._currentBalance + self._overdraftAllowed) - withdrawMoney
            self._overdraftAllowed = 0
            return True
        elif self._currentBalance < 0 and self._overdraftAllowed == 0:
            return False
        