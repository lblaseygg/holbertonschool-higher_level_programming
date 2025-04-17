#!/usr/bin/env python3
"""
Task 3: Displaying Data from JSON or CSV Files in Flask
"""

import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json_data():
    """Read data from JSON file"""
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv_data():
    """Read data from CSV file"""
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except (FileNotFoundError, csv.Error):
        return []

@app.route('/products')
def products():
    """Render products page with data from specified source"""
    source = request.args.get('source', 'json')
    product_id = request.args.get('id')
    
    # Get data based on source
    if source == 'json':
        products = read_json_data()
    elif source == 'csv':
        products = read_csv_data()
    else:
        return render_template('product_display.html', error="Wrong source")
    
    # Filter by ID if provided
    if product_id:
        try:
            product_id = int(product_id)
            products = [p for p in products if int(p['id']) == product_id]
            if not products:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Invalid product ID")
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000) 