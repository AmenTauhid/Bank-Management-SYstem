import os
import time
import sys
import Bank
import Account
class MainProgram:

    def source(self,entered_card_number):
        self.setAccNum(entered_card_number)
                
    def showMainMenu(self):

        menuPart = MainProgram()
        print("######################################")
        print('        - 1) Open new Account -       ')
        print('         - 2) Select Account -        ')
        print('           - 3) Go back -             ')
        print("######################################")

        alpha = Bank.BankInfo()

        while True:
            choice2 = str(input("Please enter the number beside the option you desire to do:\n>"))
            l1 = ["1","2","3"]
            while choice2 != l1:
                if choice2 == "1":
                    accHolderName = input("Please enter in the account holder name:\n>")
                    alpha.openAccount(accHolderName) #This function is still a bit faulty
                    #print(f"Your card number: {alpha.openAccount()}\n")
                    break
                if choice2 == "2":
                    entered_card_number = str(input("Please enter the valid account number you wish to work on:\n>"))
                    menuPart.setAccNum(entered_card_number)
                    if alpha.searchAccount(entered_card_number) is True:
                        time.sleep(2)
                        print('You have successfully logged in!')
                        time.sleep(2)
                        menuPart.showAccountMenu()
                    elif alpha.searchAccount(entered_card_number) is False:
                        print('Wrong card number')
                elif choice2 == "3":
                    menuPart.run()
                else:
                    choice2 = str(input("Invalid entry!!\nPlease enter the valid number beside the option you desire to do:\n>"))
    
    @classmethod
    def setAccNum(self,entered_card_number):
        self._cardNum = entered_card_number
        return self._cardNum 

    def showAccountMenu(self):
        print("######################################")
        print('         - 1) Check Balance -        ')
        print('            - 2) Deposit -           ')
        print('           - 3) Withdraw  -          ')
        print('            - 4) Go back -           ')
        print("######################################")
        accPart = MainProgram()
        alpha = Bank.BankInfo()
        accNum = accPart._cardNum      
        
        accName = alpha.returnValue(accNum)
        while True:
            choice = str(input("Please enter the number beside the option you desire to do:\n>"))
            l1 = ["1","2","3","4"]
            while choice != l1:
                if choice == "1":
                    balance = accName.getCurrentBalance()
                    print(f"Your current balance: {balance}\n")
                    break
                elif choice == "2":
                    depositMoney = int(input("Enter the amount of money you wish to deposit:\n>"))
                    accName.deposit(depositMoney)
                    break
                elif choice == "3":
                    withdrawMoney = int(input("Enter the amount of moeny you wish to withdraw:\n>"))
                    accName.withdraw(withdrawMoney)
                    break
                elif choice == "4":
                    accPart.showMainMenu()
                else:
                    choice = str(input("Invalid entry!!\nPlease enter the valid number beside the option you desire to do:\n>"))

    def run(self):
        runPart =MainProgram()
        os.system('cls')
        print('######################################')
        print('# Welcome to Telemonical Co. Bank ! # ')
        print("######################################")
        print('           - 1) Main Menu -           ')
        print('         - 2) About the Bank -        ')
        print('             - 3) Exit -              ')
        print("######################################")
        choice3 = str(input("Please enter the number beside the option you desire to go to:\n>"))
        l1 = ["1","2","3"]
        while choice3 != l1:
            if choice3 == "1":
                runPart.showMainMenu()
            elif choice3 == "2":
                runPart.aboutBank()
            elif choice3 == "3":
                sys.exit()
            else:
                choice3 = str(input("Invalid entry!!\nPlease enter the valid number beside the option you desire to go to:\n>"))

    def aboutBank(self):
        print("There's nothing about this bank, you cannot go back from here :)")
              

runMode = MainProgram()
runMode.run()