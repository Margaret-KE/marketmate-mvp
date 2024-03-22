from django.db import models

# marketmate/auth/models.py

from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields you need for user profile

    def __str__(self):
        return self.user.username

