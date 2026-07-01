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
        return redirect(url_for('index2.html'))
    
    if flower in cart:
        cart[flower]['quantity'] += quantity # add existing quantity
    else:
            cart[flower] = {
                 'price': flowers[flower]['price'],
                 'quantity': quantity
            }

    session['cart'] = cart # update session
    session.modified = True # force flask to save it
    flash(f'{quantity} {flower}(s) added to cart.')
    return redirect(url_for('index2', flowers=flowers, addons=addons)) # go back to home page

    return render_template('index2.html' , flowers=flowers, addons=addons, cart=cart)

def load_data():
    with open('data/flowers.json') as file:
        flowers = json.load(file)

        with open('data/addons.json') as file:
            addons = json.load(file)

    return flowers, addons

@app.route('/')
def index():
    flowers, addons = load_data()
    cart = session.get('cart', {})
    total = calculate_total(cart)
    return render_template('index.html', flowers=flowers, addons=addons, cart=cart, total=total)


def calculate_total(cart):
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return total

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/invoice')
def invoice():
    return render_template('invoice.html')

@app.route('/orders')
def order_history():
    return render_template('order_history.html')

@app.route ("/remove_from_cart/<item>")
def remove_from_cart(item):
    cart = session.get('cart', {})
    
    if item in cart:
        del cart[item]
        session['cart'] = cart
        session.modified = True
        flash(f"Removed all {item} from the cart.")
    else:
        flash("Item not found in cart.")
    return redirect(url_for('index2'))

    session['cart'] = cart
    session.modified = True
    flash(f'Add-on added to cart.')
    return redirect(url_for('index2'))

@app.route ('/select_addon', methods=['POST'])
def select_addon():
    selected_addons = {}
    _, addons = load_data()

    selected_keys = request.form.getlist('addons') # get list of selected addons from form
   
    for addon_key in selected_keys:
        if addon_key in addons:
            selected_addons[addons]= float (addons [addons] ['price'])

    session['selected_addons'] = selected_addons
    session.modified = True
    return redirect(url_for('addons.json'))

if __name__ == '__main__':
    app.run(debug=True)