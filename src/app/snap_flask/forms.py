from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError,Email,EqualTo
from snap_flask.User import User
from snap_flask.customer import Customer



class RegisterForm(FlaskForm):
    username = StringField(label='Username',validators=[InputRequired(), Length(min=4, max=20)])
    firstName = StringField(label='First Name',validators=[InputRequired(), Length(min=4, max=20)])
    lastName = StringField(label='Last Name',validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField(label='Password',validators=[InputRequired(), Length(min=8, max=20)])
    confirmPassword = PasswordField(label='Confirm Password',validators=[InputRequired(), Length(min=8, max=20),EqualTo('password')])
    emailAddress = StringField(label='Email',validators=[InputRequired(), Length(min=4, max=80), Email()])
    managerID = StringField(label='Manager Name',validators=[InputRequired(), Length(min=4, max=80)])
    roleID = StringField(label='Role ID',validators=[InputRequired(), Length(min=4, max=80)])

    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField(label='Username',validators=[InputRequired()])
    password = PasswordField(label='Password',validators=[InputRequired()])
       
    submit = SubmitField('Login')

class updateForm(FlaskForm):
    username = StringField(label='Username',validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField(label='Password',validators=[InputRequired(), Length(min=8, max=20)])
    confirmPassword = PasswordField(label='Confirm Password',validators=[InputRequired(), Length(min=8, max=20),EqualTo('password')])
    firstName =  StringField(render_kw={"placeholder": "current_user.firstName"})
    lastName =  StringField(render_kw={"placeholder": "current_user.lastName"})
    emailAddress = StringField(render_kw={"placeholder": "current_user.email"})
    managerID = StringField(render_kw={"placeholder": "current_user.manager"})
    roleID = StringField(render_kw={"placeholder": "current_user.role"})


    submit = SubmitField('Update')

class customerSearchForm(FlaskForm):
    customerNbr = StringField(label='Customer Number')
       
    submit = SubmitField('Search')

class unlockAccount(FlaskForm):
    username = StringField(label='Username')
       
    submit = SubmitField('Search')

class updateCustomerForm(FlaskForm):
    customerNbr = StringField()
    name = StringField()
    channel = StringField()
    SaleA = StringField()
    SaleB =  StringField()
    SaleC =  StringField()
    SalesD = StringField()
    SalesE = StringField()
    planTo = StringField()
    planToName = StringField()
    soldTo = StringField()
    payer = StringField()
    altPayer = StringField()
    altPayer2 = StringField()

    submit = SubmitField('Update')

