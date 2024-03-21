from django.urls import path
from . import views

urlpatterns = [
    path('api/products/', views.get_products, name='get_products'),
    path('api/products/<int:product_id>/', views.get_product, name='get_product'),
    # Add more URL patterns as needed
]

urlpatterns = [
    path('api/products/', views.get_products, name='get_products'),
    path('api/products/<int:product_id>/', views.get_product, name='get_product'),
    path('api/cart/', views.get_cart, name='get_cart'),  # New URL pattern for retrieving the user's cart
    path('api/cart/add/', views.add_to_cart, name='add_to_cart'),  # New URL pattern for adding a product to the cart
    # Add more URL patterns as needed
]
