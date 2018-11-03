import pytest
from hamcrest import *
from rest_api_test.src.user_requests import UserManager

user_manager = UserManager()


class TestUserDatabase:

    def test_server_responding(self):
        res = user_manager.get_status()
        assert_that(res.status_code, equal_to(200))
        assert_that(res.text, equal_to("Hello World"))

    def test_existing_user(self):
        res = user_manager.get_all_users()
        assert_that(res.json(), has_item("dejv"))

    def test_adding_user(self):
        res = user_manager.add_user("janosik", {"name": "Jerzy Janosik"})
        assert_that(res.text, equal_to("New user created"))

    def test_added_user_exist(self):
        res = user_manager.get_user("janosik")
        assert_that(res.json(), has_item("name"))


if __name__ == '__main__':
    pytest.main()
