from behave import *

from Coordinate import Coordinate
from Shouty import Shouty

# use_step_matcher("re")

SHOUTY = Shouty()
ARBITRARY_MESSAGE = "Hello, world"


@given('Lucy is at {xCoord:d}, {yCoord:d}')
def step_impl(context, xCoord, yCoord):
    SHOUTY.set_location("Lucy", Coordinate(xCoord, yCoord))


@step('Sean is at {xCoord:d}, {yCoord:d}')
def step_impl(context, xCoord, yCoord):
    SHOUTY.set_location("Sean", Coordinate(xCoord, yCoord))


@when('Sean shouts')
def step_impl(context):
    SHOUTY.shout("Sean", ARBITRARY_MESSAGE)


@then('Lucy should hear Sean')
def step_impl(context):
    assert(1 == len(SHOUTY.get_shouts_heard_by("Lucy")))


@then('Lucy should hear nothing')
def step_impl(context):
    assert(0 == len(SHOUTY.get_shouts_heard_by("Lucy")))
