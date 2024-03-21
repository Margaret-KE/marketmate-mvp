# marketmate/api/views.py

from django.http import JsonResponse
from .models import Product  # Assuming you have a Product model defined in models.py
from django.views.decorators.csrf import csrf_exempt  # Only if you want to disable CSRF protection

# Sample data for products
products = [
    {"id": 1, "name": "Baby Bag", "price": 20.99, "category": "Fashion"},
    {"id": 2, "name": "Techno Phone", "price": 399.99, "category": "Phones"},
    {"id": 3, "name": "Asus Laptop", "price": 799.99, "category": "Computers"},
]

# Route to retrieve all products
def get_products(request):
    return JsonResponse(products, safe=False)

# Route to retrieve a specific product by ID
def get_product(request, product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return JsonResponse(product)
    else:
        return JsonResponse({"error": "Product not found"}, status=404)

# Other view functions for your API endpoints go here...
