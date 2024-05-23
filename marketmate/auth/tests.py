# marketmate/auth/tests.py

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

class AuthAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_login(self):
        url = reverse('login')
        data = {'username': 'testuser', 'password': '12345'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        url = reverse('register')
        data = {'username': 'newuser', 'password1': 'newpass123', 'password2': 'newpass123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration

    def test_logout(self):
        url = reverse('logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Redirect after logout

