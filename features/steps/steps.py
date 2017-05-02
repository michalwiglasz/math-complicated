from behave import *


@given('we have math_complicated imported')
def step_impl(context):
    import math_complicated
    context.math_complicated = math_complicated


@when('we call add with "{x}" and "{y}"')
def step_impl(context, x, y):
    context.rv = context.math_complicated.add(1, 5)


@then('it will return "{rv}"')
def step_impl(context, rv):
    assert context.rv == rv



