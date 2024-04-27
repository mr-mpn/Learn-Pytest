import pytest
import source

def test_add():
    result  = source.add(5,3)
    assert result == 8
    
def test_divide():
    result = source.divide(10,2)
    assert result == 5
    
def test_divide_by_zero():
    with pytest.raises(ValueError):
     source.divide(10,0)
     

def test_add_strings():
    with pytest.raises(AssertionError):
     result = source.add("I Like" , "Burgers")
     assert result == "I like Burgers"
   