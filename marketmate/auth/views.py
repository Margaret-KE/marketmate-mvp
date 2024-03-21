from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import database_operations

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('index')  # Redirect to the index page after login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not database_operations.get_user_by_username(username):
            database_operations.add_user(username, email, password)
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Username already exists. Please choose a different one.')
    return render(request, 'register.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('index')

@login_required
def product_details(request, product_id):
    product = database_operations.get_product_by_id(product_id)
    if product:
        return render(request, 'product_details.html', {'product': product})
    else:
        messages.error(request, 'Product not found')
        return redirect('products')

@login_required
def add_to_cart(request, product_id):
    database_operations.add_product_to_cart(request.user.id, product_id)
    messages.success(request, 'Product added to cart successfully')
    return redirect('products')

@login_required
def cart_view(request):
    cart_items = database_operations.get_cart_items(request.user.id)
    return render(request, 'cart.html', {'cart_items': cart_items})

@login_required
def checkout(request):
    if request.method == 'POST':
        # Process the order
        messages.success(request, 'Order placed successfully')
        return redirect('order_confirmation')
    else:
        cart_items = database_operations.get_cart_items(request.user.id)
        total_amount = calculate_total_amount(cart_items)  # Assuming you have a function to calculate total amount
        return render(request, 'checkout.html', {'cart_items': cart_items, 'total_amount': total_amount})

@login_required
def order_confirmation(request):
    return render(request, 'order_confirmation.html')

def search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        results = database_operations.search_products(search_query)
        return render(request, 'search_results.html', {'results': results})
    else:
        return render(request, 'search.html')

@login_required
def admin_dashboard(request):
    # Add authentication logic to ensure only admins can access this view
    return render(request, 'admin_dashboard.html')

@login_required
def apply_discount(request):
    messages.success(request, 'Discount code applied successfully')
    return redirect('checkout')  # Redirect to the checkout page after applying discount

# Function to calculate total amount for the order
def calculate_total_amount(cart_items):
    total_amount = sum(item['price'] for item in cart_items)
    return total_amount

