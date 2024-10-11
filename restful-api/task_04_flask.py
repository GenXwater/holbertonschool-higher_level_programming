#!/usr/bin/python3
"""
Simple API using Flask for handling basic routes and JSON responses.

Routes:
- GET / : Returns a welcome message.
- GET /status : Returns "OK".
- GET /data : Returns a list of all usernames.
- GET /users/<username> : Returns user data for a specific username.
- POST /add_user : Adds a new user to the in-memory store.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory dictionary to store user data
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route("/", methods=["GET"])
def home():
    """
    Route to return a welcome message for the API.
    Returns:
        str: A welcome message.
    """
    return "Welcome to the Flask API!"

@app.route("/status", methods=["GET"])
def status():
    """
    Route to return the status of the API.
    Returns:
        str: "OK".
    """
    return "OK"

@app.route("/data", methods=["GET"])
def get_usernames():
    """
    Route to return a list of all usernames in the users dictionary.
    Returns:
        Response: JSON list of usernames.
    """
    return jsonify(list(users.keys()))

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    Route to return data for a specific user.
    
    Args:
        username (str): The username to retrieve.

    Returns:
        Response: JSON object with user data or an error if not found.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Route to add a new user to the users dictionary.

    Expects a JSON payload with the following structure:
    {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    }

    Returns:
        Response: JSON object with the added user's data or an error message.
    """
    data = request.get_json()

    # Check if 'username' is provided in the data
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    # Check if user already exists
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Add the new user to the dictionary
    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", ""),
        "city": data.get("city", "")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
