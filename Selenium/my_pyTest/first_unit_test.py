'''
pytest/ py.test - it will pick up all the modules in a project either starting with test_ or ending with _test
- it will methods starting with 'test'

pytest -h/ --help- it will give you list of all command elements

pytest -rA- it gives detailed report

pytest -rA -k abc - it will pick up all the test methods contains abc keyowrd

pytest -rA -k "not abc" - it will pick up all the test methods not containing abc keyowrd

pytest -rA test_second.py::test5 - this will pick only test 5 in test_second.py module


'''
import pytest

@pytest.yield_fixture
def setup():
    print("this is setup method")
    yield 
    print("this is tear down step")
    
    
def test1(setup):
    print("This is test1")
    a= 2
    b= 3
    assert a+1 == b, "a is not equal to b"
    
def test2(setup):
    print("This is test2")
    
def test3():
    print("This is test3")