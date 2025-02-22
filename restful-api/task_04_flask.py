from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory users dictionary
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Route for the root URL
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Route to get list of all usernames
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))

# Route to check the status
@app.route("/status")
def status():
    return "OK"

# Route to get a user's full details by username
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Route to add a new user via POST
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    # Check if the username is provided
    if not data.get("username"):
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    
    # Check if the user already exists
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Add the new user
    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", ""),
        "city": data.get("city", "")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
