from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product
from .serializers import ProductSerializer

class ProductAPITest(APITestCase):
    def setUp(self):
        self.product1 = Product.objects.create(name='Test Product 1', price=10.99, quantity=100)
        self.product2 = Product.objects.create(name='Test Product 2', price=15.99, quantity=50)

    def test_get_products(self):
        url = reverse('get_products')  # Use 'get_products' endpoint name from urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Assuming we have 2 products in the database

    def test_get_product(self):
        url = reverse('get_product', args=[self.product1.id])  # Use 'get_product' endpoint name from urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Product 1')

    def test_add_to_cart(self):
        url = reverse('add_to_cart')  # Use 'add_to_cart' endpoint name from urls.py
        data = {'product_id': self.product1.id, 'quantity': 1}  # Assuming you're adding one unit of product to cart
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # You can add more assertions here if needed

    def test_get_cart(self):
        url = reverse('get_cart')  # Use 'get_cart' endpoint name from urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


