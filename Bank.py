from random import randrange
from typing import Dict
import Account
import sys

class BankInfo:
    def __init__(self):
        self._name = "Telemonical Co."
        self._accounts: Dict[str, Account.baseAccount] = {}
    
    def openAccount(self,accHolderName):
        newAccNum = f'400000{randrange(1e10):010}'
        newAcc = Account.baseAccount(newAccNum,accHolderName)
        self._accounts[newAccNum] = newAcc
        print(f"Your card number: {newAccNum}\n")


    def searchAccount(self,entered_card_number):
        if entered_card_number in self._accounts:
            #print('You have successfully logged in!')
            return True
        else:
            return False
            #print('Wrong card number')
            

        