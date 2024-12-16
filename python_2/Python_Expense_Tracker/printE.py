from data import housingExpenses
from data import foodExpenses
from data import transportationExpenses
from data import insuranceExpenses
from data import entertaimentExpenses
from data import savingsExpenses

def printExpenses():
    print(f"{'House Expenses':<15} {'Amount ($)':>10}")
    print("–"*40)
    if not housingExpenses:
            print("NO EXPENSES")
    for entry in housingExpenses:
        descript, price = entry
        print(f"{descript:<15} {price:>10}")
    print("\n")
    print(f"{'Food Expenses':<15} {'Amount ($)':>10}")
    print("–"*40)
    if not foodExpenses:
            print("NO EXPENSES")
    for entry in foodExpenses:
        descript, price = entry
        print(f"{descript:<15} {price:>10}")
    print("\n")
    print(f"{'Transportation':<15} {'Amount ($)':>10}")
    print("–"*40)
    if not transportationExpenses:
            print("NO EXPENSES")
    for entry in transportationExpenses:
        descript, price = entry
        print(f"{descript:<15} {price:>10}")
    print("\n")
    print(f"{'Insurance':<15} {'Amount ($)':>10}")
    print("–"*40)
    if not insuranceExpenses:
            print("NO EXPENSES")
    for entry in insuranceExpenses:
        descript, price = entry
        print(f"{descript:<15} {price:>10}")
    print("\n")
    print(f"{'Entertaiment':<15} {'Amount ($)':>10}")
    print("–"*40)
    if not entertaimentExpenses:
            print("NO EXPENSES")
    for entry in entertaimentExpenses:
        descript, price = entry
        print(f"{descript:<15} {price:>10}")
    print("\n")
    print(f"{'Savings':<15} {'Amount ($)':>10}")
    print("–"*40)
    if not savingsExpenses:
            print("NO EXPENSES")
    for entry in savingsExpenses:
        descript, price = entry
        print(f"{descript:<15} {price:>10}")
    print("\n")