from django.db import models
from django.contrib.auth.models import User

class Training(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    trainer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_clients = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"{self.title} ({self.date} {self.start_time}-{self.end_time})"

class TrainingRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
    training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='registrations')
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} → {self.training.title} ({self.training.date})"
