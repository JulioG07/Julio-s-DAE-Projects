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