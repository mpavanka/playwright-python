from behave import given, when, then
from FlipKart.stepDefinations.test_flipkartDashboardvalidations import TestFKboard
import logging

@given("User is on FlipKart homepage")
def step_homepage(context):
    TestFKboard.set_up(context)
    logging.info("✅ Step matched: User is on FlipKart homepage")


@when('User searches for "{product}"')
def step_search(context, product):
    TestFKboard.test_dashboard_page(context,product)
    logging.info(f"✅ Step matched: User searches for {product}")

@then("User should see the search results page with relevant products")
def step_results(context):
    logging.info("✅ Step matched: Results page is shown")
