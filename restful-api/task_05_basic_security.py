from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for JWT token encoding and decoding
app.config['JWT_SECRET_KEY'] = 'your_secret_key'

# Initialize the JWTManager and HTTPBasicAuth
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# In-memory user data with hashed passwords and roles
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Basic Authentication Verification
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# JWT Authentication Setup
@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the request
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if the username exists and password is correct
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Create a JWT token
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# Role-based Authentication Route
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    user = users.get(current_user)
    
    # Check if the user has an admin role
    if user and user['role'] == 'admin':
        return "Admin Access: Granted"
    
    return jsonify({"error": "Admin access required"}), 403

# Custom Error Handlers for JWT Errors
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run(debug=True)
