import pytest
from playwright.sync_api import Page
import json
import os

file_path = os.path.join(os.path.dirname(__file__), "..", "DATA", "creds.json")
with open(file_path, "r") as f:
    data = json.load(f)
    creds = data["userCreds"]


@pytest.fixture(params=creds)
def credentials(request):
    return request.param["username"], request.param["password"]

def test_playwrightShortCut(openBrowser, credentials):
    page = openBrowser
    userName, passWord = credentials
    print(f"Username: {userName}, Password: {passWord}")
    page.goto("https://facebook.com")
    page.locator("[name='email']").fill(userName)
    page.locator("[name='pass']").fill(passWord)
    page.locator("[name='login']").click()