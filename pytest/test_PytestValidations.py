import pytest 

@pytest.fixture(scope="function")
def test_addition():
    print("function scope")
    print(2 + 4)
    print("ended scope in function")
    return "pass"

def test_value(commonSetUp):
    print("in pytest...")
    print("-----------------------------------")

def test_value2(commonSetUp, functioncommonSetUp):
    assert commonSetUp == "pass"
    print("in second function")
