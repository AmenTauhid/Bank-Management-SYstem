import Bank
class BaseAccount:
    def __init__(self,accNum,accHolderName):
        self._accountNumber = accNum
        self._accHolderName = accHolderName
        self._rateOfInterest = 0
        self._currentBalance = 0
    
    def getAccountNumber(self):
        return self._accountNumber
    
    def getAccountHolderName(self):
        return self._accHolderName

    def getRateofInterest(self):
        return self._rateOfInterest

    def getCurrentBalance(self):
        return self._currentBalance

    def deposit(self,depositMoney):
        try:
            self._currentBalance += (depositMoney + (depositMoney*self._rateOfInterest/100))
        except ValueError:
            return 'Not a valid deposit!'

    def withdraw(self,withdrawMoney):
        self._currentBalance = self._currentBalance - withdrawMoney
