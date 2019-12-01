from flask_wtf  import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from webstore.models import Customer



class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    first_name = StringField('First Name',
                            validators=[DataRequired(),Length(min=2,max=20)])
    last_name = StringField('Last Name',
                            validators=[DataRequired(),Length(min=2,max=20)])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password',
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = Customer.query.filter_by(c_username=username.data).first()
        if user:
            raise ValidationError('That Username already exists')



class CustomerLoginForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Login')

class CreditCardForm(FlaskForm):
    
    cardnumber = StringField('Credit Card Number', validators=[DataRequired(), Length(min=16,max=16)])
    state = StringField('State', validators=[DataRequired(), Length(min=2,max=4)])
    zipcode = IntegerField('Zip Code', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired(),Length(min=2,max=20)])
    street = StringField('Street', validators=[DataRequired(), Length(min=2,max=20)])
    submitcard = SubmitField('Add/Update Card')

class AddressForm(FlaskForm):

    id = IntegerField('id')
    state = StringField('State', validators=[DataRequired(), Length(min=2,max=4)])
    zipcode = IntegerField('Zip Code', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired(),Length(min=2,max=20)])
    street = StringField('Street', validators=[DataRequired(), Length(min=2,max=20)])
    submitaddress = SubmitField('Add Shipping Address') 

class CheckoutForm(FlaskForm):
    a_select = SelectField('Select')
    update = SubmitField('Calculate Price')
    submit = SubmitField('Checkout')
    
class AccountForm(FlaskForm):
    cardupdate = SubmitField('Update Card')
    carddelete = SubmitField('Delete Card')
    cardadd = SubmitField('Add Card')
    addressupdate = SubmitField('Update Address')
    addressdelete = SubmitField('Delete Address')
    addressadd = SubmitField('Add Address')
    
class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2,max=20)])
    category = SelectField('Category', choices=[('food', 'Food products'), ('alcohol', 'Alcoholic drinks')])
    size = IntegerField('Volume', validators=[DataRequired()])
    extra = StringField('Extra info', validators=[DataRequired()])
    submit = SubmitField('Add')

class StockForm(FlaskForm):
    product = SelectField('Product')
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    submit = SubmitField('Add')