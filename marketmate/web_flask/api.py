from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for products
products = [
    {"id": 1, "name": "Baby Bag", "price": 20.99, "category": "Fashion"},
    {"id": 2, "name": "Techno Phone", "price": 399.99, "category": "Phones"},
    {"id": 3, "name": "Asus Laptop", "price": 799.99, "category": "Computers"},
]

# Placeholder for user's cart
cart = []

# Route to retrieve all products
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Route to retrieve a specific product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404

# Route to retrieve the user's cart
@app.route('/api/cart', methods=['GET'])
def get_cart():
    return jsonify(cart)

# Route to add a product to the cart
@app.route('/api/cart/add', methods=['POST'])
def add_to_cart():
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    if not product_id or not quantity:
        return jsonify({"error": "Product ID and quantity are required"}), 400

    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    cart.append({"product": product, "quantity": quantity})
    return jsonify({"message": "Product added to cart successfully"})

# Route to remove a product from the cart
@app.route('/api/cart/remove', methods=['POST'])
def remove_from_cart():
    data = request.json
    product_id = data.get('product_id')

    if not product_id:
        return jsonify({"error": "Product ID is required"}), 400

    for item in cart:
        if item['product']['id'] == product_id:
            cart.remove(item)
            return jsonify({"message": "Product removed from cart successfully"})

    return jsonify({"error": "Product not found in cart"}), 404

# Route to clear the user's cart
@app.route('/api/cart/clear', methods=['POST'])
def clear_cart():
    cart.clear()
    return jsonify({"message": "Cart cleared successfully"})

# Route for placing an order
@app.route('/api/orders/place', methods=['POST'])
def place_order():
    # Placeholder logic for order placement (e.g., validating cart, processing payment, etc.)
    if len(cart) == 0:
        return jsonify({"error": "Cart is empty"}), 400

    total_price = sum(item['product']['price'] * item['quantity'] for item in cart)
    # Placeholder logic for processing payment...
    
    # Placeholder logic for storing the order (e.g., in a database)
    orders.append({"items": cart, "total_price": total_price})
    
    # Clear the cart after placing the order
    cart.clear()

    return jsonify({"message": "Order placed successfully"})

# Route for user authentication
@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Placeholder logic for user authentication (e.g., checking credentials against a database)
    if username == 'admin' and password == 'admin':
        authenticated_users.append(username)
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"error": "Invalid username or password"}), 401

# Route for updating the quantity of a product in the cart
@app.route('/api/cart/update', methods=['POST'])
def update_cart():
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    if not product_id or not quantity:
        return jsonify({"error": "Product ID and quantity are required"}), 400

    for item in cart:
        if item['product']['id'] == product_id:
            item['quantity'] = quantity
            return jsonify({"message": "Cart updated successfully"})

    return jsonify({"error": "Product not found in cart"}), 404

# Route for retrieving orders
@app.route('/api/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

# Route for user logout
@app.route('/api/auth/logout', methods=['POST'])
def logout():
    data = request.json
    username = data.get('username')

    if username in authenticated_users:
        authenticated_users.remove(username)
        return jsonify({"message": "Logout successful"})
    else:
        return jsonify({"error": "User not authenticated"}), 401

# Placeholder route for user profile
@app.route('/api/profile', methods=['GET'])
def get_profile():
    # Placeholder logic for retrieving user profile
    # Replace this with actual logic to retrieve user profile information
    return jsonify({"username": "example_user", "email": "user@example.com", "age": 30})
# Other routes and logic for your application go here...

# Route for processing payment
@app.route('/api/payment/process', methods=['POST'])
def process_payment():
    # Placeholder logic for processing payment
    # Replace this with actual payment processing logic
    return jsonify({"message": "Payment processed successfully"})

# Route for applying a discount code
@app.route('/api/discount/apply', methods=['POST'])
def apply_discount_code():
    data = request.json
    discount_code = data.get('discount_code')

    # Placeholder logic for applying a discount code
    # Replace this with actual discount code validation and application logic
    if discount_code == 'DISCOUNT10':
        return jsonify({"message": "Discount applied successfully"})
    else:
        return jsonify({"error": "Invalid discount code"}), 400

# Route for retrieving product categories
@app.route('/api/categories', methods=['GET'])
def get_categories():
    # Placeholder logic for retrieving product categories
    # Replace this with actual logic to fetch categories from the database
    categories = ["Electronics", "Fashion", "Home & Kitchen", "Sports & Outdoors"]
    return jsonify(categories)

# Route for searching products
@app.route('/api/products/search', methods=['GET'])
def search_products():
    query = request.args.get('query')

    # Placeholder logic for searching products
    # Replace this with actual logic to search for products based on the query
    results = [
        {"id": 1, "name": "Product 1", "price": 19.99},
        {"id": 2, "name": "Product 2", "price": 29.99},
        {"id": 3, "name": "Product 3", "price": 39.99}
    ]
    return jsonify(results)

# Route for handling 404 errors
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Other routes and logic for your application go here...

# Route for user registration
@app.route('/api/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Placeholder logic for user registration
    # Replace this with actual user registration logic, such as adding the user to a database
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    # Example: Saving user to database
    # user = User(username=username, password=password)
    # db.session.add(user)
    # db.session.commit()

    return jsonify({"message": "User registered successfully"})

# Route for user profile update
@app.route('/api/profile/update', methods=['PUT'])
def update_profile():
    data = request.json
    # Retrieve user ID from session or request data
    user_id = data.get('user_id')
    new_username = data.get('new_username')
    new_email = data.get('new_email')

    # Placeholder logic for updating user profile
    # Replace this with actual logic to update user profile in the database
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    # Example: Updating user profile in the database
    # user = User.query.get(user_id)
    # user.username = new_username
    # user.email = new_email
    # db.session.commit()

    return jsonify({"message": "User profile updated successfully"})

# Route for resetting password
@app.route('/api/password/reset', methods=['POST'])
def reset_password():
    data = request.json
    username = data.get('username')
    email = data.get('email')

    # Placeholder logic for resetting password
    # Replace this with actual logic to reset password and send reset instructions to the user's email
    if not username or not email:
        return jsonify({"error": "Username and email are required"}), 400

    # Example: Sending password reset instructions to the user's email
    # Implement email sending logic here...

    return jsonify({"message": "Password reset instructions sent successfully"})

# Route for user deletion
@app.route('/api/user/delete', methods=['DELETE'])
def delete_user():
    data = request.json
    user_id = data.get('user_id')

    # Placeholder logic for deleting user
    # Replace this with actual logic to delete user from the database
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    # Example: Deleting user from the database
    # user = User.query.get(user_id)
    # db.session.delete(user)
    # db.session.commit()

    return jsonify({"message": "User deleted successfully"})
# Other routes and logic for your application go here...

# Route for retrieving user information
@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Placeholder logic for retrieving user information
    # Replace this with actual logic to fetch user data from the database
    user = {"id": user_id, "username": "example_user", "email": "example@example.com"}

    return jsonify(user)

# Route for updating user information
@app.route('/api/user/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    new_username = data.get('username')
    new_email = data.get('email')

    # Placeholder logic for updating user information
    # Replace this with actual logic to update user data in the database
    if not new_username and not new_email:
        return jsonify({"error": "Username or email is required"}), 400

    # Example: Updating user information in the database
    # user = User.query.get(user_id)
    # user.username = new_username
    # user.email = new_email
    # db.session.commit()

    return jsonify({"message": "User information updated successfully"})

# Route for retrieving product information
@app.route('/api/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    # Placeholder logic for retrieving product information
    # Replace this with actual logic to fetch product data from the database
    product = {"id": product_id, "name": "Example Product", "price": 9.99}

    return jsonify(product)

# Route for updating product information
@app.route('/api/product/update/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    new_name = data.get('name')
    new_price = data.get('price')

    # Placeholder logic for updating product information
    # Replace this with actual logic to update product data in the database
    if not new_name and not new_price:
        return jsonify({"error": "Name or price is required"}), 400

    # Example: Updating product information in the database
    # product = Product.query.get(product_id)
    # product.name = new_name
    # product.price = new_price
    # db.session.commit()

    return jsonify({"message": "Product information updated successfully"})


if __name__ == '__main__':
    app.run(debug=True)

