from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'api'  # Explicitly specify the app label

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()

    class Meta:
        app_label = 'api'  # Explicitly specify the app label

    def __str__(self):
        return self.username

