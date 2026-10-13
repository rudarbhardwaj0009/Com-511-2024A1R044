''' 1. Create a class and object: student details
problem: create a student class to store a student's name and roll number.
create an object and display the details using an instance method.
'''

class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        print("Student Name: ",self.name)
        print("Student Roll No: ",self.rollno)
        
s1=student("Rudar",44)
s2=student("Ram",101)

s1.display()
s2.display()