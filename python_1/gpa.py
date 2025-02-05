def gpaCalc(newAverage):
    if 90 <= newAverage <101:
        print("Grade: A" )
        print("Grade Percantage:",newAverage,"%")
        print("Unweighted GPA: 4.0 ")
        print("*******************************************************")
    elif 87 <= newAverage < 90:
        print("Grade: A-" )
        print("Grade Percantage:",newAverage,"%")
        print("Unweighted GPA: 3.7 ")
        print("*******************************************************")
    elif 83 <= newAverage < 87:
        print("Grade: B+" )
        print("Grade Percantage:",newAverage,"%")
        print("Unweighted GPA: 3.3 ")
        print("*******************************************************")
    elif 80 <= newAverage < 83:
        print("Grade: B" )
        print("Grade Percantage:",newAverage,"%")
        print("Unweighted GPA: 3.0")  
        print("*******************************************************") 
    elif 77 <= newAverage < 80:
        print("Grade: B-" )
        print("Grade Percantage:",newAverage,"%")
        print("Unweighted GPA: 2.7")
        print("*******************************************************")
    elif 73 <= newAverage < 77:
        print("Grade: C+" )
        print("Grade Percantage:",newAverage,"%")
        print("Unweighted GPA: 2.3")
        print("*******************************************************")
    elif 70 <= newAverage < 73:
        print("Grade: C" )
        print("Grade Percantage:",newAverage,"%")
        print("Unweighted GPA: 2.0")
        print("*******************************************************")
    elif 67 <= newAverage < 70:
        print("Grade: C-")
        print("Grade Percantage:",newAverage,"%")
        print("Unweighted GPA: 1.7")
        print("*******************************************************")
    elif 63 <= newAverage < 67:
        print("Grade: D+")
        print("Grade Percantage:",newAverage,"%")
        print("Unweighted GPA: 1.3")
        print("*******************************************************")
    elif 60 <= newAverage < 63:
        print("Grade: D ")
        print("Grade Percantage:",newAverage,"%")
        print("Unweighted GPA: 1.0")
        print("*******************************************************")
    elif 50 <= newAverage < 60:
        print("Grade: D-")
        print("Grade Percantage:",newAverage,"%")
        print("Unweighted GPA: 0.7")
        print("*******************************************************")
    elif 0 <= newAverage < 50:
        print("Grade: F ")
        print("Grade Percantage:",newAverage,"%")
        print("Unweighted GPA: 0.0")
        print("*******************************************************")
    else:
        print("Your average is out of range, students can't a get grade that is greather than 100")
        print("**************************************************************************************")