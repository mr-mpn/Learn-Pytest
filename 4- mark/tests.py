import pytest
import source
import time
#we can manage which tests to be executed with marks

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
   
@pytest.mark.slow
def test_very_slow():
    time.sleep(2)
    result = source.divide(10,2)
    assert result == 5
    
#if we just write pytest tests.py it will run all the tests, but if we write pytest -m slow : it will run the test file that has the mark slow
#so it will be 1 passed, 4 deselected 

@pytest.mark.skip(reason="This feature is currently broken!")
def test_add_broken():
    assert source.add(1, 2) == 3

#Result : 5 passed
#s ...  means skip

@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_zero_broken():
    with pytest.raises(ZeroDivisionError):
       assert source.divide(10, 0)

#Now we have s ... x which s is the skip and x is the fail that we knew before
#it will not fail in the test since we marked it as fail

