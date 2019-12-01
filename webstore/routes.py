from flask import render_template, url_for, flash, redirect, request
from sqlalchemy.sql import func
from webstore import app, db
from webstore.forms import RegistrationForm, CustomerLoginForm, CreditCardForm, AddressForm, CheckoutForm, AccountForm, ProductForm, StockForm
from webstore.models import Customer, Product, Food, Alcohol, Warehouse, CreditCard, ShoppingCart, Shipping_Address, Cost, Order, Staff, Stock, Food, Alcohol
from flask_login import login_user, current_user, logout_user


@app.route('/')

@app.route('/home')  #now we have 2 routes to get to the hello_world page --> /home and just /
def home():
    return render_template('home.html')
    
@app.route('/staff')  #now we have 2 routes to get to the hello_world page --> /home and just /
def staff():
    return render_template('staff.html')

@app.route('/shop')  #new route, new function -> Allows us to have multiple pages easily.
def shop():
    resultFood=Product.query.join(Food, Product.product_id==Food.product_id).add_columns(Product.product_id,Product.product_name, Food.calories, Product.size)
    resultAlcohol=Product.query.join(Alcohol, Product.product_id==Alcohol.product_id).add_columns(Product.product_id,Product.product_name, Alcohol.alcohol_content, Product.size)
    return render_template('shop.html', productsFood=resultFood, productsAlcohol=resultAlcohol)
    
@app.route('/warehouse', methods=['GET', 'POST']) #creates warehouse page
def warehouse():
    result=db.session.query(Warehouse.warehouse_id, Warehouse.city, Warehouse.street, Warehouse.zipcode, Warehouse.state, Warehouse.capacity, func.sum(Stock.quantity)).join(Stock, Warehouse.warehouse_id==Stock.warehouse_id).group_by(Warehouse.warehouse_id).all()
    print(result)
    return render_template('warehouse.html', warehouseData=result, title='Warehouse')
 
@app.route('/products', methods=['GET', 'POST']) #creates products page
def products():
    resultFood=Product.query.join(Food, Product.product_id==Food.product_id).add_columns(Product.product_id,Product.product_category, Product.product_name, Food.calories, Product.size)
    resultAlcohol=Product.query.join(Alcohol, Product.product_id==Alcohol.product_id).add_columns(Product.product_id,Product.product_category,Product.product_name, Alcohol.alcohol_content, Product.size)
    return render_template('products.html', foodData=resultFood, alcoholData=resultAlcohol, title='Products')

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
            flash(f'Login Unsuccessful! Unknown username or password.', 'danger')
            return redirect(url_for('login'))

    return render_template('customerlogin.html', title='Customer Login',form=form)

@app.route('/stafflogin', methods=['GET', 'POST'])
def staff_login(): #Customer Login page
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = CustomerLoginForm()
    if form.validate_on_submit(): #checking validation of data
        user = Staff.query.filter_by(s_username=form.username.data).first()
        if user and (user.password == form.password.data):
            login_user(user)
            return redirect(url_for('staff'))
        else:
            flash(f'Login Unsuccessful! Unknown username or password.', 'danger')
            return redirect(url_for('staff_login'))

    return render_template('stafflogin.html', title='Staff Login',form=form)
    
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

@app.route("/addstock", methods=['GET', 'POST'])
def addstock():
    form = StockForm()
    wid = request.args.get('id')
    
    if request.method == 'POST':
        pid=request.form.get("product")
        stock=Stock(product_id=pid, warehouse_id=wid, quantity=form.quantity.data)
        db.session.add(stock)
        db.session.commit()
        flash(f'Stock added', 'success')
        return redirect(url_for('warehouse'))
        
    winfo=Warehouse.query.filter_by(warehouse_id=wid).first();
    products=Product.query.add_columns(Product.product_id, Product.product_name).all()
    choices=[]
    for product in products:
        choices.append((product.product_id, product.product_name))
    form.product.choices=choices
    
    return render_template('addstock.html', form=form, warehouse=winfo)
    
@app.route("/addproduct", methods=['GET', 'POST'])
def addproduct():
    form = ProductForm()
    if request.method == 'POST':
        product = Product(product_name=form.name.data, product_category=form.category.data, size=form.size.data)
        db.session.add(product)
        db.session.commit()
        if form.category.data=='food':
            food = Food(product_id=product.product_id, food_category='Yummy', calories=form.extra.data)
            db.session.add(food)
            db.session.commit()
        elif form.category.data=='alcohol':
            alcohol = Alcohol(product_id=product.product_id, alcohol_category='Yummy', alcohol_content=form.extra.data)
            db.session.add(alcohol)
            db.session.commit()
        flash(f'New product saved', 'success')
        return redirect(url_for('products'))
        
    return render_template('addproduct.html', form=form)
    
@app.route("/account", methods = ['GET', 'POST'])
def account():
    form = AccountForm()
    formcard = CreditCardForm()
    formaddress = AddressForm()
    resultaddress = Shipping_Address.query.filter_by(customer_id=current_user.get_id())
    resultcard = CreditCard.query.filter_by(c_id=current_user.get_id())
    selectcard=CreditCard.query.filter_by(cardnumber=request.form.get("Card")).first()
    selectaddress=Shipping_Address.query.filter_by(address_id=request.form.get("Address")).first()

    if request.method == 'POST':    
        print (request.form)
        if 'cardadd' in request.form:
            flash(f'Adding card!', 'success')
            return render_template('addcard.html', title='Account', fields="", form = formcard)
        elif 'carddelete' in request.form:
            db.session.delete(selectcard)
            db.session.commit()
            flash(f'Card deleted!', 'danger')
        elif 'cardupdate' in request.form:
            flash(f'Updating card!', 'success')
            return render_template('addcard.html', title='Account', fields=selectcard, form = formcard)
        elif 'addressadd' in request.form:
            flash(f'Adding Address!', 'success')
            return render_template('address.html', title='Account', fields="", form = formaddress)
        elif 'addressdelete' in request.form:
            db.session.delete(selectaddress)
            db.session.commit()
            flash(f'Address deleted!', 'danger')
        elif 'addressupdate' in request.form:
            flash(f'Updating address!', 'success')
            return render_template('address.html', title='Account', fields=selectaddress, form = formaddress)
            
        elif 'submitcard' in request.form:
            print('In cardadd')
            creditcard = CreditCard.query.filter(CreditCard.cardnumber==formcard.cardnumber.data).first()
            if(creditcard):
                print('Update')
                creditcard.state=formcard.state.data
                creditcard.street=formcard.street.data
                creditcard.city=formcard.city.data
                creditcard.zipcode=formcard.zipcode.data
            else:
                print('Add')
                creditcard = CreditCard(state=formcard.state.data,zipcode = formcard.zipcode.data, street = formcard.street.data, city = formcard.city.data, cardnumber = formcard.cardnumber.data, c_id = (current_user.get_id()))
                db.session.add(creditcard)
            db.session.commit()
            flash(f'Credit Card added/updated', 'success')
 
        elif 'submitaddress' in request.form:
            print('In addressadd')
            address = Shipping_Address.query.filter(Shipping_Address.address_id==formaddress.id.data).first()
            if(address):
                print('Update')
                address.state=formaddress.state.data
                address.street=formaddress.street.data
                address.city=formaddress.city.data
                address.zipcode=formaddress.zipcode.data
            else:
                print('Add')
                address = Shipping_Address(zipcode = formaddress.zipcode.data, state = formaddress.state.data, street = formaddress.street.data, city = formaddress.city.data, customer_id = (current_user.get_id()))
                db.session.add(address)
            db.session.commit()
            flash(f'Shipping address added/updated', 'success') 
    return render_template('account.html', title='Account', form=form, customer=current_user.c_username, cardlist=resultcard, addresslist=resultaddress)

@app.route("/add", methods=['POST'])
def add_to_cart():
    quant = int(request.form['quantity'])
    prod_id = request.form['id']
    if request.method == 'POST':
        exists = ShoppingCart.query.join(Product).filter(ShoppingCart.c_id==current_user.get_id(), Product.product_id==prod_id).first()
        if(exists):
            exists.quantity+=quant
        else:
            product = ShoppingCart(c_id = (current_user.get_id()), product_id = prod_id, quantity = quant)
            db.session.add(product)
        db.session.commit()
        flash(f'Product Added to cart', 'success')
        return redirect(url_for('shop'))
    return redirect(url_for('shop'))

@app.route("/Checkout", methods=['GET', 'POST'])
def checkout():
    form = CheckoutForm()
    address = Shipping_Address.query.filter_by(customer_id=current_user.get_id()).first()
    if address:
        print ('Have address')
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
        
        if request.method == 'POST':
            print('helloworld')
            if 'submit_button' in request.form:
                ShoppingCart.query.filter_by(c_id=current_user.get_id()).delete()
                db.session.commit()
                flash(f'Checkout Succesful, your order has been placed! Redirecting to home..', 'success')
                creditcard = (CreditCard.query.filter_by(c_id=current_user.get_id())).first()
                order = Order(subtotal = totalprice, card_number=creditcard.cardnumber)
                db.session.add(order)
                db.session.commit()
                return redirect(url_for('home'))
            elif 'select_address' in request.form:
                print ('Updating prize')
                select_state =  str(request.form.get("Address"))
                print (select_state)
                newprices = []
                for results in resultCart:
                    quantity = results.quantity
                    prod_id = results.product_id
                    Cost_per_item = ((Cost.query.filter_by(product_id = prod_id, state=select_state))).one().price
                    itemprice = Cost_per_item * quantity
                    newprices.append(itemprice)
                newtotalprice  = 0 
                for price in newprices:
                    newtotalprice += price
                new_zipped_data = zip(resultCart, newprices)
                return render_template('checkout.html', Cart = new_zipped_data, addresslist = resultaddress, Prices = newprices, total = newtotalprice, title = 'Checkout', form=form)
            else:
                return render_template('checkout.html', Cart = zipped_data, addresslist = resultaddress, Prices = prices, total = totalprice, title = 'Checkout', form=form)
        print('I am here')
        return render_template('checkout.html', Cart = zipped_data, addresslist = resultaddress, Prices = prices, total = totalprice, title = 'Checkout', form=form)
    else:
        flash(f'No shipping Address found. Please Add one!', 'danger')
        return redirect(url_for('home'))