import requests
from rest_api_test.config.server import SERVER


class UserManager:

    def __init__(self):
        self.server_data = SERVER
        self.base_url = self.server_data["base_url"]

    def get_status(self):
        return requests.get(self.base_url)

    def add_user(self, user_name, user_data):
        return requests.post(self.base_url + "/user/{}".format(user_name), json=user_data)

    def get_user(self, user_name):
        return requests.get(self.base_url + "/user/{}".format(user_name))

    def get_all_users(self):
        return requests.get(self.base_url + "/users")

    def clean_db(self):
        return requests.get(self.base_url + "/clean_db")

    def restore_db(self):
        return requests.get(self.base_url + "/restore_db")
