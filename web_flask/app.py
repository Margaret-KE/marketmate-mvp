# app.py

from flask import Flask, jsonify, request, redirect, url_for, flash, session, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os
from dotenv import load_dotenv
import pymysql.cursors
import database_operations

# Load environment variables from .env file
load_dotenv()

# Database configuration
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# Connect to the database
connection = pymysql.connect(host=DB_HOST,
                             user=DB_USER,
                             password=DB_PASSWORD,
                             database=DB_NAME,
                             cursorclass=pymysql.cursors.DictCursor)

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Authentication decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page', 'error')
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# Routes for user authentication
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = database_operations.get_user_by_username(username)
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            flash('Logged in successfully', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password)
        if not database_operations.get_user_by_username(username):
            database_operations.add_user(username, email, hashed_password)
            flash('Account created successfully. Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Username already exists. Please choose a different one.', 'error')
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully', 'success')
    return redirect(url_for('index'))

# Routes for product management, order processing, cart management, search and filtering, admin dashboard, discount code handling, etc. go here...

@app.route('/products')
def products():
    # Retrieve and display products from the database
    products = database_operations.get_products()
    return render_template('products.html', products=products)

# Other routes and logic for the MarketMate app go here...

if __name__ == '__main__':
    app.run(debug=True)

