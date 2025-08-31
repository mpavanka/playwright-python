import pytest

def pytest_addoption(parser):
    parser.addoption("--user", action="store", default="default_user", help="Username for login")
    parser.addoption("--pass", action="store", default="default_pass", help="Password for login")


@pytest.fixture
def credentials(request):
    user = request.config.getoption("--user")
    password = request.config.getoption("--pass")
    return user, password