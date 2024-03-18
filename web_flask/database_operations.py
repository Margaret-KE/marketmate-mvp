import pymysql.cursors

# Function to establish database connection
def get_connection():
    connection = pymysql.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='your_database_name',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# Function to fetch all products from the database
def get_products():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM products"
            cursor.execute(sql)
            products = cursor.fetchall()
            return products
    finally:
        connection.close()

# Function to add a new user to the database
def add_user(username, email, password):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (username, email, password))
            connection.commit()
    finally:
        connection.close()

# Function to retrieve user by username
def get_user_by_username(username):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE username = %s"
            cursor.execute(sql, (username,))
            user = cursor.fetchone()
            return user
    finally:
        connection.close()

# Function to add a product to the cart
def add_to_cart(user_id, product_id, quantity):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # Check if the product is already in the cart
            sql = "SELECT * FROM cart WHERE user_id = %s AND product_id = %s"
            cursor.execute(sql, (user_id, product_id))
            existing_item = cursor.fetchone()

            if existing_item:
                # Update the quantity if the product is already in the cart
                new_quantity = existing_item['quantity'] + quantity
                sql = "UPDATE cart SET quantity = %s WHERE user_id = %s AND product_id = %s"
                cursor.execute(sql, (new_quantity, user_id, product_id))
            else:
                # Add the product to the cart
                sql = "INSERT INTO cart (user_id, product_id, quantity) VALUES (%s, %s, %s)"
                cursor.execute(sql, (user_id, product_id, quantity))
            connection.commit()
    finally:
        connection.close()

# Function to retrieve the items in the user's cart
def get_cart_items(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM cart WHERE user_id = %s"
            cursor.execute(sql, (user_id,))
            cart_items = cursor.fetchall()
            return cart_items
    finally:
        connection.close()

# Function to place an order
def place_order(user_id, cart_items):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # Insert order details into the orders table
            sql = "INSERT INTO orders (user_id) VALUES (%s)"
            cursor.execute(sql, (user_id,))
            order_id = cursor.lastrowid

            # Insert items from the cart into the order_items table
            for item in cart_items:
                sql = "INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)"
                cursor.execute(sql, (order_id, item['product_id'], item['quantity']))

            # Clear the user's cart after placing the order
            sql = "DELETE FROM cart WHERE user_id = %s"
            cursor.execute(sql, (user_id,))
            connection.commit()
    finally:
        connection.close()           

