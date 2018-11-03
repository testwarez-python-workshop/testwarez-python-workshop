from flask import Flask, request, jsonify, Response
from app.users import USERS

app = Flask(__name__)

GET = "GET"
POST = "POST"


@app.route("/")
def index():
    return "Hello World"


@app.route("/user/<username>", methods=[GET])
def access_users(username):
    if request.method == GET:
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details)
        else:
            return Response(status=404)


@app.route("/user/<username>", methods=[POST])
def add_user(username):
    if request.method == POST:
        USERS.update({username: request.get_json()})
        return "New user created"


@app.route("/users", methods=[GET])
def get_users():
    if request.method == GET:
        return jsonify(USERS)


if __name__ == "__main__":
    app.run()
