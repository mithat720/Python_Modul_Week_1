#Get Midterm and Final grades from a student for any course. The sum of 40% of the midterm exam grade and 60% of the final grade will give the year-end average. 
#If the average is below 50, "FAILED" will appear on the screen, and if it is 50 or above, "SUCCESSFUL" will be displayed on the screen. This printing process is 4 lessons. and the lessons will be written one after the other.
for course in range(1,5):   # Repeat the process for 4 courses
    print("Course", course)

    midterm = float(input("Enter the midterm grade: "))
    final = float(input("Enter the final grade: "))

    average = (midterm * 0.4) + (final * 0.6) #Calculate the average

    if average >= 50:
        print("Result: Succesful")
    else:
        print("Result: Failed")
    