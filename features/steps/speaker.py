from behave import *

use_step_matcher("re")


@given("I navigate to register page")
def step_impl(context):
    """
    Navigate to register page and as the web server will run in local when
    we run
    end to end tests using behave, the url will be
    http://127.0.0.1:5000/register
    """
    context.browser.get('http://127.0.0.1:5000/register')


@step("I enter valid information about me")
def step_impl(context):
    """
    Find the html element using the name attribute and input the required data
    Here entering some valid values.
    """
    context.browser.find_element_by_name('name').send_keys('validusername')
    context.browser.find_element_by_name('last_name').send_keys(
        'validlastname')
    context.browser.find_element_by_name('email').send_keys('validemail')
    context.browser.find_element_by_name('country').send_keys('validcountry')


@when("I click on Submit button")
def step_impl(context):
    """
     Find the input button on the html page and invoke .click()
    """
    context.browser.find_element_by_xpath(
        f"//input[@type='submit' and @value='Submit']").click()


@then("register is successful")
def step_impl(context):
    """
    If the register is successful it will be shown a Congrats message.
    """
    assert 'Congrats! You are registered as a Speaker' in \
           context.browser.page_source
