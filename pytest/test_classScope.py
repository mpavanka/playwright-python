import pytest

class TestscopeFixture:

    def test_classScope1(self, classcommonSetUp):
        print("in class scope 1")

    def test_classScope2(self, classcommonSetUp):
        print("in class scope 2")
    
    def test_classScope3(self, classcommonSetUp):
        print("in class scope 3")

def test_outsideclassScope(classcommonSetUp):
    print("in outside class scope function")

def test_outsideclassScope2(classcommonSetUp):
    print("in outside class scope function 2")

@pytest.mark.smoke
def test_outsideclassScope3(functioncommonSetUp):
    print("in outside class scope function 3")
