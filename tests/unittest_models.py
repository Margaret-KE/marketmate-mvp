import unittest
from app.models.product import Product

class TestProductModel(unittest.TestCase):
    def test_product_creation(self):
        # Test creating a new product
        product = Product(name='Test Product', price=10.99, category='Test Category')
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.price, 10.99)
        self.assertEqual(product.category, 'Test Category')

if __name__ == '__main__':
    unittest.main()

