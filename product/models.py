from django.db import models
from django.utils import timezone

class Product(models.Model):
    image = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.FloatField()
    composition = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.model

class Suits(models.Model):
    product = models.ForeignKey(Product, related_name='suits', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Suits for {self.product.model}"

class Pants(models.Model):
    product = models.ForeignKey(Product, related_name='pants', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Pants for {self.product.model}"

class WomenSuit(models.Model):
    product = models.ForeignKey(Product, related_name='women_suit', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Women's Suit for {self.product.model}"

class Accessories(models.Model):
    product = models.ForeignKey(Product, related_name='accessories', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Accessory for {self.product.model}"

from django.contrib.auth.models import User

class UserHasSuits(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    suits = models.ForeignKey(Suits, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} has {self.suits}"

class Sales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=100)
    value = models.FloatField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Sale of {self.product.model}"

class DataDash(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=100)
    value = models.FloatField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Data Dashboard for {self.product.model}"
