import pytest
from app.models import User

def test_user_creation():
    user = User(username='testuser', email='test@example.com', password='password123')
    assert user.username == 'testuser'
    assert user.email == 'test@example.com'
    assert user.check_password('password123') == True

