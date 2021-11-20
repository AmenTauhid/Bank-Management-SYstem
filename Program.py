import os
import time
import sys

class mainProgram:
                
    def showMainMenu():
        print("######################################")
        print('        - 1) Open new Account -         ')
        print('         - 2) Select Account -      ')
        print('           - 3) Go back -            ')
        print("######################################")
        choice = str(input("Please enter the number beside the option you desire to do:\n>"))
        l1 = ["1","2","3"]
        while choice != l1:
            if choice == "1":
                #TODO: open account
                pass
            elif choice == "2":
                choice2 = 0
                while choice2 <= 0:
                    choice2 = int(input("Please enter the valid account number you wish to work on:\n>")) # this part of the method is on trial right now, will implement it correctly later on.
                    if choice2 >= 0:
                        mainProgram.showAccountMenu()
                    else:
                        choice2 = int(input("Invalid entry!!\n Entered account number is either invalid or doesn't exist\nPlease enter the valid account number you wish to work on:\n>"))
            elif choice == "3":
                mainProgram.run()
            else:
                choice = str(input("Invalid entry!!\nPlease enter the valid number beside the option you desire to do:\n>"))
        pass

    def showAccountMenu():
        print("######################################")
        print('          - 1) Check Balance -         ')
        print('             - 2) Deposit -      ')
        print('            - 3) Withdraw  -            ')
        print('             - 4) Go back -            ')
        print("######################################")
        choice = str(input("Please enter the number beside the option you desire to do:\n>"))
        l1 = ["1","2","3","4"]
        while choice != l1:
            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
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
        print('           - 1) Main Menu -         ')
        print('         - 2) About the Bank -      ')
        print('             - 3) Exit -            ')
        print("######################################")
        choice = str(input("Please enter the number beside the option you desire to go to:\n>"))
        l1 = ["1","2","3"]
        while choice != l1:
            if choice == "1":
                mainProgram.showMainMenu()
            elif choice == "2":
                mainProgram.aboutBank()
            elif choice == "3":
                sys.exit()
            else:
                choice = str(input("Invalid entry!!\nPlease enter the valid number beside the option you desire to go to:\n>"))

    def aboutBank():
        #TODO: for fun :)
        pass

mainProgram.run()