# write a python program to determine whether a student is eligible for scholarship.
# The scholarship should be granted if the student satisfies either of the following conditions:
# a) The students has CGPA of 8.5 or above attendance of 85 percent or above.
# b) The student has won a natioanl-level competition

# The program should take CGPA, attendance percentage, and national-level competition status as input,
# then display whether the student is eligble for the scholarship.


cgpa = float(input("CGPA: "))
att = float(input("Attendance: "))
comp = input("Competition (yes/no): ")

if cgpa >= 8.5 or att >= 85 or comp == "yes":
    print("Eligible")
else:
    print("Not Eligible")
    
    

