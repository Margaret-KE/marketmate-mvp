# marketmate/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include URLs from the 'api' app
    path('auth/', include('auth.urls')),  # Include URLs from the 'auth' app
    path('login/', include('login.urls')),  # Include URLs from the 'login' app
    # Add more URL patterns as needed
]
