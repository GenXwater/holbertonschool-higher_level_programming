#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv


app = Flask(__name__)

def read_json_file(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def read_csv_file(filepath):
    products = []
    with open(filepath, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            try:
                row['id'] = int(row.get('id', 0))
                row['price'] = float(row.get('price', 0.0))
            except ValueError:
                row['id'] = 0
                row['price'] = 0.0

            row['name'] = row.get('name', 'N/A')
            row['category'] = row.get('category', 'N/A')
            products.append(row)
    return products

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def items():
    with open('items.json') as json_file:
        data = json.load(json_file)
        items_list = data.get("items", [])

    return render_template('items.html', items=items_list)

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == "json":
        products = read_json_file('products.json')
    elif source == "csv":
        products = read_csv_file('products.csv')
    else:
        return render_template('product_display.html', error="Wrong source. Please specify 'json' or 'csv'.")

    if product_id:
        products = [product for product in products if product.get("id") == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found.")

    return render_template('product_display.html', products=products)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)