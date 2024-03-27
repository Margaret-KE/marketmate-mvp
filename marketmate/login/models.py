# marketmate/login/models.py

from django.db import models
from django.contrib.auth.models import User

class LoginSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Session for {self.user.username}"

