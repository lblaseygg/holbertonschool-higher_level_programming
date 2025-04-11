from flask import Flask, render_template, request
import json
import csv

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

@app.route('/products')
def products():
    source = request.args.get('source', 'json')
    product_id = request.args.get('id')
    
    if source == 'json':
        products = read_json_data()
    elif source == 'csv':
        products = read_csv_data()
    else:
        return render_template('product_display.html', error="Wrong source")
    
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