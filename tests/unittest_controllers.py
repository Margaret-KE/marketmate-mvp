import unittest
from app.controllers.product_controller import get_products

class TestProductController(unittest.TestCase):
    def test_get_products(self):
        # Test the get_products function
        products = get_products()
        self.assertIsNotNone(products)
        self.assertIsInstance(products, list)

if __name__ == '__main__':
    unittest.main()

