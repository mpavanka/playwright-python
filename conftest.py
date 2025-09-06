import pytest

def pytest_addoption(parser):
    parser.addoption("--user", action="store", default="default_user", help="Username for login")
    parser.addoption("--pass", action="store", default="default_pass", help="Password for login")
    parser.addoption("--my-browser", action="store", default="chromium",
                 help="Browser to use: chromium, firefox, webkit")


@pytest.fixture(scope="session")
def credentials(request):
    user = request.config.getoption("--user")
    password = request.config.getoption("--pass")
    browser = request.config.getoption("--my-browser")
    print(f"Running tests on {browser} with user {user}")
    return user, password, browser

@pytest.fixture(scope="session")
def openBrowser(playwright, credentials):
    userName, passWord, browser_name = credentials
    # if browser_name not in ["chromium", "firefox", "webkit"]:
    #     raise ValueError(f"Unsupported browser: {browser_name}. Choose from 'chromium', 'firefox', 'webkit'.")
    browser = getattr(playwright, browser_name).launch(headless=False, slow_mo=50)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://flipkart.com")
    yield page
    context.close()
    browser.close()
