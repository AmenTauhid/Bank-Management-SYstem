from random import randrange
import Account
import SavingAccount 
import ChecquingAccount
import typing
class BankInfo:

    """
    def __init__(self):
        self._name = "ABC Bank"
        self._accounts = []

        accNum1 = '123456'
        accName1 = "Adam"
        accNum2 = '124124'
        accName2 = "Miles"
        accNum3 = '523122'
        accName3 = "Chris"
        accNum4 = '623412'
        accName4 = "Miley"
        accNum5 = '435131'
        accName5 = "Siddy"
        
        self._accounts.append(SavingAccount.SavingAccount(accNum1[0],accName1[0]))
        self._accounts.append(SavingAccount.SavingAccount(accNum2[1],accName2[1]))
        self._accounts.append(SavingAccount.SavingAccount(accNum3[2],accName3[2]))
        self._accounts.append(ChecquingAccount.ChecquingAccount(accNum4[3],accName4[3]))
        self._accounts.append(ChecquingAccount.ChecquingAccount(accNum5[4],accName5[4]))
    """    


    def __init__(self):
        self._name = "Telemonical Co."
        self._accounts: typing.Dict[str, Account.BaseAccount()] = {}

        accNum1 = '123456'
        user1 = SavingAccount.SavingAccount(accNum1,"Adam")
        self._accounts[accNum1] = user1
        accNum2 = '124124'
        user2 = SavingAccount.SavingAccount(accNum2,"Miley")
        self._accounts[accNum2] = user2
        accNum3 = '523122'
        user3 = SavingAccount.SavingAccount(accNum3,"Chris")
        self._accounts[accNum3] = user3
        accNum4 = '623412'
        user4 = ChecquingAccount.ChecquingAccount(accNum4,"Philips")
        self._accounts[accNum4] = user4
        accNum5 = '435131'
        user5 = ChecquingAccount.ChecquingAccount(accNum5,"Sid")
        self._accounts[accNum5] = user5
   
    '''
    def openAccount(self,accHolderName):
        accNum = f'400{randrange(1e10):010}'
        account = Account.BaseAccount(accNum,accHolderName) 
        self._accounts[accNum] = account
        print(f"Your card number: {accNum}\n")
    '''
         
    """
    def searchAccount(self,entered_card_number,):
        
        #if entered_card_number in self._accounts:
        #    return True 
        #else:
        #    return False
    
        for i in self._accounts:
            if self._accounts == entered_card_number: 
                return True
        return False
    """

    def searchAccount(self,entered_card_number):

        key_list = list(self._accounts.keys())
        val_list = list(self._accounts.values())

        for i in range(len(self._accounts)):
            if key_list[i] == entered_card_number:
                return True
        return False
    
    def returnValue(self,accNum):
        val_list = list(self._accounts.values())
        key_list = list(self._accounts.keys())

        for i in range(len(self._accounts)):
            if key_list[i] == accNum:
                return val_list[i]


     
            

        