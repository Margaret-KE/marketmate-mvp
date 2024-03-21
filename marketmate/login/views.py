from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User  # Assuming you have a User model defined in models.py

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your home view
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
        else:
            # Create the new user
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')  # Replace 'login' with the name of your login view
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Replace 'login' with the name of your login view

