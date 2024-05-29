# marketmate/login/tests.py

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import LoginSession

class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password123'})
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertTrue(response.url.startswith('/'))  # Redirected to home page
        # You can add more assertions here to test if the user is logged in successfully

    def test_logout_view(self):
        # Login the user first
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertEqual(response.url, '/')  # Redirected to home page after logout
        # You can add more assertions here to test if the user is logged out successfully

    def test_login_session_model(self):
        session = LoginSession.objects.create(user=self.user)
        self.assertEqual(str(session), f"Session for {self.user.username}")
        # You can add more assertions here to test other attributes of the LoginSession model

