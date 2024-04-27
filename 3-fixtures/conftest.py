import shapes
import pytest

#we can define our fixtures in another code with the name of conftest so that they are not written in the test file


@pytest.fixture    #Can be used to define the rectangle only once and then pass it to the functions as an object
def my_rectangle():
    return shapes.rectangle(length = 10 , width = 20)

#This object is now global and can be used in other .py files