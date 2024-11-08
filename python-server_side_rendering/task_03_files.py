import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    # Charger les données depuis le fichier JSON
    with open('items.json', 'r') as file:
        data = json.load(file)
    # Passer la liste d'items au template
    items_list = data.get("items", [])
    return render_template('items.html', items=items_list)

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []

def read_csv(file_path):
    products = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                products.append(row)
        return products
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    # Lire les données en fonction de la source
    if source == "json":
        products = read_json("products.json")
    elif source == "csv":
        products = read_csv("products.csv")
    else:
        return render_template("product_display.html", error="Wrong source")

    # Filtrer les produits par ID si un ID est fourni
    if product_id:
        products = [product for product in products if product.get("id") == product_id]
        if not products:
            return render_template("product_display.html", error="Product not found")
    
    return render_template("product_display.html", products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
