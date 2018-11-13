from rest_api_test.src.user_requests import UserManager

user_manager = UserManager()


def before_all(context):
    user_manager.get_status()
    user_manager.restore_db()


def before_tag(context, tag):
    if tag == 'empty_db':
        user_manager.clean_db()
        context.user_data = []
