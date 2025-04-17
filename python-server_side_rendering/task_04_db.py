#!/usr/bin/env python3
"""
Task 4: Extending Dynamic Data Display to Include SQLite in Flask
"""

import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def create_database():
    """Create and populate the SQLite database"""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Insert sample data
    cursor.execute('''
        INSERT OR IGNORE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99),
        (3, 'Desk Chair', 'Furniture', 199.99)
    ''')
    
    conn.commit()
    conn.close()

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

def read_sql_data(product_id=None):
    """Read data from SQLite database"""
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if product_id:
            cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT * FROM Products')
        
        products = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return products
    except sqlite3.Error:
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
    elif source == 'sql':
        products = read_sql_data(product_id)
    else:
        return render_template('product_display.html', error="Wrong source")
    
    # Filter by ID if provided (for JSON and CSV sources)
    if product_id and source != 'sql':
        try:
            product_id = int(product_id)
            products = [p for p in products if int(p['id']) == product_id]
            if not products:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Invalid product ID")
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000) 