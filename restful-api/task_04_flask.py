from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Root route
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Data route - returns list of all usernames
@app.route("/data")
def data():
    return jsonify(list(users.keys()))

# Status route
@app.route("/status")
def status():
    return "OK"

# User details route
@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

# Add user route
@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.get_json()
    
    # Check if username is provided
    if "username" not in user_data:
        return jsonify({"error": "Username is required"}), 400
    
    username = user_data["username"]
    
    # Add user to the dictionary
    users[username] = user_data
    
    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201

if __name__ == "__main__":
    app.run(debug=True)