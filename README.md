Pytest works by discovering and collecting test functions and fixtures from Python modules, leveraging Python's introspection capabilities. It then executes these tests by invoking the appropriate functions and fixtures based on configurable rules, running assertions to verify expected behavior. Pytest provides detailed reporting of test outcomes and supports customization through plugins and configuration options. Overall, it simplifies the process of writing and running tests in Python projects, offering flexibility and scalability for test suites.

To install pytest : pip install pytest

-To ensure that pytest recognizes your Python files as test files, you should follow these naming conventions:
For test files containing test functions or classes, the filename should start with (test_ )or end with (_test.py)

-Inside these test files, test functions should also follow a specific naming convention. They should start with test_.
Examples of valid test function names:
def test_add():

-After organizing your test files and functions according to these conventions, you can run pytest by simply executing pytest in your terminal within the project directory.
