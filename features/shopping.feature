Feature: Adding a product to the cart

Scenario: Adding a product to an empty cart
    Given I am on the product list page
    When I add a product to the cart
    Then the cart should contain 1 item

Scenario: Adding a product to a non-empty cart
    Given I am on the product list page
    And I have already added a product to the cart
    When I add another product to the cart
    Then the cart should contain 2 items
