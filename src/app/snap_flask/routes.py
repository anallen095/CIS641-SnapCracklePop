from snap_flask.database import crsr, cnxn
from snap_flask.User import User
from snap_flask.customer import Customer
from flask import render_template, redirect, url_for, flash, Flask, request, jsonify, session, app
from snap_flask.forms import RegisterForm, LoginForm, updateForm, customerSearchForm, updateCustomerForm, unlockAccount
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta
import flask_excel as excel

# Create a Flask app instance
app=Flask(__name__)

# Set a secret key for your Flask application
app.config['SECRET_KEY'] = 'key'

#Flask Login Stuff
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# Define a function to load a user for Flask Login
@login_manager.user_loader
def load_user(userID):
    user_row = crsr.execute('SELECT userID, username, firstName, lastName, managerID, roleID, emailAddress FROM Users WHERE username = ?', (userID,)).fetchone()
    if user_row:
        return User(user_row.userID, user_row.username,user_row.firstName, user_row.lastName, user_row.managerID, user_row.roleID, user_row.emailAddress)
    return None

# Makes session time out after 30 minutes
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)

# Bcrypt for password hashing
bcrypt = Bcrypt(app)

# Define a route for the homepage
@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html', title='Homepage')



# Define a route for user login
@app.route('/login', methods=['POST', 'GET'])
def login():
    # Create a login form instance
    form = LoginForm()
    # Gets user information from database
    if form.validate_on_submit():
        user_data = crsr.execute('SELECT userID, password, username, firstName, lastName, managerID, roleID, emailAddress, loginAttempt, accountLocked FROM Users WHERE username = ?', (form.username.data,)).fetchone()
        attempt = int(user_data.loginAttempt)
        locked = int(user_data.accountLocked)

        # checks if a user exists
        if user_data and user_data[0] is not None:
            # checks if account is locked
            if locked > 0: 
                flash(f'Account Locked. Please contat admin', category='danger')
            # checks passowrd attempts
            elif attempt < 3: 
                if bcrypt.check_password_hash(user_data.password, form.password.data):
                    usr = User(user_data.userID, user_data.username,user_data.firstName, user_data.lastName, user_data.managerID, user_data.roleID, user_data.emailAddress)
                    login_user(usr)
                    return redirect(url_for('dashboard'))
                else:
                    flash(f'Wrong Password', category='danger')
                    loginAttempt = attempt + 1
                    crsr.execute("UPDATE [dbo].[Users] SET [loginAttempt] = ? WHERE [username] = ?", attempt,form.username.data)
                    cnxn.commit()
                    return redirect(url_for('login'))
            else: 
                flash(f'Three Login Failures Occurred. Account Locked.', category='danger')
                crsr.execute("UPDATE [dbo].[Users] SET [accountLocked] = ? WHERE [username] = ?", 1,form.username.data)
                cnxn.commit()
        else: 
            flash(f'User Does Not Exist', category='danger')
            return redirect(url_for('login'))

    return render_template('login.html', title='Login', form=form)


# Define a route for user logout
@app.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    flash(f'User Sucessfully Logged Out. Thanks for stopping by!', category='sucess')
    return redirect(url_for('login'))


# Define a route for customer updates
@app.route('/customer')
@login_required
def customer():
    crsr.execute("SELECT customerName, customerNbr, customerChannel, planTo, planToDescritpion, salesA, salesB, salesC, salesD, salesE FROM customers")
    data = crsr.fetchall()
    headings = ("Customer Name", "Customer Nbr", "Channel", "Plan To Nbr", "Plan To Description", "Sales A", "Sales B","Sales C","Sales D","Sales E",)
    return render_template("table.html", headings=headings, data=data, lg='Customer Data')

# Define a route for user password forgot
@app.route('/forgot')
@login_required
def forgot():
    return render_template('forgot.html', title='Forgot Password')

# Define a route for user registration
@app.route('/register',methods=['POST','GET'])
@login_required
def register():
    # create RegisterForm instance
    form=RegisterForm()

    if form.validate_on_submit():
        # encrypts password
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        
        # Checks for duplicate username
        existing_user_count = crsr.execute('SELECT COUNT(*) FROM Users WHERE username = ?', (form.username.data,)).fetchone()
        if existing_user_count and existing_user_count[0] > 0:
            flash(f'Username is already taken. Please choose a different one.', category='danger')
            return redirect(url_for('register'))
        else:
            # Get the maximum user ID
            maxid_result = crsr.execute("SELECT MAX(userID) FROM Users;").fetchone()
            maxid = maxid_result[0] if maxid_result[0] is not None else 0

            # Generate a new user ID
            newID = maxid + 1
            print(newID)

            # Insert the new user in database
            crsr.execute("INSERT INTO Users ([userID],[username],[firstName],[lastName],[password],[emailAddress],[managerID],[roleID]) VALUES (?,?, ?, ?,?, ?, ?, ?)", 
                         newID, form.username.data, form.firstName.data, form.lastName.data, hashed_password, form.emailAddress.data, 1, 1)
            # updates change log
            crsr.execute("INSERT INTO [dbo].[changeLog] ([username],[time],[action]) VALUES (?, ?, ?)",form.username.data, datetime.now(), 'Register Account')
            cnxn.commit()
            flash(f'Account has been registered. It is now pending approval from our admin team', category='success')

            return redirect(url_for('login'))
        
    return render_template('register.html', title='User Registration',form=form)

# Defines route for dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', title='User Dashboard')

# defines route user database table
@app.route('/users')
@login_required
def users():
    crsr.execute("SELECT username, firstName, lastName, managerID, roleID from Users")
    data = crsr.fetchall()
    headings = ("Username", "First Name", "Last Name", "Manager", "Role")
    return render_template("table.html", headings=headings, data=data, lg='User Data')

# defines route for sales database table
@app.route('/sales')
@login_required
def sales():
    return render_template('sales.html', title='Sales Hier')

# defines route for unlock account for admins 
@app.route('/admin',methods=['POST','GET'])
@login_required
def admin():
    form = unlockAccount()

    if request.method == "POST":
        crsr.execute("UPDATE [dbo].[Users] SET [accountLocked] = ? WHERE [username] = ?", 0 ,form.username.data)
        crsr.execute("INSERT INTO [dbo].[changeLog] ([username],[time],[action]) VALUES (?, ?, ?)", current_user.username, datetime.now(), 'Unlocked Account')
        cnxn.commit()
        flash(f'Account Unlocked!','success')
        return redirect(url_for('admin'))

    return render_template('admin.html', title='Admin', form=form)


# Defines a route to update a customer account
@app.route('/updatec')
@login_required
def updatec():
    return render_template('updatec.html', title='Update Customer')

# Defines a route to deactivate a user account
@app.route('/deactivate')
@login_required
def deactivate():
    return render_template('deactivate.html', title='Deactivate User')

# Defines a route to search the database for a customer
@app.route('/customerSearch',methods=['POST','GET'])
@login_required
def customerSearch():
    # Creates an instance of the customerSearchForm
    form=customerSearchForm()

    if form.validate_on_submit():  # Check if the form was submitted and is valid
        search_val = form.customerNbr.data
        crsr.execute("SELECT customerNbr FROM customers WHERE customerNbr = ?", search_val)
        customer_data = crsr.fetchone()  # Use fetchone() to retrieve a single row

        if customer_data:
            cust = Customer(search_val)
            return render_template('customerDash.html', title='Customer Search', cust = cust)
        else:
            flash(f'Customer Does Not Exist', category='danger')
            return redirect(url_for('login'))

    return render_template('customerSearch.html', title='Customer Search', form=form, lg='Customer Dashboard')



# Defines the route for the customer dashboard, only accessible via customer search
@app.route('/customerDash')
@login_required
def cDash(nbr):
    cust = Customer(nbr)
    form=updateCustomer(cust)
    id = cust.id

    if request.method == "POST":
        crsr.execute("UPDATE [dbo].[customers] SET [customerName] = ?,[customerChannel] = ?,[soldToNbr] = ?,[payerNbr] = ?,[altPayer] = ,[altPayer2] = ?,[salesA] = ?,[salesB] = ?,[salesC] = ? ,[salesD] = ? ,[salesE] = ? ,[planTo] = ? ,[planToDescritpion] = ? WHERE customerNbr = ?", form.name.data, form.channel.data, form.soldTo.data, form.payer.data, form.altPayer.data, form.altPayer2.data, form.SaleA.data, form.SaleB.data, form.SaleC.data,form.SalesD.data,form.SalesE.data, form.planTo.data, form.planToName.data, cust.id)
        crsr.execute("INSERT INTO [dbo].[changeLog] ([username],[time],[action]) VALUES (?, ?, ?)", current_user.username, datetime.now(), 'Update Customer')
        cnxn.commit()
        flash(f'Customer Updated Successfully!','success')
        return redirect(url_for('dashboard'))

    return render_template('customerDash.html', title='Customer Search', cust = cust, lg='Customer Dashboard')



@app.route('/updateCustomer',methods=['POST','GET'])
@login_required
def updateCustomer():
    form=updateCustomerForm()
    nbr = '1234567890'
    cust = Customer(nbr)
    id = cust.id

    if request.method == "POST":
        crsr.execute("UPDATE [dbo].[customers] SET [customerName] = ?,[customerChannel] = ?,[soldToNbr] = ?,[payerNbr] = ?,[altPayer] = ?,[altPayer2] = ?,[salesA] = ?,[salesB] = ?,[salesC] = ? ,[salesD] = ? ,[salesE] = ? ,[planTo] = ? ,[planToDescritpion] = ? WHERE customerNbr = ?", form.name.data, form.channel.data, form.soldTo.data, form.payer.data, form.altPayer.data, form.altPayer2.data, form.SaleA.data, form.SaleB.data, form.SaleC.data,form.SalesD.data,form.SalesE.data, form.planTo.data, form.planToName.data, cust.id)
        crsr.execute("INSERT INTO [dbo].[changeLog] ([username],[time],[action]) VALUES (?, ?, ?)", current_user.username, datetime.now(), 'Update Customer')
        cnxn.commit()
        flash("Customer Updated Successfully!")
        return redirect(url_for('customerSearch'))

    return render_template('updatec.html',form=form, id=id, cust=cust)

# Defines a route and method to update a user account
@app.route('/updateu',methods=['POST','GET'])
@login_required
def updateu():
    form = updateForm()
    nameToUpdate = crsr.execute("SELECT firstName, lastName, emailAddress, managerID, roleID FROM users where username  = ?", (current_user.username,)).fetchone()

    if request.method == "POST":
        print('hello')
        crsr.execute("UPDATE [dbo].[Users] SET [firstName] = ?, [lastName] = ?, [emailAddress] = ?, [managerID] = ?, [roleID] = ? WHERE username = ?", form.firstName.data, form.lastName.data, form.emailAddress.data, form.managerID.data, form.roleID.data, current_user.username)
        crsr.execute("INSERT INTO [dbo].[changeLog] ([username],[time],[action]) VALUES (?, ?, ?)", current_user.username, datetime.now(), 'Update User')
        cnxn.commit()
        flash(f'User Updated Successfully!','success')
        return redirect(url_for('dashboard'))

    return render_template('updateu.html',form=form,name_to_update = nameToUpdate, id=current_user.username)

# Creates a route and defines method to download the data from the tables
@app.route('/download/<data>', methods=['GET'])
@login_required
def download_data(data):
    print_data = data
    excel.init_excel(app)
    extension_type = "csv"
    filename = "dataDownload" + "." + extension_type
    d = {'colName': print_data}
    return excel.make_response_from_dict(d, file_type=extension_type, file_name=filename)