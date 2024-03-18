import unittest
from app import app

class TestIntegration(unittest.TestCase):
    def test_user_registration(self):
        # Test registering a new user
        client = app.test_client()
        response = client.post('/register', data={'username': 'testuser', 'email': 'test@example.com', 'password': 'password123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Account created successfully', response.data)

if __name__ == '__main__':
    unittest.main()

