#!/usr/bin/python3
"""Flask"""

from flask import Flask, jsonify, request


app = Flask(__name__)
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route("/")
def home():
    return 'Welcome to the Flask API!'


@app.route("/data")
def list_all_users():
    return jsonify(list(users.keys()))


@app.route("/status")
def return_status():
    return 'ok'


@app.route("/users/<username>")
def give_user_info(username):
    if not users.get(username):
        return jsonify({"error": "User not found"}), 404
    return users[username]


@app.route("/add_user", methods=["POST"])
def create_user():
    new_user = request.get_json()
    new_username = new_user.get('username')

    if not new_username:
        return jsonify({"error": "Username is required"}), 400
    else:
        users[new_username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run(debug=True)
