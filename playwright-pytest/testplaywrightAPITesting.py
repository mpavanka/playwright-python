from playwright.sync_api import Playwright
from deepdiff import DeepDiff
import pytest
import json

class TestAPIUtility:
    def get_expected_file(self):
        with open("expectedData/expecteddata.json", 'r') as file:
            data = json.load(file)
        return data

    def test_get_token(self, playwright: Playwright):
        expected_data = self.get_expected_file()
        api_req = playwright.request.new_context()
        response = api_req.post(
            "https://reqres.in/api/login",
            headers={"Content-Type": "application/json"},
            data={
                "email": "eve.holt@reqres.in",
                "password": "cityslicka"
            }
        )
        token = response.json()
        print(token.get("error"))
        print("--------------------")
        diff = DeepDiff(expected_data, token)
        print(diff)
        api_req.dispose()

    def test_get_api_details(self, playwright: Playwright):
        api_req_context = playwright.request.new_context()
        response = api_req_context.get("https://reqres.in/api/users/2")
        data = response.json()
        print(response.status)
        print(response.ok)
        print(data.get("data", {}).get("email"))
        print(json.dumps(data, indent=4))
        api_req_context.dispose()
