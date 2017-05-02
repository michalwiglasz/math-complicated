from behave import *


@given('we have math_complicated imported')
def step_impl(context):
    import math_complicated
    context.math_complicated = math_complicated


@when('we call add with "{x}" and "{y}"')
def step_impl(context, x, y):
    x = int(x)
    y = int(y)
    context.rv = context.math_complicated.add(x, y)


@then('it will return "{rv}"')
def step_impl(context, rv):
    rv = int(rv)
    assert context.rv == rv



