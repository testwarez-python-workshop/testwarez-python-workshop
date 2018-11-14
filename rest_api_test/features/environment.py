from rest_api_test.src.user_requests import UserManager

user_manager = UserManager()


def before_all(context):
    user_manager.get_status()
    user_manager.restore_db()


def before_scenario(context, scenario):
    if "empty_db" in context.tags:
        if scenario.keyword != "Scenario Outline" or (scenario.keyword == "Scenario Outline" and ".1" in scenario.name):
            user_manager.clean_db()
            context.user_data = []
