import unittest
from app import app

class TestRoutes(unittest.TestCase):
    def test_home_route(self):
        # Test the home route
        client = app.test_client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to MarketMate', response.data)

if __name__ == '__main__':
    unittest.main()

