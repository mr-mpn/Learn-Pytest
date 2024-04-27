import math

class shape:  #This is the upper class which then the circle will inherit from it
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
    
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius **2
    
    def perimeter(self):
        return 2 * math.pi*self.radius