#!/usr/bin/env python3
"""
A simple API built using Flask to handle basic routes and JSON responses.

Endpoints:
- GET / : Returns a welcome message.
- GET /status : Returns "OK".
- GET /data : Returns a list of usernames stored in memory.
- GET /users/<username> : Returns the user data for a given username.
- POST /add_user : Adds a new user to the memory store.

The API serves data about users stored in memory in a dictionary format.
"""

from flask import Flask, jsonify, request

# Create a Flask application instance
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
    GET /
    Returns:
        A string message welcoming users to the Flask API.
    """
    return "Welcome to the Flask API!"

@app.route("/status", methods=["GET"])
def status():
    """
    Route to check the status of the API.
    GET /status
    Returns:
        A string message "OK" indicating the API is up and running.
    """
    return "OK"

@app.route("/data", methods=["GET"])
def get_usernames():
    """
    Route to retrieve a list of all usernames stored in the API.
    GET /data
    Returns:
        A JSON response containing a list of all usernames.
    """
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    Route to retrieve user data for a specific username.
    GET /users/<username>
    Args:
        username (str): The username to look for in the users dictionary.
    Returns:
        A JSON response with the user's data if found, or an error message if not.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Route to add a new user to the API.
    POST /add_user
    Expected JSON data format:
    {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    }
    Returns:
        A confirmation message with the added user's data, or an error if the username is missing.
    """
    data = request.get_json()

    # Check if the required 'username' field is present
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    # Check if the user already exists
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

# Run the Flask development server if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
