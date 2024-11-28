main.py:
-------
from data import addData
from printE import printExpenses
from total import getTotal

print("Expense Tracker V1")
name = input("What is your name? ")
Continue = True

while Continue:
    print("MAIN MENU")
    print("="*40)
    print("[1] ADD DATA")
    print("[2] GET TOTAL")
    print("[3] PRINT EXPENSES")
    print("[4] QUIT")
    print("="*40)
    callDown = int(input())
    
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
        print(name + ", I hope you found the tool helpful!")
        print("*"*40)
        Continue = False

data.py:
-------
housingExpenses = []
foodExpenses= []
transportationExpenses = []
insuranceExpenses = []
entertaimentExpenses= []
savingsExpenses = []

def addData():
    quit = False
    print("CATEGORIES:")
    print("[1] Housing")
    print("[2] Food & Groceries")
    print("[3] Transportation")
    print("[4] Insurance")
    print("[5] Entertaiment")
    print("[6] Savings")
    print("Enter the Category ID, a brief description, and the amount spent, separated by '-'. To stop entering data, type 'QUIT'.")
    while not quit:
        print("–"*40)
        data = input()
        print("–"*40)
        if data.upper() == "QUIT":
            quit = True
            continue
        
        parts = data.split("-")
        category_ID = int(parts[0])
        description = parts[1]
        costA = parts[2]
        cost = float(costA.replace("$",""))
            
        if(category_ID == 1):
            housingExpenses.append([description, cost])
        elif(category_ID == 2):
            foodExpenses.append([description, cost])
        elif(category_ID == 3):
            transportationExpenses.append([description, cost])
        elif(category_ID == 4):
            insuranceExpenses.append([description, cost])
        elif(category_ID == 5):
            entertaimentExpenses.append([description, cost])
        elif(category_ID == 6):
            savingsExpenses.append([description, cost])

total.py:
--------
from data import housingExpenses
from data import foodExpenses
from data import transportationExpenses
from data import insuranceExpenses
from data import entertaimentExpenses
from data import savingsExpenses

def getTotal():
    total = 0
    subTotal1 = 0
    subTotal2 = 0
    subTotal3 = 0
    subTotal4 = 0
    subTotal5 = 0
    subTotal6 = 0
    print("—"*40)
    for entry in housingExpenses:
        price = entry[1]
        subTotal1 += price
        total += price
    print("Housing: $", subTotal1)
    for entry in foodExpenses:
        price = entry[1]
        subTotal2 += price
        total += price
    print("Food & Groceries: $", subTotal2)
    for entry in transportationExpenses:
        price = entry[1]
        subTotal3 += price
        total += price
    print("Transportation: $", subTotal3)
    for entry in insuranceExpenses:
        price = entry[1]
        subTotal4 += price
        total += price
    print("Insurance: $", subTotal4)
    for entry in entertaimentExpenses:
        price = entry[1]
        subTotal5 += price
        total += price
    print("Entertaiment: $", subTotal5)
    for entry in savingsExpenses:
        price = entry[1]
        subTotal6 += price
        total += price
    print("Savings: $", subTotal6)
    print("—"*40)
    print("TOTAL MONEY SPENT: $", total)
    print("="*40)

printE.py:
---------
from data import housingExpenses
from data import foodExpenses
from data import transportationExpenses
from data import insuranceExpenses
from data import entertaimentExpenses
from data import savingsExpenses

def printExpenses():
    print(f"{'House Expenses':<15} {'Amount ($)':>10}")
    print("–"*40)
    for entry in housingExpenses:
        descript, price = entry
        print(f"{descript:<15} {price:>10}")
    print("\n")
    print(f"{'Food Expenses':<15} {'Amount ($)':>10}")
    print("–"*40)
    for entry in foodExpenses:
        descript, price = entry
        print(f"{descript:<15} {price:>10}")
    print("\n")
    print(f"{'Transportation':<15} {'Amount ($)':>10}")
    print("–"*40)
    for entry in transportationExpenses:
        descript, price = entry
        print(f"{descript:<15} {price:>10}")
    print("\n")
    print(f"{'Insurance':<15} {'Amount ($)':>10}")
    print("–"*40)
    for entry in insuranceExpenses:
        descript, price = entry
        print(f"{descript:<15} {price:>10}")
    print("\n")
    print(f"{'Entertaiment':<15} {'Amount ($)':>10}")
    print("–"*40)
    for entry in entertaimentExpenses:
        descript, price = entry
        print(f"{descript:<15} {price:>10}")
    print("\n")
    print(f"{'Savings':<15} {'Amount ($)':>10}")
    print("–"*40)
    for entry in savingsExpenses:
        descript, price = entry
        print(f"{descript:<15} {price:>10}")
    print("\n")

