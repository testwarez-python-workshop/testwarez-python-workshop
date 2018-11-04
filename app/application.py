from flask import Flask, request, jsonify, Response
from app.users import USERS

app = Flask(__name__)

GET = "GET"
POST = "POST"


@app.route("/", methods=[GET, POST])
def index():
    return "Hello World"


@app.route("/user/<username>", methods=[GET])
def access_users(username):
    user_details = USERS.get(username)
    if user_details:
        return jsonify(user_details)
    else:
        return Response(status=404)


@app.route("/user/<username>", methods=[POST])
def add_user(username):
    USERS.update({username: request.get_json()})
    return "New user created"


@app.route("/users", methods=[GET])
def get_users():
    return jsonify(USERS)


if __name__ == "__main__":
    app.run()
