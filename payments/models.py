from django.db import models
from django.contrib.auth.models import User
from subscriptions.models import Subscription

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=50, choices=[
        ('cash', 'Готівка'),
        ('card', 'Картка'),
        ('online', 'Онлайн-платіж'),
    ])

    def __str__(self):
        return f"{self.user.username} — {self.amount} грн ({self.method})"
