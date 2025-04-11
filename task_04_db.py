from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_data():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv_data():
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except (FileNotFoundError, csv.Error):
        return []

def read_sql_data(product_id=None):
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if product_id:
            cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT * FROM Products')
        
        rows = cursor.fetchall()
        products = [dict(row) for row in rows]
        conn.close()
        return products
    except sqlite3.Error:
        return []

@app.route('/products')
def products():
    source = request.args.get('source', 'json')
    product_id = request.args.get('id')
    
    if source == 'json':
        products = read_json_data()
    elif source == 'csv':
        products = read_csv_data()
    elif source == 'sql':
        products = read_sql_data(product_id)
    else:
        return render_template('product_display.html', error="Wrong source")
    
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
    app.run(debug=True, port=5000) 