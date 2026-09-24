import json

from flask import Flask, render_template, request, session, flash,  redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    pizza = load_data()
    return render_template('index.html', pizza=pizza)

def load_data():
        with open('data/pizza.json') as file:
            data = json.load(file)
        return data

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/checkout')
def checkout():
    return render_template('invoice.html')

@app.route ('/order')
def order_history():
    return render_template('order_history.html')

if __name__ == '__main__':
    app.run(debug=True)

