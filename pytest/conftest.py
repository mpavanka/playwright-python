import pytest


@pytest.fixture(scope="session")
def commonSetUp():
    print("am in common session or fixture")
    return "pass"

@pytest.fixture(scope="module")
def commonSetUpmodule():
    print("am in common module or fixture")

@pytest.fixture(scope="function")
def functioncommonSetUp():
    print("am in common function or fixture from confest.py class")
    yield
    print("Tear down process for functions from conftest file ")

@pytest.fixture(scope="class")
def classcommonSetUp():
    print("am in common class or fixture")
    yield
    print("Tear down process for class from conftest file ")