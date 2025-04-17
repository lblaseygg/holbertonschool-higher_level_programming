#!/usr/bin/env python3
"""
Task 2: Creating a Dynamic Template with Loops and Conditions in Flask
"""

import json
from flask import Flask, render_template

app = Flask(__name__)

def load_items():
    """Load items from the JSON file"""
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            return data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []

@app.route('/items')
def items():
    """Render the items page with dynamic content"""
    items_list = load_items()
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000) 