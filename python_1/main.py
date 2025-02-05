def main():

    #User Basic Information
    print("")
    print("*******************************************************")
    print("")
    print("Let's create your student porfolio!")
    print("")
    userName = input("Enter your full name: ")
    userSchool = input("Enter the school you go to: ")
    userGrade = input("Enter your grade level: ")
    print("")
    print("*******************************************************")
    print("")

    #Welcome Message
    print(userName,",","Welcome to the GPA calculator[V1]! ")
    print("")
    print("*******************************************************")
    print("")

    #Goes from input classes => input class scores => calculate average => moves average to main.py 
    from classes import generate_Classes
    from classes import returnAverage
    generate_Classes() 

    print("Loading...")
    print("*******************************************************")
    
    # Grabs average and conditions it to its respective GPA
    from gpa import gpaCalc
    newAverage = returnAverage()
    gpaCalc(newAverage)

    #Ask user if they want to use the calculator again 
    userResponse = input( "\nTry again? [Y or N] ")
    print("")

    if userResponse.lower() == "y":
        userResponse = True
    elif userResponse.lower() == "n":
        print("See you later", userName, "!")
        return

    while userResponse:
        generate_Classes()
        newAverage = returnAverage()
        gpaCalc(newAverage)
        userResponse = input("\nTry again? [Y or N] ")

main()


