from flask import render_template, url_for, flash, redirect, request
from webstore import app, db
from webstore.forms import RegistrationForm, CustomerLoginForm, CreditCardForm, AddressForm, CheckoutForm
from webstore.models import Customer, Product, Food, Alcohol, Warehouse, CreditCard, ShoppingCart, Shipping_Address, Cost, Order
from flask_login import login_user, current_user, logout_user


@app.route('/')

@app.route('/home')  #now we have 2 routes to get to the hello_world page --> /home and just /
def home():
    return render_template('home.html')

@app.route('/shop')  #new route, new function -> Allows us to have multiple pages easily.
def shop():
    resultFood=Product.query.join(Food, Product.product_id==Food.product_id).add_columns(Product.product_id,Product.product_name, Food.calories, Product.size)
    resultAlcohol=Product.query.join(Alcohol, Product.product_id==Alcohol.product_id).add_columns(Product.product_id,Product.product_name, Alcohol.alcohol_content, Product.size)
    return render_template('shop.html', productsFood=resultFood, productsAlcohol=resultAlcohol)
@app.route('/warehouse') #creates warehouse page
def warehouse():
    result=Warehouse.query.all()
    return render_template('warehouse.html', warehouseData=result, title='Warehouse')

@app.route('/login', methods=['GET', 'POST'])
def customer_login(): #Customer Login page
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = CustomerLoginForm()
    if form.validate_on_submit(): #checking validation of data
        user = Customer.query.filter_by(c_username=form.username.data).first()
        if user and (user.password == form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccesful, No account exists!', 'danger')
        return redirect(url_for('home'))

    return render_template('customerlogin.html', title='Customer Login',form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit(): #checking validation of data
        customer = Customer(c_username=form.username.data, password=form.password.data,balance=0,
                            first_name=form.first_name.data, last_name=form.last_name.data)
        db.session.add(customer)
        db.session.commit()
        flash(f'Account Created!', 'success')
        return redirect(url_for('customer_login'))
    return render_template('register.html', title = 'Register',form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account", methods = ['GET', 'POST'])
def account():
    form = CreditCardForm()
    if form.validate_on_submit():
        creditcard = CreditCard(state=form.state.data,zipcode = form.zipcode.data, street = form.street.data,
                                city = form.city.data, cardnumber = form.cardnumber.data, c_id = (current_user.get_id()))
        db.session.add(creditcard)
        db.session.commit()
        flash(f'Credit Card added', 'success')
        return redirect(url_for('shop'))
    return render_template('account.html', title='Account', form=form)

@app.route("/add", methods=['POST'])
def add_to_cart():
    quant = int(request.form['quantity'])
    prod_id = request.form['id']
    if request.method == 'POST':
        product = ShoppingCart(c_id = (current_user.get_id()), product_id = prod_id, quantity = quant)
        db.session.add(product)
        db.session.commit()
        flash(f'Product Added to cart', 'success')
        return redirect(url_for('shop'))
    return redirect(url_for('shop'))

@app.route("/addadress", methods=['GET', 'POST'])
def add_address():
    form = AddressForm()
    if form.validate_on_submit():
        address = Shipping_Address(zipcode = form.zipcode.data, state = form.state.data, street = form.street.data,
                                  city = form.city.data, customer_id = (current_user.get_id()))
        db.session.add(address)
        db.session.commit()
        flash(f'Shipping Address Added!', 'success')
        return redirect(url_for('checkout'))
    return render_template('address.html', title = 'Add Address', form=form)

@app.route("/Checkout", methods=['GET', 'POST'])
def checkout():
    form = CheckoutForm()
    address = Shipping_Address.query.filter_by(customer_id=current_user.get_id()).first()
    if address:
        resultCart = ShoppingCart.query.filter_by(c_id=current_user.get_id()).join(Product).add_columns(Product.product_id, Product.product_name, ShoppingCart.quantity)
        resultaddress = Shipping_Address.query.filter_by(customer_id=current_user.get_id())
        first_state = (resultaddress.first()).state #getting first address's state to populate our price column

        prices = []
        for results in resultCart:
            quantity = results.quantity
            prod_id = results.product_id
            Cost_per_item = ((Cost.query.filter_by(product_id = prod_id, state=first_state)).first()).price
            itemprice = Cost_per_item * quantity
            prices.append(itemprice)
        totalprice  = 0 
        for price in prices:
            totalprice += price
        zipped_data = zip(resultCart, prices) #this creates an object with 2 values, to use in our table
        
        if form.validate_on_submit(): #this method currently does not work 
            db.session.delete(resultCart)
            db.session.commit()
            flash(f'Checkout Succesful!', 'success')
            creditcard = (CreditCard.query.filter_by(c_id=current_user.get_id())).first()
            order = Order(subtotal = totalprice, card_number=creditcard.cardnumber,)
            db.session.add(order)
            db.session.commit()
            return redirect(url_for('home'))
        return render_template('checkout.html', Cart = zipped_data, addresslist = resultaddress, Prices = prices, total = totalprice, title = 'Checkout', form=form)
    
    else:
        flash(f'No shipping Address found. Please Add one!', 'danger')
        return redirect(url_for('home'))