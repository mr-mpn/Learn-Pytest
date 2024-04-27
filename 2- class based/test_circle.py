import pytest
import shapes
import math

#Class Based tests come with two functions : 1-setup 2-teardown
#Setup method runs everytime a test is being executed
#Teardown method runs everytime a test done with execution
#Pytest -s to be able to see the setting up and tearing down in the terminal
class TestCircle:
    
    def setup_method(self,method):
        print("Setting up ..." , method)  
        self.circle = shapes.circle(10)
        
    def teardown_method(self,method):
        print("Tearing down ..." , method)
    
    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius **2

    def test_perimeter(self):
        result  = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert  result == expected