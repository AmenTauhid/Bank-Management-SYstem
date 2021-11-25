from random import randrange
import Account
import SavingAccount 
import ChecquingAccount
import typing
class BankInfo:


    def __init__(self):
        self._name = "Telemonical Co."
        self._accounts: typing.Dict[str, Account.BaseAccount()] = {}

        accNum1 = '4000218124421'
        user1 = SavingAccount.SavingAccount(accNum1,"Adam")
        self._accounts[accNum1] = user1
        accNum2 = '4000321262624'
        user2 = SavingAccount.SavingAccount(accNum2,"Miley")
        self._accounts[accNum2] = user2
        accNum3 = '400043523122'
        user3 = SavingAccount.SavingAccount(accNum3,"Chris")
        self._accounts[accNum3] = user3
        accNum4 = '400093623412'
        user4 = ChecquingAccount.ChecquingAccount(accNum4,"Philips")
        self._accounts[accNum4] = user4
        accNum5 = '400102435131'
        user5 = ChecquingAccount.ChecquingAccount(accNum5,"Sid")
        self._accounts[accNum5] = user5

   
    
    def openAccount(self,accHolderName):
        accNum = f'400{randrange(1e10):010}'
        account = Account.BaseAccount(accNum,accHolderName) 
        self._accounts[accNum] = account
        print(f"Your card number: {accNum}\n")
        return accNum

    def searchAccount(self,entered_card_number):

        key_list = list(self._accounts.keys())
        val_list = list(self._accounts.values())

        for i in range(len(self._accounts)):
            if key_list[i] == entered_card_number:
                return True
        return False

    def returnAccValue(self,accNum):
        val_list = list(self._accounts.values())
        key_list = list(self._accounts.keys())

        for i in range(len(self._accounts)):
            if key_list[i] == accNum:
                return val_list[i]


     
            

        