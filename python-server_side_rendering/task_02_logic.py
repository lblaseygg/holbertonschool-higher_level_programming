#!/usr/bin/env python3
"""
Task 2: Creating a Dynamic Template with Loops and Conditions in Flask
"""

from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/items')
def items():
    # Get the path to items.json
    json_path = os.path.join(os.path.dirname(__file__), 'items.json')
    
    try:
        # Read and parse the JSON file
        with open(json_path, 'r') as file:
            data = json.load(file)
            items = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or is invalid, use empty list
        items = []
    
    # Pass the items to the template
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True) 