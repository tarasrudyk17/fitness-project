from django.db import models
from django.contrib.auth.models import User

class SubscriptionType(models.Model):
    CATEGORY_CHOICES = [
        ('morning', 'Ранкова'),
        ('daytime', 'Денна'),
        ('unlimited', 'Безлімітна'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_days = models.PositiveIntegerField(help_text="Тривалість у днях")
    access_time = models.CharField(max_length=50, help_text="Наприклад, 7:00–16:00")
    freeze_days = models.PositiveIntegerField(default=0, help_text="Кількість днів заморозки")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.duration_days} днів"

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscriptions")
    subscription_type = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} — {self.subscription_type.name} ({self.start_date} - {self.end_date})"
