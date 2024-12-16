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
    print("[5] Entertainment")
    print("[6] Savings")
    print("Enter the Category ID, a brief description, and the amount spent, separated by '-'. To stop entering data, type 'QUIT'.")
    while not quit:
        print("–" * 40)
        data = input()
        
        if data.upper() == "QUIT":
            quit = True
            continue
        
        with open("expenses.txt", "a") as file:
            file.write(data + "\n")
        
        try:
            parts = data.split("-")
        
            if len(parts) != 3:
                print("Invalid format. Please enter data as 'Category ID - Description - Amount'.")
                continue
            
            category_ID = int(parts[0].strip()) 
            description = parts[1].strip()
            costA = parts[2].strip()
            cost = float(costA.replace("$", "").strip())
        
            if category_ID == 1:
                housingExpenses.append([description, cost])
            elif category_ID == 2:
                foodExpenses.append([description, cost])
            elif category_ID == 3:
                transportationExpenses.append([description, cost])
            elif category_ID == 4:
                insuranceExpenses.append([description, cost])
            elif category_ID == 5:
                entertaimentExpenses.append([description, cost])
            elif category_ID == 6:
                savingsExpenses.append([description, cost])
            else:
                print("Invalid category ID. Please use numbers between 1 and 6.")
        
        except ValueError as e:
            print(f"Error processing input: {e}. Ensure the data is correctly formatted.")
