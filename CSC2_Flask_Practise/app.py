import json

from flask import Flask, render_template, request, session, flash,  redirect, url_for

app = Flask(__name__)

app.secret_key = 'your_secret_key'

# Add selected flower to the shopping cart
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    flower = request.form['flower'] #get selcted flower name
    quantity = int(request.form['quantity']) #convert quantity to a number
    flowers, addons = load_data() #get flower data from file, ignore addons data for now
    cart = session.get('cart', {}) #get cart from session or start fresh

    if flower not in flowers:
        flash('Invalid flower selected.')
        return redirect(url_for('index1.html'))
    
    if flower in cart:
        cart[flower] += quantity # add existing quantity
    else:
            cart[flower] = {
                 'price': flowers[flower]['price'],
                 'quantity': quantity
            }

    session['cart'] = cart # update session
    session.modified = True # force flask to save it
    flash(f'{quantity} {flower}(s) added to cart.')
    return redirect(url_for('index.html')) # go back to home page

    return render_template('index1.html')

def load_data():
    with open('data/flowers.json') as file:
        flowers = json.load(file)

        with open('data/addons.json') as file:
            addons = json.load(file)

    return flowers, addons



@app.route('/')
def index():
    flowers, addons = load_data()
    return render_template('index.html', flowers=flowers, addons=addons)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/checkout')
def checkout():
    return render_template('invoice.html')

@app.route('/orders')
def order_history():
    return render_template('order_history.html')

if __name__ == '__main__':
    app.run(debug=True)