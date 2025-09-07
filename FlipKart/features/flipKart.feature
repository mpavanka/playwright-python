Feature: FlipKart Dashboard Validations

  Scenario: Search for a product
    Given User is on FlipKart homepage
    When User searches for "laptop"
    Then User should see the search results page with relevant products

#   Scenario: Validate product search results
#     Then User should see at least one product in the search results

#   Scenario: Filter products by Price Rangesss
#     When User sets the price range filter to "20000" to "50000"
#     Then User should see products within the specified price range

#   Scenario: Sort products by Price: Low to High
#     When User sorts the products by "Price: Low to High"
#     Then User should see products sorted in ascending order of price

#   Scenario: Validate product details
#     When User clicks on the first product in the search results
#     Then User should see the product details page with correct information

#   Scenario: Add product to Cart
#     When User adds the first product to the cart
#     Then The product should be added to the cart successfully

#   Scenario: Remove product from Cart
#     When User removes the product from the cart
#     Then The cart should be empty

#   Scenario: Validate pagination
#     When User navigates to the second page of search results
#     Then User should see different products than on the first page

#   Scenario: Search for a non-existing product
#     When User searches for "xyzabc123"
#     Then User should see a message indicating no products were found

#   Scenario: Filter products by Customer Ratings
#     When User applies a filter for "4★ & above" customer ratings
#     Then User should see products with customer ratings of 4 stars and above
# senario: Filter products by Brand
#     When User clicks on Brand filter and selects "HP" and "DELL"
#     Then User should see products filtered by selected brands