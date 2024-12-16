from data import addData
from printE import printExpenses
from total import getTotal
from printRaw import printRawData

WELCOME_MESSAGE = "Expense Tracker V1"
print(WELCOME_MESSAGE)

NAME = input("What is your name? ")
Continue = True

def goodbye(NAME):
    return NAME + ", I hope you found the tool helpful!"

def main():
    global Continue    
    while Continue:
        print("MAIN MENU")
        print("="*40)
        print("[1] ADD DATA")
        print("[2] GET TOTAL")
        print("[3] PRINT EXPENSES")
        print("[4] QUIT")
        print("[5] PRINT RAW DATA")
        print("="*40)
        
        try:
            callDown = int(input())
        
        except ValueError: 
            print("That wasn't a valid number. Try again!")
        
        else:
            if callDown == 1:
                addData()
            elif callDown == 2:
                getTotal()
            elif callDown == 3:
                print("="*40)
                printExpenses()
                print("="*40)
            elif callDown == 4:
                print("*"*40)
                print(goodbye(NAME))
                with open("expenses.txt", "w") as file:
                    pass
                print("*"*40)
                Continue = False
            elif callDown == 5:
                print("*"*40)
                printRawData()
                print("*"*40)
        finally:
            print()
main()