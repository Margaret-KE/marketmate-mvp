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
    return render(request, 'login.html')  # Render the login.html template for GET requests

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
    return render(request, 'register.html')  # Render the register.html template for GET requests

