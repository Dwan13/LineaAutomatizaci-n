from behave import given, when, then, step

import sys
sys.path.insert(0, "PruebaFib")

import fibonacci



@given('Yo tengo una serie de fibonacci')
def step_impl(context):
    pass

@when('Agregando "{x:g}"')
def step_impl(context, x):
    assert isinstance(x, float)
    context.result = fib([x])

@then('La serie de fibonacci retorna "{fibo:g}"')
def step_impl(context, fibo):
    assert isinstance(fibo, float)
    assert context.result == fibo
