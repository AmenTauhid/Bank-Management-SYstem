class Account:
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

    def deposit():
        pass
    
    def withdraw():
        pass