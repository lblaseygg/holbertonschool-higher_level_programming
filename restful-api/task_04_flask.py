from flask import Flask, request, jsonify

app = Flask(__name__)

# Store users in-memory
users = {}

@app.route('/')
def home():
    return "Welcome to the API!"

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(list(users.values()))

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data['username']
    if username in users:
        return jsonify({"error": "Username already exists"}), 400
    
    users[username] = {"username": username}
    return jsonify({"message": "User added successfully"}), 201

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "API is running"})

if __name__ == '__main__':
    app.run(debug=True)

