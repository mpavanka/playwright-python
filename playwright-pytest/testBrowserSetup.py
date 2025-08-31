import pytest
from playwright.sync_api import Page


# def test_openBrowser(playwright):
#     browser = playwright.chromium.launch(headless=False, slow_mo=50, channel="msedge")
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.example.com")
#     page.wait_for_timeout(50000) # Wait for 50 seconds to observe the browser
#     browser.close()

def test_playwrightShortCut(page:Page, credentials):
    userName, passWord = credentials

    print(f"Username: {userName}, Password: {passWord}")
    page.goto("https://facebook.com")
    page.locator("[name='email']").fill(userName)
    page.locator("[name='pass']").fill(passWord)