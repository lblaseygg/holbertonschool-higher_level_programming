#!/usr/bin/env python3
"""
Task 3: Displaying Data from JSON or CSV Files in Flask
"""

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_data():
    """Read data from JSON file"""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def read_csv_data():
    """Read data from CSV file"""
    try:
        products = []
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append(row)
        return products
    except FileNotFoundError:
        return []

@app.route('/products')
def products():
    """Render products page with data from specified source"""
    source = request.args.get('source', 'json')
    product_id = request.args.get('id')
    
    if source == 'json':
        products = read_json_data()
    elif source == 'csv':
        products = read_csv_data()
    else:
        return render_template('task_03/product_display.html', error="Wrong source")
    
    if product_id:
        products = [p for p in products if str(p['id']) == product_id]
        if not products:
            return render_template('task_03/product_display.html', error="Product not found")
    
    return render_template('task_03/product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000) 