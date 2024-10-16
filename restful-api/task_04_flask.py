#!/usr/bin/python3
"""Flask put more words"""


from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """Flask put more words"""
    return 'Welcome to the Flask API!'


@app.route("/data")
def list_all_users():
    """Flask put more words"""
    return jsonify(list(users.keys()))


@app.route("/status")
def return_status():
    """Flask put more words"""
    return 'OK'


@app.route("/users/<username>")
def give_user_info(username):
    """Flask put more words"""
    if not users.get(username):
        return jsonify({"error": "User not found"}), 404
    return users[username]


@app.route("/add_user", methods=["POST"])
def create_user():
    """Flask put more words"""
    new_user = request.get_json()
    new_username = new_user.get('username')

    if not new_username:
        return jsonify({"error": "Username is required"}), 400
    else:
        users[new_username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run(debug=True)
