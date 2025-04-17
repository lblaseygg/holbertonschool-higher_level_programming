from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT OR IGNORE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()

def read_json_data():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def read_csv_data():
    try:
        products = []
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append(row)
        return products
    except FileNotFoundError:
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
        
        products = [dict(row) for row in cursor.fetchall()]
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
        return render_template('task_03/product_display.html', error="Wrong source")
    
    if product_id and source != 'sql':
        products = [p for p in products if str(p['id']) == product_id]
        if not products:
            return render_template('task_03/product_display.html', error="Product not found")
    
    return render_template('task_03/product_display.html', products=products)

if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000) 