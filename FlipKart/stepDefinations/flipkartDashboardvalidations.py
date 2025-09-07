import pytest
from playwright.sync_api import Page, Playwright, sync_playwright

@pytest.mark.usefixtures("test_setup")
class TestFKboard:

    def set_up(self):
        
        print("This is FlipKart Dashboard validations class")
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context()
        self.page = context.new_page()
        self.page.goto("https://flipkart.com")

    
    def test_dashboard_page(self, product):
        product = product
        self.page.get_by_placeholder("Search for Products, Brands and More").click()
        self.page.locator("input[name='q']").fill(product)
        self.page.keyboard.press("Enter")
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(5000)
    
    def test_select_Filter(self):
        filters = [
            ("Brand", "HP"),
            ("Processor", "Core i7"),
            ("Customer Ratings", "4★ & above"),
        ]
        for category, option in filters:
            attributeValue  = self.page.locator("//div[normalize-space(text())='" + category +"']/following-sibling::*").get_attribute("class")
            if "rZzKt4" not in attributeValue:
                self.page.locator("//div[normalize-space(text())='" + category +"']/following-sibling::*").click()
            # self.page.locator("//section/div/div[text()='" + (category) + "']").click()
            self.page.locator("//div/label/div[text()='"+ (option) +"']").click()
            self.page.wait_for_load_state("networkidle")
            self.page.wait_for_timeout(5000)
        self.page.select_option("//div[@class='tKgS7w']/select", "50000")

    def test_validate_and_clear_filters(self):
        selectedFilters = self.page.locator("//section[@class='pgRLLn _2OLUF3']/div[2]/div[1]/div")
        assert selectedFilters.count() == 3
        counter=0
        for category, option in self.filters:
            value = selectedFilters.nth(2).text_content()
            print(f"Value: {value}, Option: {option}")
            print("-------------------------------------------")
            assert (selectedFilters.nth(2).text_content()), option
            counter+=1
        self.page.locator("//*[@id='container']/div/div[3]/div/div[1]/div/div[1]/div/section[1]/div[1]/div[2]/span").click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(5000)
        assert selectedFilters.count() == 0
    
