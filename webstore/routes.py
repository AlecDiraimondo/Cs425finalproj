from flask import render_template, url_for, flash, redirect
from webstore import app, db
from webstore.forms import RegistrationForm, CustomerLoginForm, CreditCardForm
from webstore.models import Customer, Product, Food, Alcohol, Warehouse, CreditCard
from flask_login import login_user, current_user, logout_user


@app.route('/')

@app.route('/home')  #now we have 2 routes to get to the hello_world page --> /home and just /
def home():
    return render_template('home.html')

@app.route('/shop')  #new route, new function -> Allows us to have multiple pages easily.
def shop():
    resultFood=Product.query.join(Food, Product.product_id==Food.product_id).add_columns(Product.product_name, Food.calories, Product.size)
    resultAlcohol=Product.query.join(Alcohol, Product.product_id==Alcohol.product_id).add_columns(Product.product_name, Alcohol.alcohol_content, Product.size)
    return render_template('shop.html', productsFood=resultFood, productsAlcohol=resultAlcohol, title='Products')

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

