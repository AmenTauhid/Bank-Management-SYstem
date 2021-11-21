import os
import time
import sys
import Bank
import Account

class mainProgram:
    def showMainMenu():
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
                    alpha.openAccount(accHolderName)
                    break
                elif choice2 == "2":
                    #print(alpha._accounts)
                    entered_card_number = input("Please enter the valid account number you wish to work on:\n>")
                    if alpha.searchAccount(entered_card_number) is True:
                        print('You have successfully logged in!')
                        mainProgram.showAccountMenu()
                    elif alpha.searchAccount(entered_card_number) is False:
                        print('Wrong card number')
                elif choice2 == "3":
                    mainProgram.run()
                else:
                    choice2 = str(input("Invalid entry!!\nPlease enter the valid number beside the option you desire to do:\n>"))

    def showAccountMenu():
        print("######################################")
        print('          - 1) Check Balance -        ')
        print('             - 2) Deposit -           ')
        print('            - 3) Withdraw  -          ')
        print('             - 4) Go back -           ')
        print("######################################")
        while True:
            choice = str(input("Please enter the number beside the option you desire to do:\n>"))
            l1 = ["1","2","3","4"]
            while choice != l1:
                if choice == "1":
                    #TODO: Check Balance
                    pass
                elif choice == "2":
                    #TODO: Deposit
                    pass
                elif choice == "3":
                    #TODO: Withdraw
                    pass
                elif choice == "4":
                    mainProgram.showMainMenu()
                else:
                    choice = str(input("Invalid entry!!\nPlease enter the valid number beside the option you desire to do:\n>"))

    def run():
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
                mainProgram.showMainMenu()
            elif choice3 == "2":
                mainProgram.aboutBank()
            elif choice3 == "3":
                sys.exit()
            else:
                choice3 = str(input("Invalid entry!!\nPlease enter the valid number beside the option you desire to go to:\n>"))

    def aboutBank():
        #TODO: for fun :)
        pass

mainProgram.run()