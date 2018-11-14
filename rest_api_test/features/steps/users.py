from behave import *
from hamcrest import *
from rest_api_test.src.user_requests import UserManager

user_manager = UserManager()


@given("server is responding")
def step_impl(context):
    res = user_manager.get_status()
    assert_that(res.status_code, equal_to(200))
    assert_that(res.text, equal_to("Hello World"))


@when('I get "{user_name}" data')
def step_impl(context, user_name):
    res = user_manager.get_user(user_name)
    assert_that(res.status_code, equal_to(200))
    context.user_data = res.json()


@then('I can get all data')
def step_impl(context):
    res = user_manager.get_all_users()
    assert_that(res.status_code, equal_to(200))


@when('I get all data')
def step_impl(context):
    res = user_manager.get_all_users()
    context.user_data = res.json()


@then("I can see following parameters")
def step_impl(context):
    for row in context.table:
        assert_that(context.user_data, has_item(row['user']))
        assert_that(context.user_data[row['user']], has_value(row['name']))


@then('I can see name "{name}"')
def step_impl(context, name):
    assert_that(context.user_data, has_value(name))


@when('I create "{name}" user with following data')
def step_impl(context, name):
    user_data = {}
    for row in context.table:
        user_data[row["key"]] = row["value"]
    user_manager.add_user(name, user_data)


@then('number of users is "{num_val}"')
def step_impl(context, num_val):
    assert_that(context.user_data, has_length(int(num_val)))
