class baseAccount:
    def __init__(self,accNum,accHolderName):
        self._accountNumber = accNum
        self._accHolderName = accHolderName
        self._rateOfInterest = 15
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
        self._currentBalance = depositMoney + (depositMoney*self._rateOfInterest/100)
        pass
    
    def withdraw(self,withdrawMoney):
        self._currentBalance -= withdrawMoney
        pass