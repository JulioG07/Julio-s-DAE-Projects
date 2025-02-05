# In this file, the generateClass() function serves the porpuse of generating 
# the classes that the user is currrently enrolled in
average = 0

def generate_Classes():
    #global methoud allows you to use variables in another files 
    global average
    global newAverage 


    # Create an empty list to store class names
    class_array = []


    # Get input for each class, up to a maximum of 8
    for i in range(1, 9):
        class_name = input(f"Enter the name of class {i} (or enter 'done' to finish): ")
        
        # Check if the user entered 'done' to stop input
        if class_name.lower() == 'done':
            break
        
        # Append allows you to display your array 
        class_array.append(class_name)

    #Gets the array's lenght
    amountOfClasses = len(class_array)

    # Prints the list of classes
    print("\nYou are currently enrolled in" , amountOfClasses , "classes:")
    print("")
 
    
    for class_name in class_array:
        print(class_name)
    

    print("\nEnter your grade for the respective classes that you are taking:")
    print("")
    if amountOfClasses == 8:
        score1 = float(input(class_array[0] + ": "))
        score2 = float(input(class_array[1] + ": "))
        score3 = float(input(class_array[2] + ": "))
        score4 = float(input(class_array[3] + ": "))
        score5 = float(input(class_array[4] + ": "))
        score6 = float(input(class_array[5] + ": "))
        score7 = float(input(class_array[6] + ": "))
        score8 = float(input(class_array[7] + ": "))

        average = float(score1 + score2 + score3 + score4 + score5 + score6 + score7 + score8) / 8
        newAverage = round(average,2)
        print("\nOverall average: " , newAverage)
        print("")
        print("*******************************************************")

    elif amountOfClasses == 7:
        score1 = float(input(class_array[0] + ": "))
        score2 = float(input(class_array[1] + ": "))
        score3 = float(input(class_array[2] + ": "))
        score4 = float(input(class_array[3] + ": "))
        score5 = float(input(class_array[4] + ": "))
        score6 = float(input(class_array[5] + ": "))
        score7 = float(input(class_array[6] + ": "))

        average = float(score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7
        newAverage = round(average,2)
        print("\nOverall average: " , newAverage)
        print("")
        print("*******************************************************")


    elif amountOfClasses == 6:
        score1 = float(input(class_array[0] + ": "))
        score2 = float(input(class_array[1] + ": "))
        score3 = float(input(class_array[2] + ": "))
        score4 = float(input(class_array[3] + ": "))
        score5 = float(input(class_array[4] + ": "))
        score6 = float(input(class_array[5] + ": "))

        average = float(score1 + score2 + score3 + score4 + score5 + score6) / 6
        newAverage = round(average,2)
        print("\nOverall average: " , newAverage)
        print("")
        print("*******************************************************")


    elif amountOfClasses == 5:
        score1 = float(input(class_array[0] + ": "))
        score2 = float(input(class_array[1] + ": "))
        score3 = float(input(class_array[2] + ": "))
        score4 = float(input(class_array[3] + ": "))
        score5 = float(input(class_array[4] + ": "))

        average = float(score1 + score2 + score3 + score4 + score5) / 5
        newAverage = round(average,2)
        print("\nOverall average: " , newAverage)
        print("")
        print("*******************************************************")

    elif amountOfClasses == 4:
        score1 = float(input(class_array[0] + ": "))
        score2 = float(input(class_array[1] + ": "))
        score3 = float(input(class_array[2] + ": "))
        score4 = float(input(class_array[3] + ": "))

        average = float(score1 + score2 + score3 + score4) / 4
        newAverage = round(average,2)
        print("\nOverall average: " , newAverage)
        print("")
        print("*******************************************************")

    elif amountOfClasses == 3:
        score1 = float(input(class_array[0] + ": "))
        score2 = float(input(class_array[1] + ": "))
        score3 = float(input(class_array[2] + ": "))

        average = float(score1 + score2 + score3) / 3
        newAverage = round(average,2)
        print("\nOverall average: " , newAverage)
        print("")
        print("*******************************************************")


    elif amountOfClasses == 2:
        score1 = float(input(class_array[0] + ": "))
        score2 = float(input(class_array[1] + ": "))

        average = float(score1 + score2) / 2
        newAverage = round(average,2)
        print("\nOverall average: " , newAverage)
        print("")
        print("*******************************************************")

    elif amountOfClasses == 1:
        score1 = float(input(class_array[0] + ": "))

        average = float(score1) / 1
        newAverage = round(average,2)
        print("\nOverall average: " , newAverage)
        print("")
        print("*******************************************************")

    else:
        print("\nError was found in the program")
        print("")
        print("*******************************************************")


def returnAverage():
    return newAverage
# Call the function to execute the process
#generate_Classes()