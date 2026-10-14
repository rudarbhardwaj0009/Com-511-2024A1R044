'''
2. Instance methods: Rectangle area and perimeter
Problem: create a rectangle class with length and breadth.
use instance methods to calculate its area and perimeter 
'''


class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length*self.breadth)
    
rect1=rectangle(10,5)

print("Rectangle Area : ",rect1.area())
print("Rectangle Perimeter : ",rect1.perimeter())