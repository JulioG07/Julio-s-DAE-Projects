def printRawData():
    with open("expenses.txt", "r") as file:
        for line in file:
            print(line.strip())