from behave import *

use_step_matcher("re")


@given("we have behave installed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("we implement a test")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert True is not False


@then("behave will test it for us!")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.failed is False
