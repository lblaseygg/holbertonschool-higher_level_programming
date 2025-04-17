#!/usr/bin/env python3
"""
Task 2: Creating a Dynamic Template with Loops and Conditions in Flask
"""

from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items():
    """Render the items page with dynamic content"""
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items = data.get('items', [])
    except FileNotFoundError:
        items = []
    return render_template('task_02/items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000) 