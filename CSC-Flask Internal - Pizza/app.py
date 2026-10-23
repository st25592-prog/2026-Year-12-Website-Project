import json

from flask import Flask, render_template, request, session, flash,  redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'


def load_data():
    with open('data/pizzas.json', 'r') as file:
        pizzas = json.load(file)

    with open('data/addons.json', 'r') as file:
        addons = json.load(file)

    return pizzas, addons

@app.route('/')
def index():
    cart = session.get('cart', {})
    selected_addons = session.get('selected_addons', {})
    pizzas, addons = load_data()
    total = calculate_total(cart, selected_addons)
    return render_template('index.html', pizzas=pizzas, addons=addons, cart=cart, selected_addons=selected_addons, total=total)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    # Get the selected pizza name from the form
    pizza_name = request.form.get('pizzas')

    # Get the quantity selected
    try:
        quantity = int(request.form.get('quantity', 1))
        if quantity < 1:
            raise ValueError
    except (ValueError, TypeError):
        flash('Please enter a valid quantity.')
        return redirect(url_for('index'))

    # Load the pizza menu
    pizzas, addons = load_data()

    # Check that the selected pizza exists
    if pizza_name not in pizzas:
        flash('Invalid pizza selected.')
        return redirect(url_for('index'))

    # Get the cart from the session
    cart = session.get('cart', {})

    # Get the selected pizza's details
    pizza_details = pizzas[pizza_name]
    price = float(pizza_details['price'])

    # Check stock availability
    current_quantity = cart.get(pizza_name, {}).get('quantity', 0)
    new_quantity = current_quantity + quantity

    if new_quantity > int(pizza_details['stock']):
        flash(f"Only {pizza_details['stock']} {pizza_name} pizzas are available.")
        return redirect(url_for('index'))

    # Add pizza or increase its quantity
    if pizza_name in cart:
        cart[pizza_name]['quantity'] = new_quantity
    else:
        cart[pizza_name] = {
            'price': price,
            'quantity': quantity
        }

    # Save the updated cart
    session['cart'] = cart
    session.modified = True

    flash(f'{quantity} {pizza_name} pizza(s) added to your cart!')
    return redirect(url_for('index'))


def calculate_total(cart, selected_addons):
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    total = total + sum(selected_addons.values())
    return total

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/checkout")
def checkout():
    cart = session.get("cart", {})
    selected_addons = session.get("selected_addons", {})

    total = calculate_total(cart, selected_addons)

    return render_template(
        "invoice.html",
        cart=cart,
        selected_addons=selected_addons,
        total=total
    )

@app.route('/orders')
def order_history():
    return render_template('order_history.html')

@app.route("/remove_from_cart/<item>")
def remove_from_cart(item):
    cart = session.get('cart', {})
    
    if item in cart:
        del cart[item]
        session['cart'] = cart
        session.modified = True
        flash(f"Removed all {item} from the cart.")
    else:
        flash("Item not found in cart.")
    return redirect(url_for('index'))

    session['cart'] = cart
    session.modified = True
    flash(f'Add-on added to cart.')
    return redirect(url_for('index'))

@app.route ('/selected_addons', methods=['POST'])
def selected_addons():
    selected_addons = {}
    _, addons = load_data()

    selected_keys = request.form.getlist('addons') # get list of selected addons from form
   
    for addon in selected_keys:
        if addon in addons:
            selected_addons[addon] = float (addons [addon] ['price'])

    session['selected_addons'] = selected_addons
    print(session)
    session.modified = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)