import pytest
import shapes

@pytest.mark.parametrize("side_length , expected_area" , [(5,25) , (4,16) , (9,81)])
def test_multiple_square_areas(side_length,expected_area):
    assert shapes.square(side_length).area() == expected_area
 
#results will be 3 passes since we had three numbers given to it as a tupple and then checking the assertion on them.   
    
    
    
    
    
    
#Parameterized testing in Pytest allows testing with different values without messy loops.
#Useful for testing the same scenario with different inputs.