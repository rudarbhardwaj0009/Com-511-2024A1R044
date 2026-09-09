# write a python program to input marks of 5 students.
# for each student, the program should check whether the entered marks are valid or invalid. 
# Marks are considered vaild only if they are between 0 and 100. if the marks are invalid, the program
# should display "invalid marks skipped" and move to the next student without printing those marks.
# if the marks are valid, the program should display the marks as valid.




for i in range(5):
    marks = int(input("Enter marks: "))

    if marks >= 0 and marks <= 100:
        print("Valid marks")
    else:
        print("Invalid marks skipped")