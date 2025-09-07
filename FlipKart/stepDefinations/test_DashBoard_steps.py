from behave import Given, When, Then
from behave import *
from playwright.sync_api import sync_playwright
    
@Given("User is on FlipKart login page")
def user_is_on_FlipKart_login_page(self):
    print("User is on FlipKart login page")

@When("User searches for {string}")
def user_searches_for(self, product):
    pass

@Then("User should see the search results page with relevant products")
def user_should_see_the_search_results_page_with_relevant_products(self):
    pass
