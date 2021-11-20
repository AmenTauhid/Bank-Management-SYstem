from random import randrange
from typing import Dict
import Account
import sys

class BankInfo:
    def __init__(self):
        self._name = "Telemonical Co."
        self._accounts: Dict[str, Account.Account] = {}
    
    def openAccount(self,accHolderName):
        newAcc = f'400000{randrange(1e10):010}'
        self._accounts[newAcc] = newAcc
        print(f"Your card number: {newAcc}\n")


    def searchAccount(self,entered_card_number):
        for i in range(3):
            if entered_card_number != self._accounts:
                print('Wrong card number')
            else:
                print('You have successfully logged in!')
                break

        