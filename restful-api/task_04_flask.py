from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory data structure to store users
users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_usernames():
    return jsonify({"users": list(users.keys())})  # Ensure it returns an object

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username'].strip()

    if not username:
        return jsonify({"error": "Invalid username"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    # Add new user to the dictionary
    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", ""),
        "city": data.get("city", "")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run(debug=True)
