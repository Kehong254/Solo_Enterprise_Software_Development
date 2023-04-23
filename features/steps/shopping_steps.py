from behave import given, when, then
from selenium import webdriver

@given('I am on the product list page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://localhost:8000/products/')

@when('I add a product to the cart')
def step_impl(context):
    add_to_cart_button = context.browser.find_element_by_css_selector('form button')
    add_to_cart_button.click()

@then('the cart should contain 1 item')
def step_impl(context):
    cart_items = context.browser.find_elements_by_css_selector('.cart-item')
    assert len(cart_items) == 1

@when('I add another product to the cart')
def step_impl(context):
    add_to_cart_button = context.browser.find_element_by_css_selector('form button')
    add_to_cart_button.click()

@then('the cart should contain 2 items')
def step_impl(context):
    cart_items = context.browser.find_elements_by_css_selector('.cart-item')
    assert len(cart_items) == 2

def after_scenario(context, scenario):
    context.browser.quit()
