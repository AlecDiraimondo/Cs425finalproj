from webstore import db
from datetime import datetime

class Customer(db.Model):
    __tablename__ = 'Customer'
    c_id = db.Column(db.Integer, primary_key=True)
    c_username = db.Column(db.String(20), unique=True, nullable = False)
    password = db.Column(db.String(20), nullable = False)
    balance = db.Column(db.Integer, nullable = False)
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(20), nullable = False)
    def __repr__(self):
        return f"User('{self.c_username}','{self.c_id}', '{self.balance}')"  

class CreditCard(db.Model):
    __tablename__ = 'CreditCard'
    state = db.Column(db.String(20), nullable = False)
    zipcode = db.Column(db.String(20), nullable = False)
    street = db.Column(db.String(40), nullable = False)
    city = db.Column(db.String(20), nullable = False)
    cardnumber = db.Column(db.Integer, nullable = False, primary_key=True)
    c_id = db.Column(db.Integer, db.ForeignKey('Customer.c_id'))

class Product(db.Model):
    __tablename__ = 'Product'
    product_name= db.Column(db.String(20), nullable = False)
    product_category= db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.Integer, nullable= False)

class ShoppingCart(db.Model):
    __tablename__ = 'ShoppingCart'
    c_id = db.Column(db.Integer, db.ForeignKey('Customer.c_id'), primary_key = True)
    product_id = db.Column(db.Integer, db.ForeignKey('Product.product_id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable = False)

class Order(db.Model):
    __tablename__ = 'Order'
    order_id = db.Column(db.Integer, primary_key = True)
    subtotal = db.Column(db.Numeric(8,2), nullable=False)
    card_number = db.Column(db.Integer, primary_key = True)
    time_ordered = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    status = db.Column(db.String(20), nullable = False)

class OrderDetails(db.Model):
    __tablename__ = 'OrderDetails'
    quantity = db.Column(db.Integer, nullable = False)
    product_id = db.Column(db.Integer, db.ForeignKey('Product.product_id'), primary_key = True)
    order_id = db.Column(db.Integer, db.ForeignKey('Order.order_id'), primary_key = True)

class Warehouse(db.Model):
    __tablename__ = 'Warehouse'
    warehouse_id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(40), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(20), nullable=False)
    state = db.Column(db.Integer, nullable=False)
    capacity = db.Column(db.Integer) 

class Stock(db.Model):
    __tablename__ = 'Stock'
    warehouse_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)

class Shipping_Address(db.Model):
    __tablename__ = 'Shipping_Address'
    zipcode = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(20), primary_key=True)
    street = db.Column(db.String(40), primary_key=True)
    city = db.Column(db.String(20), nullable=False)
    order_id = db.Column(db.Integer)
    
class Cost(db.Model):
    __tablename__ = 'Cost'
    product_id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Numeric(8,2))

class Staff(db.Model):
    __tablename__ = 'Staff'
    s_username = db.Column(db.String(20), primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    job_title = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    salary = db.Column(db.Numeric(8,2))
    state = db.Column(db.String(20), nullable=False)
    street = db.Column(db.String(40), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)

class Food(db.Model):
    __tablename__ = 'Food'
    product_id = db.Column(db.Integer, primary_key=True)
    food_category = db.Column(db.String(20), nullable=False)
    calories = db.Column(db.Integer, nullable=False)

class Alcohol(db.Model):
    __tablename__ = 'Alcohol'
    product_id = db.Column(db.Integer, primary_key=True)
    alcohol_category = db.Column(db.String(20), nullable=False)
    alcohol_content = db.Column(db.Numeric(3,1))
